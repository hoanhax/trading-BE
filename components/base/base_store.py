class BaseStore:
  def __init__(self, Model):
    self.Model = Model

  def create(self, data):
    model = self.Model(**data)
    model.save()
    return model

  def list(self, limit, offset):
    models = self.Model.objects[offset:(offset + limit)]
    return models

  def update(self, objectId, data):
    model = self.Model.objects(id=objectId).update_one(**data)
    model.save()
    return model

  def remove(self, objectId):
    model = self.Model.objects(id=objectId)
    model.delete()
    return model
