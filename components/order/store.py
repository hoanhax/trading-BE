from components.base.base_store import BaseStore
from .order import Order
from pymongo import ReturnDocument
from log.logger import log
import json


class OrderStore(BaseStore):
  def __init__(self):
    super().__init__(Order)

  async def updateByRef(self, order):
    # model = await self.Model.find_one_and_update(
    #     {'ref': ref},
    #     {'$set': order},
    #     upsert=True, return_document=ReturnDocument.AFTER)
    model = self.Model(**order)
    await model.commit()
    # log.info(model)
    return model
