import csv
import logging
logging.basicConfig(level=logging.WARNING)


class Util:
  def readData(self, filePath):
    with open(filePath, newline='') as file:
      reader = csv.reader(file)
      res = list(map(self.mapData, reader))
    return res

  def mapData(self, item):
    # Time Open	High	Low	Close	Volume
    return {
        "date": item[0],
        "open": float(item[1]),
        "high": float(item[2]),
        "low": float(item[3]),
        "close": float(item[4]),
        "volume": float(item[5])
    }
