from mongoengine import *
from config.enum import MarketEnum, ForexSymbol, BrokerEnum


class BackTest(Document):
  symbol = EnumField(ForexSymbol, required=True)
  from_date = DateTimeField(required=True)
  to_date = DateTimeField(required=True)
  market = EnumField(MarketEnum, required=True)
  broker = EnumField(BrokerEnum, required=True)
  cash = IntField(required=True)
  # Strategy used on this backtest, we will store function next as string of strategy
  strategy = StringField()
