from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

import backtrader as bt
import backtrader.feed as feed
from backtrader import date2num

import datetime as dt
from datetime import date, datetime, timedelta


import influxdb_client
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS
from json import dumps


import os
import logging
logging.basicConfig(level=os.environ.get("LOGLEVEL", "DEBUG"))
log = logging.getLogger(__name__)


class InfluxDB(feed.DataBase):
  params = (
      ('name', 'influxdb'),
      ('port', '8086'),
      ('url', None),
      ('bucket', None),
      ('org', None),
      ('token', None),
      ('symbol', 'EURUSD'),
      ('timeframe', bt.TimeFrame.Minutes),
      ('fromdate', None),
      ('todate', datetime.now()),
      ('high', 'high'),
      ('low', 'low'),
      ('open', 'open'),
      ('close', 'close'),
      ('volume', 'volume'),
      ('ointerest', 'oi'),
  )

  def start(self):
    super(InfluxDB, self).start()
    # try:
    #   self.ndb = InfluxDBClient(
    #       url=self.p.url, token=self.p.token, org=self.p.org)
    # # except InfluxDBClientError as err:
    # except:
    #   print('Failed to establish connection to InfluxDB')

    ndb = InfluxDBClient(
        url=self.p.url, token=self.p.token, org=self.p.org)

    query_api = ndb.query_api()

    delta = timedelta(days=12)

    now = datetime.now()

    fromdate = self.p.fromdate if self.p.fromdate else (now - delta)
    todate = self.p.todate if self.p.todate else now

    log.info(fromdate)
    log.info(todate)

    start = fromdate.strftime("%Y-%m-%dT%H:%M:%SZ")
    stop = todate.strftime("%Y-%m-%dT%H:%M:%SZ")

    query = f' from(bucket:"forex")\
                  |> range(start: {start}, stop: {stop})\
                  |> filter(fn: (r) => r.symbol == "{self.p.symbol}")\
                  |> pivot(rowKey:["_time"], columnKey: ["_field"], valueColumn: "_value") '

    tables = query_api.query(org=self.p.org, query=query)
    results = []
    for table in tables:
      for record in table.records:
        data = {
            "datetime": record.get_time(),
            "symbol": record.values.get('symbol'),
            "open": record.values.get('open'),
            "high": record.values.get('high'),
            "close": record.values.get('close'),
            "low": record.values.get('low'),
            "volume": record.values.get('volume'),
        }
        results.append(data)
    self.biter = iter(results)

  def _load(self):
    try:
      bar = next(self.biter)
    except StopIteration:
      return False

    self.l.datetime[0] = date2num(bar['datetime'])
    self.l.open[0] = bar['open']
    self.l.high[0] = bar['high']
    self.l.low[0] = bar['low']
    self.l.close[0] = bar['close']
    self.l.volume[0] = bar['volume']

    return True

  def json_serial(self, obj):
    if isinstance(obj, (datetime, date)):
      return obj.isoformat()
    raise TypeError("Type %s not serializable" % type(obj))
