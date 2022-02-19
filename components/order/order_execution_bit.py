from umongo import EmbeddedDocument
from umongo.fields import *
from utils.mongo_async import instance


@instance.register
class OrderExecutionBit(EmbeddedDocument):
  dt = DateTimeField(allow_none=True)
  size = FloatField(allow_none=True)
  price = FloatField(allow_none=True)
  closed = FloatField(allow_none=True)
  opened = FloatField(allow_none=True)
  openedvalue = FloatField(allow_none=True)
  closedvalue = FloatField(allow_none=True)
  closedcomm = FloatField(allow_none=True)
  openedcomm = FloatField(allow_none=True)
  value = FloatField(allow_none=True)
  comm = FloatField(allow_none=True)
  pnl = FloatField(allow_none=True)
  psize = FloatField(allow_none=True)
  pprice = FloatField(allow_none=True)
