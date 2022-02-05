from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

import backtrader as bt
import backtrader.feed as feed
from backtrader import date2num, num2date

from datetime import datetime, timedelta


from urllib.parse import quote_plus
import pymongo

import os
import logging
logging.basicConfig(level=os.environ.get("LOGLEVEL", "DEBUG"))
log = logging.getLogger(__name__)


class MongoDB(feed.DataBase):
  params = (
      ('port', '27020'),
      ('host', 'mongo'),
      ('database', None),
      ('username', None),
      ('password', None),
      ('collection', 'forex'),
      ('symbol', 'EURUSD'),
      ('timeframe', bt.TimeFrame.Minutes),
      # ('fromdate', None),
      # ('todate', datetime.now()),
      ('high', 'high'),
      ('low', 'low'),
      ('open', 'open'),
      ('close', 'close'),
      ('volume', 'volume'),
      ('ointerest', 'ointerest'),
  )

  def start(self):
    super(MongoDB, self).start()
    uri = "mongodb://%s:%s@%s:%s" % (
        quote_plus(self.p.username), quote_plus(self.p.password), quote_plus(self.p.host), self.p.port)
    mng_client = pymongo.MongoClient(uri)
    mng_db = mng_client[self.p.database]
    db_collection = mng_db.get_collection(self.p.collection)

    delta = timedelta(days=14)
    now = datetime.now()

    fromdate = self.p.fromdate if self.p.fromdate else (now - delta)
    todate = self.p.todate if self.p.todate else now
    log.info("fromdate: %s todate: %s", fromdate, todate)
    result = db_collection.find(
        {
            "$and": [{"datetime": {"$gte": fromdate}},
                     {"datetime": {"$lte": todate}}]
        }
    )
    # for i in result:
    #   log.info(i)

    self.biter = iter(result)

  def _load(self):
    try:
      bar = next(self.biter)

    except StopIteration:
      return False
    self.lines.datetime[0] = date2num(bar['datetime'])
    self.lines.open[0] = bar['open']
    self.lines.high[0] = bar['high']
    self.lines.low[0] = bar['low']
    self.lines.close[0] = bar['close']
    self.lines.volume[0] = bar['volume']
    return True
