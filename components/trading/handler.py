from .store import TradingStore
import os.path  # To manage paths

import backtrader as bt
import pytz
import json

from components.datafeed.mongo_feed import MongoDB
from components.order.store import OrderStore

from log.logger import log
from libs.unsync import unsync
from .trading_util import convertOrder

# import logging
# from config.enum import BrokerEnum
# logging.basicConfig(level=os.environ.get("LOGLEVEL", "DEBUG"))
# log = logging.getLogger(__name__)


class Handler:
  def __init__(self, tradingConfig, mongoConfig, Strategy, cash=100000):
    self.tradingConfig = tradingConfig
    self.mongoConfig = mongoConfig

    self.Strategy = Strategy
    self.cash = cash

    # self.initialize()

  def run(self):
    log.info('run test02')
    self.cerebro.addstrategy(self.Strategy, listenter=self)
    self.cerebro.adddata(self.data)
    self.cerebro.broker.setcash(self.cash)

    timezone = pytz.timezone('UTC')
    self.cerebro.run(tz=timezone)

  """ Notify handler from strategy """

  @unsync
  async def notify_order(self, order):
    try:
      orderData = convertOrder(order)
      log.info(self.trading.id)
      orderData['trading'] = self.trading.id
      # log.info(orderData)
      await self.orderStore.updateByRef(orderData)
    except Exception as e:
      log.error(e)

  def notify_trade(self, trade):
    pass

  def notify_cashvalue(self, cash, value):
    pass

  def notify_fund(self, cash, value, fundvalue, shares):
    pass

  """ Privates methods """

  async def initialize(self):
    # Add the Data Feed to Cerebro
    self.cerebro = bt.Cerebro()
    self.orderStore = OrderStore()
    self._generateData()
    await self._storeTrading()

  def _generateData(self):
    data = MongoDB(
        host=self.mongoConfig["host"],
        username=self.mongoConfig["username"],
        password=self.mongoConfig["password"],
        port=self.mongoConfig["port"],
        database=self.mongoConfig["database"],
        symbol=self.mongoConfig["symbol"],
        timeframe=self.tradingConfig["timeframe"],
        fromdate=self.tradingConfig["fromdate"],
        todate=self.tradingConfig["todate"],
    )
    self.data = data

  async def _storeTrading(self):
    tradingStore = TradingStore()
    tradingInfo = {
        "symbol": self.mongoConfig["symbol"],
        "database": self.mongoConfig["database"],
        "fromdate": self.tradingConfig["fromdate"],
        "todate": self.tradingConfig["todate"],
        "market": self.tradingConfig["market"],
        "broker": self.tradingConfig["broker"],
        "cash": self.cash,
        "strategy": self.Strategy.__name__
    }
    trading = await tradingStore.create(tradingInfo)
    self.trading = trading
