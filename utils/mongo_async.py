from urllib.parse import quote_plus

import asyncio

from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase
from umongo.frameworks import MotorAsyncIOInstance

import os
import logging
logging.basicConfig(level=os.environ.get("LOGLEVEL", "DEBUG"))

log = logging.getLogger(__name__)

instance = MotorAsyncIOInstance()


class MongoAsync():
  def __init__(self, config, database=None):
    self.config = config
    self.database = database

  async def init_mongo(self, config, database):
    loop = asyncio.get_event_loop()
    uri = self.generateUri(config, database)
    client = AsyncIOMotorClient(uri, io_loop=loop)
    # return conn.get_database()
    return client

  async def setup_mongo(self, app) -> None:
    """Setup mongo with async

    Args:
        app (WebApplication): aiohttp webapplication
        config (dic): Mongodb configuration
        database (string): Datbasename to connect
    Return:
      None
    """
    database = self.database if self.database else self.config['database']
    app['mongo_client'] = await self.init_mongo(self.config, database)
    if (database):
      app['db'] = app['mongo_client'][database]
      instance.set_db(app['db'])
      app['mongo_instance'] = instance

    log.info(app['db'])

    async def close_mongo(self):
      if (app['db']):
        app['db'].client.close()

    app.on_cleanup.append(close_mongo)

  def generateUri(self, config, database):
    uri = None
    if (database):
      uri = "mongodb://%s:%s@%s:%s/%s?authSource=admin" % (
          quote_plus(config["username"]),
          quote_plus(config["password"]),
          quote_plus(config["host"]),
          config["port"],
          quote_plus(database))
    else:
      uri = "mongodb://%s:%s@%s:%s/%s?authSource=admin" % (
          quote_plus(config["username"]),
          quote_plus(config["password"]),
          quote_plus(config["host"]),
          config["port"])
    return uri
