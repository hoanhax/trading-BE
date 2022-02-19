from email.policy import default
from umongo import Document
from umongo.fields import *
# from config.enum import MarketEnum, MarketDB, ForexSymbol, BrokerEnum
from utils.mongo_async import instance


@instance.register
class Trading(Document):
  symbol = StringField(required=True)
  fromdate = DateTimeField(required=True)
  todate = DateTimeField(required=True)
  database = StringField(required=True)
  market = StringField(required=True)
  broker = StringField(required=True)
  cash = IntField(required=True)
  # Strategy used on this backtest, we will store function next as string of strategy
  strategy = StringField()
