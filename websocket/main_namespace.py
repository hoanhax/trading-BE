from trading.backtest.backtest import BackTest
from trading.strategy.test_strategy import TestStrategy
from trading.trading import Trading
from websocket.market_handler import MarketHandler

import socketio
from config.enum import MainEnum
import os

from websocket.util import Util

import logging
logging.basicConfig(level=os.environ.get("LOGLEVEL", "DEBUG"))

log = logging.getLogger(__name__)


class MainNamespace(socketio.AsyncNamespace):
  def on_connect(self, sid, environ):
    pass

  def on_disconnect(self, sid):
    pass

  def on_get_data(self, sid, data):
    util = Util()
    absolutePath = os.path.join(os.getcwd(), 'data/EURUSD_D1.csv')
    log.debug(absolutePath)
    response = util.readData(absolutePath)
    return response
    # self.emit('')
    # pass

  def on_get_market_data(self, sid, data):
    # pass
    market_handler = MarketHandler()
    response = market_handler.query_data(None)
    # log.info(response)
    return response

  async def on_get_candlestickets(self, sid, data):
    pass

  async def on_get_orders(self, sid, data):
    pass

  async def on_run_trading(self, sid, data):
    absolutePath = os.path.join(os.getcwd(), 'data/EURUSD_D1.csv')
    trading = Trading(absolutePath, TestStrategy)
    trading.run()

  async def on_run_trading_01(self, sid, data):
    backtest = BackTest()
    backtest.test01()

  async def on_run_trading_02(self, sid, data):
    backtest = BackTest()
    backtest.test02()
