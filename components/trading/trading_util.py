from datetime import datetime
from log.logger import log


def convertOrder(order):
  data = {
      "status": order.status,
      "ref": order.ref,
      "created": convertOrderData(order.created),
      "executed": convertOrderData(order.executed),
      "info": order.info,
      "isbuy": order.isbuy(),
      "issell": order.issell(),
      "isalive": order.alive()
  }
  return data


def convertOrderData(orderData):
  orderData = {
      "exbits": convertOrderExecutionBits(orderData.exbits),
      "dt": datetime.fromtimestamp(orderData.dt) if orderData.dt else None,
      "size": orderData.size,
      "price": orderData.price,
      "pricelimit": orderData.pricelimit,
      "trailamount": orderData.trailamount,
      "trailpercent": orderData.trailpercent,
      "value": orderData.value,
      "comm": orderData.comm,
      "pnl": orderData.pnl,
      "psize": orderData.psize,
      "pprice": orderData.pprice
  }
  return orderData


def convertOrderExecutionBits(orderExecutionBits):
  items = []
  for orderExecutionBit in orderExecutionBits:
    item = {
        "dt": datetime.fromtimestamp(orderExecutionBit.dt),
        "size": orderExecutionBit.size,
        "price": orderExecutionBit.price,
        "closed": orderExecutionBit.closed,
        "opened": orderExecutionBit.opened,
        "openedvalue": orderExecutionBit.openedvalue,
        "closedvalue": orderExecutionBit.closedvalue,
        "closedcomm": orderExecutionBit.closedcomm,
        "openedcomm": orderExecutionBit.openedcomm,
        "value": orderExecutionBit.value,
        "comm": orderExecutionBit.comm,
        "pnl": orderExecutionBit.pnl,
        "psize": orderExecutionBit.psize,
        "pprice": orderExecutionBit.pprice
    }
    items.append(item)
  return items
