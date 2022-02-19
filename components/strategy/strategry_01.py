import logging
import os
import backtrader as bt

from components.base.base_strategy import BaseStrategy

logging.basicConfig(level=os.environ.get("LOGLEVEL", "DEBUG"))
log = logging.getLogger(__name__)


class Strategy01(BaseStrategy):
  def next(self):
    # Simply log the closing price of the series from the reference
    # self.log('Close, %.5f' % self.dataclose[0])

    # Check if an order is pending ... if yes, we cannot send a 2nd one
    if self.order:
      return

    # Check if we are in the market
    if not self.position:

      # Not yet ... we MIGHT BUY if ...
      if self.dataclose[0] < self.dataclose[-1]:
        # current close less than previous close

        if self.dataclose[-1] < self.dataclose[-2]:
          # if self.dataclose[-2] < self.dataclose[-3]:
          #   # previous close less than the previous close

          # BUY, BUY, BUY!!! (with default parameters)
          self.log('BUY CREATE, %.2f' % self.dataclose[0])

          # Keep track of the created order to avoid a 2nd order
          self.order = self.buy()
    else:
      # Already in the market ... we might sell
      if len(self) >= (self.bar_executed + 5):
        # SELL, SELL, SELL!!! (with all possible default parameters)
        self.log('SELL CREATE, %.2f' % self.dataclose[0])

        # Keep track of the created order to avoid a 2nd order
        self.order = self.sell()
