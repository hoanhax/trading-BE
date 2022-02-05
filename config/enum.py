from enum import Enum


class MainEnum (Enum):
  CANDELSTICKET_DATA = 'candlesticket_data'
  ORDER_DATA = 'order_data'
  GET_CANDLESTICKETS = 'get_candlestickets'
  GET_ORDERS = 'get_orders'


class MarketEnum (Enum):
  FOREX = 'forex'
  STOCK = 'stock'
  CRYPTO = 'crypto'


class ForexSymbol (Enum):
  EURUSD = 'EURUSD'
  USDCAD = 'USDCAD'
  GBPUSD = 'GBPUSD'


class OrderEnum (Enum):
  CREATED = 'created'


class BrokerEnum (Enum):
  NONE = 'none'


class OrderStatus (Enum):
  SUBMITTED = 'Submitted'  # sent to the broker and awaiting confirmation
  ACCEPTED = 'Accepted'  # accepted by the broker
  PARTIAL = 'Partial'  # partially executed
  COMPLETED = 'Completed'  # fully exexcuted
  CANCELLED = 'Cancelled'  # canceled by the user
  EXPIRED = 'Expired'  # expired
  MARGIN = 'Margin'  # not enough cash to execute the order.
  REJECTED = 'Rejected'  # Rejected by the broker


class OrderType (Enum):
  # A market order will be executed with the next available price. In backtesting it will be the opening price of the next bar
  Market = 'Market'

  # An order which can only be executed at the given price or better
  Limit = 'Limit'

  Stop = 'Stop'
