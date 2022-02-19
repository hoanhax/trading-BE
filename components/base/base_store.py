from log.logger import log
from pymongo import ReturnDocument


class BaseStore:
  def __init__(self, Model):
    self.Model = Model

  async def create(self, data):
    model = self.Model(**data)
    await model.commit()
    return model

  async def list(self, limit, offset):
    models = await self.Model.find().limit(limit).skip(offset)
    return models

  async def update(self, objectId, data):
    model = await self.Model.find_one_and_update(
        {'_id': objectId},
        {'$set': data},
        return_document=ReturnDocument.AFTER)
    return model

  async def updateUpsert(self, objectId, data):
    model = await self.Model.find_one_and_update(
        {'_id': objectId},
        {'$set': data},
        upsert=True, return_document=ReturnDocument.AFTER)
    return model

  async def remove(self, objectId):
    model = await self.Model.find_one_and_delete({'_id': objectId})
    return model
