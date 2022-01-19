import os
from trading.market.maket_data import MarketData
from config import setting

import logging
logging.basicConfig(level=os.environ.get("LOGLEVEL", "DEBUG"))

log = logging.getLogger(__name__)


class MarketHandler:
  def query_data(self, query):
    influxdb = setting.influxdb
    log.info(influxdb)
    marketData = MarketData(influxdb['url'], influxdb['forex_bucket'],
                            influxdb['org'], influxdb['token'])
    data = marketData.read_data('EURUSD', '-5d', '-1d')
    return data
