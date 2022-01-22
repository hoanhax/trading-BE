import backtrader as bt
import datetime  # For datetime objects
import os.path  # To manage paths
import sys  # To find out the script name (in argv[0])
import logging
logging.basicConfig(level=os.environ.get("LOGLEVEL", "DEBUG"))
log = logging.getLogger(__name__)


class Trading:
  def __init__(self, data, strategy, cash=100000):
    self.data = data
    self.strategy = strategy
    self.cerebro = bt.Cerebro()
    self.cash = cash
    self.initialize()

  def initialize(self):
    self.cerebro.addstrategy(self.strategy)

    # Add the Data Feed to Cerebro
    self.cerebro.adddata(self.data)

    # Set our desired cash start
    self.cerebro.broker.setcash(self.cash)

  def run(self):
    log.debug('run trading')
    self.cerebro.run()
