import asyncio
import backtrader as bt

from utils.class_util import method_exists
import os
import logging
logging.basicConfig(level=os.environ.get("LOGLEVEL", "DEBUG"))
log = logging.getLogger(__name__)


class BaseStrategy(bt.Strategy):
  params = (
      ('listenter', None),
  )

  def __init__(self):
    self.dataclose = self.datas[0].close
    self.datetime = self.datas[0].datetime
    self.order = None

  def log(self, txt, dt=None):
    ''' Logging function for this strategy'''
    dt = dt or self.datetime.datetime(0)
    # log.info('%s, %s' % (dt.isoformat(), txt))

  def notify_order(self, order):
    self.log('notify_order')
    if (method_exists(self.p.listenter, 'notify_order')):
      asyncio.create_task(self.p.listenter.notify_order(order))

    if order.status in [order.Submitted, order.Accepted]:
      # Buy/Sell order submitted/accepted to/by broker - Nothing to do
      return

    # Check if an order has been completed
    # Attention: broker could reject order if not enough cash
    if order.status in [order.Completed]:
      if order.isbuy():
        self.log('BUY EXECUTED, %.2f' % order.executed.price)
      elif order.issell():
        self.log('SELL EXECUTED, %.2f' % order.executed.price)

      self.bar_executed = len(self)

    elif order.status in [order.Canceled, order.Margin, order.Rejected]:
      self.log('Order Canceled/Margin/Rejected')

    # Write down: no pending order
    self.order = None

  def notify_trade(self, trade):
    pass
    # self.log('notify_trade')

  def notify_cashvalue(self, cash, value):
    if (method_exists(self.p.listenter, 'notify_cashvalue')):
      self.p.listenter.notify_cashvalue(cash, value)

    # self.log('notify_cashvalue')

  def notify_fund(self, cash, value, fundvalue, shares):
    if (method_exists(self.p.listenter, 'notify_fund')):
      self.p.listenter.notify_fund(cash, value, fundvalue, shares)

    # self.log('notify_fund')
