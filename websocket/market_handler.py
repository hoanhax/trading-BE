import os
from trading.market.maket_data import MarketData
from config import setting
from datetime import datetime

import logging
logging.basicConfig(level=os.environ.get("LOGLEVEL", "DEBUG"))

log = logging.getLogger(__name__)


class MarketHandler:
  def query_data(self, query):
    influxdb = setting.influxdb
    log.info(datetime.now())
    marketData = MarketData(influxdb['url'], influxdb['forex_bucket'],
                            influxdb['org'], influxdb['token'])
    data = marketData.read_data('EURUSD', '-365d', '-1d')
    log.info(datetime.now())
    return data
