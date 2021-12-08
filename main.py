from strawberry.aiohttp.views import GraphQLView
import aiohttp_cors
from aiohttp import web
import socketio
import os
from websocket.handler import SocketHandler
import logging
logging.basicConfig(level=logging.WARNING)
# logging.basicConfig(level=os.environ.get("LOGLEVEL", "WARNING"))
logging.getLogger('asyncio').setLevel(logging.WARNING)

sio = socketio.AsyncServer(async_mode='aiohttp', cors_allowed_origins='*')

app = web.Application()
sio.attach(app)

socketHandler = SocketHandler(sio)
socketHandler.register()

if __name__ == '__main__':
  web.run_app(app, access_log=None)
