from trading.backtest.backtest import BackTest
from trading.datafeed.influx_feed import InfluxDB

from config import setting

from trading.strategy.strategry_01 import Strategy01


class BackTest01 (BackTest):
  def __init__(self, symbol='EURUSD'):
    influxdb = setting.influxdb
    data = InfluxDB(
        host=influxdb['url'],
        org=influxdb['org'],
        token=influxdb['token'],
        symbol=symbol
    )
    super().__init__(data, Strategy01)
