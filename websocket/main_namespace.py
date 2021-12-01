import socketio


class MainNamespace(socketio.AsyncNamespace):
  def on_connect(self, sid, environ):
    pass

  def on_disconnect(self, sid):
    pass

  async def on_my_event(self, sid, data):
    await self.emit('my_response', data)
