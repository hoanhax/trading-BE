from trading.trading import Trading
from trading.strategy.test_strategy import TestStrategy

from websocket.handler import SocketHandler
import socketio
from aiohttp import web
import aiohttp_cors
from strawberry.aiohttp.views import GraphQLView
sio = socketio.AsyncServer(async_mode='aiohttp', cors_allowed_origins='*')

trading = Trading('./data/EURUSD_D1.csv', TestStrategy)

app = web.Application()
sio.attach(app)

socketHandler = SocketHandler(sio)
socketHandler.register()


if __name__ == '__main__':
  print('main')
  web.run_app(app)
  trading.run()
