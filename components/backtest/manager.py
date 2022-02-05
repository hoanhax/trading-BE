from components.trading import Trading
from components.datafeed.influx_feed import InfluxDB
from components.datafeed.mongo_feed import MongoDB

import backtrader as bt
from config import setting
import datetime
from components.strategy.strategry_01 import Strategy01

DEFAULT_CASH = 1000


class Manager:
  def test01(self):
    influxdb = setting.influxdb
    data = InfluxDB(
        url=influxdb['url'],
        org=influxdb['org'],
        token=influxdb['token'],
        symbol='EURUSD'
    )
    # Creating backtest record to store in db
    trading = Trading(data, Strategy01)
    trading.initialize()
    trading.run()

  def test02(self):
    mongodb = setting.mongodb
    data = MongoDB(
        host=mongodb['host'],
        username=mongodb['username'],
        password=mongodb['password'],
        port=mongodb['port'],
        timeframe=bt.TimeFrame.Minutes,
        fromdate=datetime.datetime(2022, 1, 13),
        todate=datetime.datetime(2022, 1, 14),
        database=mongodb['database'],
        symbol=mongodb['symbol']
    )
    trading = Trading(data, Strategy01)
    # trading.initialize()
    trading.run()
