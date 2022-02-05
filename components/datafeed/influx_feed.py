from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

import backtrader as bt
import backtrader.feed as feed
from backtrader import date2num

import datetime as dt
from datetime import date, datetime, timedelta


from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS


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
    log.info('start read data')
    log.info(datetime.now())
    ndb = InfluxDBClient(
        url=self.p.url, token=self.p.token, org=self.p.org)

    query_api = ndb.query_api()

    delta = timedelta(days=365)

    now = datetime.now()

    fromdate = self.p.fromdate if self.p.fromdate else (now - delta)
    todate = self.p.todate if self.p.todate else now

    start = fromdate.strftime("%Y-%m-%dT%H:%M:%SZ")
    stop = todate.strftime("%Y-%m-%dT%H:%M:%SZ")
    log.info(start)
    log.info(stop)
    query = f' from(bucket:"forex")\
                  |> range(start: {start}, stop: {stop})\
                  |> filter(fn: (r) => r.symbol == "{self.p.symbol}")\
                  |> pivot(rowKey:["_time"], columnKey: ["_field"], valueColumn: "_value")\
                  |> duplicate(column: "_time", as: "datetime") '
    # query = f' from(bucket:"forex")\
    #               |> range(start: {start}, stop: {stop})\
    #               |> filter(fn: (r) => r.symbol == "{self.p.symbol}")\
    #               |> pivot(rowKey:["_time"], columnKey: ["_field"], valueColumn: "_value") '
    tables = query_api.query(org=self.p.org, query=query)

    self.biter = iter(tables[0])

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
