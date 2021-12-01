from websocket.main_namespace import MainNamespace


class SocketHandler:
  def __init__(self, sio):
    self.sio = sio

  def register(self):
    self.sio.register_namespace(MainNamespace('/'))
