import backtrader as bt
import datetime  # For datetime objects
import os.path  # To manage paths
import sys  # To find out the script name (in argv[0])
import logging
logging.basicConfig(level=os.environ.get("LOGLEVEL", "DEBUG"))
log = logging.getLogger(__name__)


class Trading:
  def __init__(self, dataPath, strategy):
    self.dataPath = dataPath
    self.strategy = strategy
    self.cerebro = bt.Cerebro()
    log.debug('init')
    self.initialize()

  def initialize(self):
    self.cerebro.addstrategy(self.strategy)

    # Datas are in a subfolder of the samples. Need to find where the script is
    # because it could have been called from anywhere
    # modpath = os.path.dirname(os.path.abspath(sys.argv[0]))
    # https://eatradingacademy.com/software/forex-historical-data/
    # Time	Open	High	Low	Close	Volume
    # datapath = os.path.join(modpath, self.dataPath)

    # Create a Data Feed
    data = bt.feeds.GenericCSVData(
        dataname=self.dataPath,
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
    self.cerebro.adddata(data)

    # Set our desired cash start
    self.cerebro.broker.setcash(100000.0)

  def run(self):
    log.debug('run trading')
    self.cerebro.run()
