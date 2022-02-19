from umongo import Document, EmbeddedDocument
from umongo.fields import *
# from config.enum import MarketEnum, MarketDB, ForexSymbol, BrokerEnum
from utils.mongo_async import instance

from components.trading.model import Trading
from config.enum import OrderStatus

from .order_data import OrderData


@instance.register
class Order(Document):
  trading = ReferenceField(Trading)
  status = IntField(required=True)
  ref = IntField()
  created = EmbeddedField(OrderData)
  executed = EmbeddedField(OrderData)
  info = DictField()
  isbuy = BooleanField()
  issell = BooleanField()
  isalive = BooleanField()
