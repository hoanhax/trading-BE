import datetime

from components.trading.handler import Handler
import backtrader as bt
from config.enum import *
from components.strategy.strategry_01 import Strategy01
from config.setting import mongodb

DEFAULT_CASH = 1000


class Manager:
  # def test01(self):
  #   influxdb = setting.influxdb
  #   data = InfluxDB(
  #       url=influxdb['url'],
  #       org=influxdb['org'],
  #       token=influxdb['token'],
  #       symbol='EURUSD'
  #   )
  #   # Creating backtest record to store in db
  #   trading = Handler(data, Strategy01)
  #   trading.initialize()
  #   trading.run()

  async def test02(self):
    fromdate = datetime.datetime(2022, 1, 13)
    todate = datetime.datetime(2022, 1, 14)
    timeframe = bt.TimeFrame.Minutes
    market = MarketEnum.FOREX.value
    symbol = ForexSymbol.EURUSD.value
    cash = 10000
    mongoConfig = {
        "port": mongodb['port'],
        "host": mongodb['host'],
        "username": mongodb['username'],
        "password": mongodb['password'],
        "database": mongodb['database'],
        "collection": mongodb['collection'],
        "symbol": mongodb['symbol']
    }
    tradingConfig = {
        "fromdate": fromdate,
        "todate": todate,
        "timeframe": timeframe,
        "market": market,
        "broker": BrokerEnum.NONE.value
    }
    tradingHandler = Handler(tradingConfig, mongoConfig, Strategy01, cash)
    await tradingHandler.initialize()
    await tradingHandler.run()
