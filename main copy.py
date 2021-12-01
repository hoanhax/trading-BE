from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

import datetime  # For datetime objects
import os.path  # To manage paths
import sys  # To find out the script name (in argv[0])

import backtrader as bt

from components.strategy.test_strategy import TestStrategy

if __name__ == '__main__':
  # Create a cerebro entity
  cerebro = bt.Cerebro()

  # Add a strategy
  cerebro.addstrategy(TestStrategy)

  # Datas are in a subfolder of the samples. Need to find where the script is
  # because it could have been called from anywhere
  modpath = os.path.dirname(os.path.abspath(sys.argv[0]))
  # https://eatradingacademy.com/software/forex-historical-data/
  # Time	Open	High	Low	Close	Volume
  datapath = os.path.join(modpath, './data/EURUSD_D1.csv')

  # Create a Data Feed
  data = bt.feeds.GenericCSVData(
      dataname=datapath,

      fromdate=datetime.datetime(2020, 1, 1),
      todate=datetime.datetime(2021, 10, 31),

      nullvalue=0.0,

      dtformat=('%Y-%m-%d %H:%M'),

      datetime=0,
      open=1,
      high=2,
      low=3,
      close=4,
      volume=5,
      openinterest=-1
  )

  # Add the Data Feed to Cerebro
  cerebro.adddata(data)

  # Set our desired cash start
  cerebro.broker.setcash(100000.0)

  # Print out the starting conditions
  print('Starting Portfolio Value: %.2f' % cerebro.broker.getvalue())

  # Run over everything
  cerebro.run()
  # cerebro.plot()
  # Print out the final result
  print('Final Portfolio Value: %.2f' % cerebro.broker.getvalue())
