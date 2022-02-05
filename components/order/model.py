from mongoengine import *
from config.enum import MarketEnum, ForexSymbol, BrokerEnum


class Order(Document):
  backtest = ReferenceField()