from components.base.base_store import BaseStore
from .model import Trading


class TradingStore (BaseStore):
  def __init__(self):
    super().__init__(Trading)
