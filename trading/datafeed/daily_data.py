import itertools
import backtrader as bt

class MyCSVData(bt.CSVDataBase):

    def start(self):
        # Nothing to do for this data feed type
        pass

    def stop(self):
        # Nothing to do for this data feed type
        pass

    def _loadline(self, linetokens):
        i = itertools.count(0)

        dttxt = linetokens[next(i)]
        # Format is YYYY-MM-DD
        y = int(dttxt[0:4])
        m = int(dttxt[5:7])
        d = int(dttxt[8:10])

        dt = datetime.datetime(y, m, d)
        dtnum = date2num(dt)

        self.lines.datetime[0] = dtnum
        self.lines.open[0] = float(linetokens[next(i)])
        self.lines.high[0] = float(linetokens[next(i)])
        self.lines.low[0] = float(linetokens[next(i)])
        self.lines.close[0] = float(linetokens[next(i)])
        self.lines.volume[0] = float(linetokens[next(i)])
        # self.lines.openinterest[0] = float(linetokens[next(i)])

        return True
