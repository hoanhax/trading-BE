import os
from datetime import date, datetime

import influxdb_client
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS
from json import dumps

import logging
logging.basicConfig(level=os.environ.get("LOGLEVEL", "DEBUG"))

log = logging.getLogger(__name__)


class MarketData ():
  def __init__(self, url, bucket, org, token):
    self.url = url
    self.bucket = bucket
    self.org = org
    self.token = token
    self.client = influxdb_client.InfluxDBClient(
        url=self.url,
        token=self.token,
        org=self.org
    )

  def read_data(self, symbol, start, stop):
    with InfluxDBClient(url=self.url, token=self.token, org=self.org) as client:

      query_api = client.query_api()
      # query = f' from(bucket:{self.bucket})\
      #             |> range(start: {begin}, end: {end})\
      #             |> filter(fn: (r) => r.symbol == {symbol}) '
      query = f' from(bucket:"forex")\
                  |> range(start: {start}, stop: {stop})\
                  |> filter(fn: (r) => r.symbol == "{symbol}")\
                  |> pivot(rowKey:["_time"], columnKey: ["_field"], valueColumn: "_value") '
      # query = 'from(bucket: "forex") |> range(start: -30d)'
      tables = query_api.query(org=self.org, query=query)
      results = []
      log.info(len(tables))
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
      return results

  def write_data():
    pass

  def json_serial(self, obj):
    if isinstance(obj, (datetime, date)):
      return obj.isoformat()
    raise TypeError("Type %s not serializable" % type(obj))
