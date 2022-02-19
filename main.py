from config.setting import mongodb
from utils.mongo_async import MongoAsync
from strawberry.aiohttp.views import GraphQLView
from aiohttp import web
import socketio
from websocket.handler import SocketHandler
import logging
logging.basicConfig(level=logging.WARNING)
# logging.basicConfig(level=os.environ.get("LOGLEVEL", "WARNING"))
logging.getLogger('asyncio').setLevel(logging.WARNING)

# Connect mongodb
# mongoUtil = MongoUtil()
# mongoUtil.connect(mongodb)


# app = web.Application()
# sio.attach(app)

app = web.Application()


def init():
  print('init')
  mongoUtil = MongoAsync(mongodb)
  app.on_startup.append(mongoUtil.setup_mongo)
  # app.on_startup.append(ensure_indexes)  # in production should be in CD stage
  # app.add_routes(routes)
  sio = socketio.AsyncServer(async_mode='aiohttp', cors_allowed_origins='*')
  sio.attach(app)
  socketHandler = SocketHandler(sio)
  socketHandler.register()
  return app


init()

if __name__ == '__main__':
  web.run_app(app, access_log=None)
