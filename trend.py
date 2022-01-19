from enum import Enum
from websocket.util import Util
import os
import logging
logging.basicConfig(level=os.environ.get("LOGLEVEL", "DEBUG"))

log = logging.getLogger(__name__)


class TrendEnums(Enum):
  UP = 1
  DOWN = 2
  SIDEWAY = 3


def readData():
  util = Util()
  absolutePath = os.path.join(os.getcwd(), 'data/data1.csv')
  items = util.readData(absolutePath)
  return items


def calTrend(first, second):
  firstClose = first['close']
  secondClose = second['close']
  trend = TrendEnums.DOWN if firstClose < secondClose else TrendEnums.UP if firstClose > secondClose else TrendEnums.SIDEWAY
  return trend


def analyze(items):
  result = []
  if len(items) == 1 or len(items) == 2:
    return items

  # lastValue = items[0]
  lastTrend = calTrend(items[0], items[1])

  '''
  Add first value, and add trend value to this item. We will store trend value for the first value of the trend
  example result = [{close: 1, date: xxx, open: xxx, trend: UP}, {close: 5, date: xxx, open: xxx, trend: DOWN}, {close: 3, date: xxx, open: xxx, trend: UP}]
  it mean from close:1 -> close:5 is trend UP, from close:5 -> close:3 is trend DOWN
  '''
  items[0]['trend'] = lastTrend
  result.append(items[0])
  for index in range(1, len(items)):
    preItem = items[index-1]
    item = items[index]
    trend = calTrend(preItem, item)
    # print(preItem['close'])
    # print(item['close'])
    # print(trend)
    # print(lastTrend)
    if trend != lastTrend:
      preItem['trend'] = trend
      lastTrend = trend
      result.append(preItem)
  return result


if __name__ == '__main__':
  print('readdata')
  data = readData()
  # print(data)
  result = analyze(data)
  print(result)
