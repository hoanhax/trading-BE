from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

import backtrader as bt
import backtrader.feed as feed
import datetime as dt

import influxdb_client
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS
from json import dumps


class InfluxDB(feed.DataBase):
  params = (
      ('name', 'influxdb'),
      ('host', '127.0.0.1'),
      ('port', '8086'),
      ('url', None),
      ('bucket', None),
      ('org', None),
      ('token', None),
      ('symbol', None),
      ('timeframe', bt.TimeFrame.Minutes),
      ('fromdate', None),
      ('todate', None),
      ('high', 'high'),
      ('low', 'low'),
      ('open', 'open'),
      ('close', 'close'),
      ('volume', 'volume'),
      ('ointerest', 'oi'),
  )

  def start(self):
    super(InfluxDB, self).start()
    try:
      self.client = InfluxDBClient(
          url=self.p.url, token=self.p.token, org=self.p.org)
    # except InfluxDBClientError as err:
    except:
      print('Failed to establish connection to InfluxDB')

    query_api = self.client.query_api()
    query = f' from(bucket:"forex")\
                  |> range(start: {self.p.start}, stop: {self.p.stop})\
                  |> filter(fn: (r) => r.symbol == "{self.p.symbol}")\
                  |> pivot(rowKey:["_time"], columnKey: ["_field"], valueColumn: "_value") '
    try:
      tables = query_api.query(org=self.org, query=query)
    except:
      print('InfluxDB query failed')

    results = []
    for table in tables:
      for record in table.records:
        data = {
            "time": dumps(record.get_time(), default=self.json_serial),
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

    self.l.datetime[0] = bar['time']
    self.l.open[0] = bar['open']
    self.l.high[0] = bar['high']
    self.l.low[0] = bar['low']
    self.l.close[0] = bar['close']
    self.l.volume[0] = bar['volume']

    return True
