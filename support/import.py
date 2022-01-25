#!/usr/bin/env python
import sys
import os
import pandas as pd
import pymongo
import json
from urllib.parse import quote_plus
from datetime import datetime


def import_content(filepath, collection_name='forex', db_name='market'):
  # uri = "mongodb://%s:%s@%s:%s" % (
  #     quote_plus('root'), quote_plus('4yW9wCsNYNc3RYqh'), "localhost", "27020")
  uri = "mongodb://root:4yW9wCsNYNc3RYqh@localhost:27020"
  mng_client = pymongo.MongoClient(uri)
  mng_db = mng_client[db_name]

  collist = mng_db.list_collection_names()
  # Create collection if does not exist
  print(collist)
  if collection_name not in collist:
    col = mng_db.create_collection(
        name=collection_name,
        timeseries={
            "timeField": "datetime",
            "metaField": "metadata",
            "granularity": "minutes"
        }
    )
    # db_cm = mng_db[collection_name]
    # db_cm.create_index(
    #     [("datetime", pymongo.ASCENDING)],
    #     unique=True
    # )

  db_cm = mng_db[collection_name]

  cdir = os.path.dirname(__file__)
  file_res = os.path.join(cdir, filepath)

  header_list = ["datetime", "open", "high", "low", "close", "volume"]
  df = pd.read_csv(
      file_res,
      header=None,
      names=header_list,
      dtype={"open": float, "high": float,
             "low": float, "close": float, "volume": int},
      parse_dates=['datetime'],
      date_parser=lambda col: pd.to_datetime(col, utc=True),
      # nrows=5,
      sep=',')
  # df['metadata'] = pd.Series(dict)
  # df["metadata.symbol"] = "EURUSD"
  # df["metadata"]["base"] = "EUR"
  # df["metadata"]["quote"] = "USD"

  items = json.loads(df.to_json(orient='records'))
  print(items)
  list(map(lambda item: addMetadata(item), items))
  # db_cm.delete_many({})
  result = db_cm.insert_many(items)
  # print(result.inserted_ids)
  # print(json.dumps(result, indent=1))


def addMetadata(item):
  item['metadata'] = {"symbol": "EURUSD", "base": "EUR", "quote": "USD"}
  item['datetime'] = datetime.fromtimestamp(item['datetime']/1000)
  return item


if __name__ == "__main__":
  filepath = '../data/EURUSD5_mongo.csv'
  import_content(filepath)
