from websocket.handler import SocketHandler
import socketio
from aiohttp import web
from strawberry.aiohttp.views import GraphQLView
sio = socketio.AsyncServer(async_mode='aiohttp')


app = web.Application()
sio.attach(app)

socketHandler = SocketHandler(sio)
socketHandler.register()

if __name__ == '__main__':
  web.run_app(app)
