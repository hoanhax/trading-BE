from trading.trading import Trading
from trading.datafeed.influx_feed import InfluxDB

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
