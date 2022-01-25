from trading.trading import Trading
from trading.datafeed.influx_feed import InfluxDB
from trading.datafeed.mongo_feed import MongoDB

from config import setting

from trading.strategy.strategry_01 import Strategy01


class BackTest:
  def test01(self):
    influxdb = setting.influxdb
    data = InfluxDB(
        url=influxdb['url'],
        org=influxdb['org'],
        token=influxdb['token'],
        symbol='EURUSD'
    )
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
        database=mongodb['database'],
        symbol=mongodb['symbol']
    )
    trading = Trading(data, Strategy01)
    trading.initialize()
    trading.run()
