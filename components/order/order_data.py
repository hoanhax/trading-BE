from umongo import EmbeddedDocument
from umongo.fields import *
# from config.enum import MarketEnum, MarketDB, ForexSymbol, BrokerEnum
from utils.mongo_async import instance

# https://www.backtrader.com/docu/order/#reference-order-and-associated-classes
from .order_execution_bit import OrderExecutionBit


@instance.register
class OrderData(EmbeddedDocument):
  exbits = ListField(EmbeddedField(OrderExecutionBit))
  dt = DateTimeField(allow_none=True)
  size = FloatField()
  price = FloatField()
  pricelimit = FloatField(allow_none=True)
  trailamount = FloatField(allow_none=True)
  trailpercent = FloatField(allow_none=True)
  value = FloatField()
  comm = FloatField(allow_none=True)
  pnl = FloatField(allow_none=True)
  psize = FloatField(allow_none=True)
  pprice = FloatField(allow_none=True)
