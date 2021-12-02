import socketio
from config.enum import MainEnum


class MainNamespace(socketio.AsyncNamespace):
  def on_connect(self, sid, environ):
    pass

  def on_disconnect(self, sid):
    pass

  async def on_get_candlestickets(self, sid, data):
    pass

  async def get_orders(self, sid, data):
    pass
