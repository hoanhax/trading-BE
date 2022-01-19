# #!/usr/bin/env python
# import sys
# import os
# import pandas as pd
# import pymongo
# import json
# from urllib.parse import quote_plus


# def import_content(filepath):
#   uri = "mongodb://%s:%s@%s" % (
#       quote_plus('root'), quote_plus('4yW9wCsNYNc3RYqh'), "localhost")

#   mng_client = pymongo.MongoClient(uri)

#   # mng_client = pymongo.MongoClient('localhost', 27020)
#   mng_db = mng_client['trade']
#   collection_name = 'forex'
#   db_cm = mng_db[collection_name]
#   cdir = os.path.dirname(__file__)
#   file_res = os.path.join(cdir, filepath)

#   header_list = ["timestamp", "open", "high", "low", "close", "volume"]
#   data = pd.read_csv(file_res, header=None,
#                      names=header_list, nrows=5, sep='	')

#   items = json.loads(data.to_json(orient='records'))
#   print(items)
#   # db_cm.remove()
#   # db_cm.insert(data_json)


# if __name__ == "__main__":
#   filepath = '../data/EURUSD5.csv'
#   import_content(filepath)
