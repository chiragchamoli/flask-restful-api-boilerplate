# Author: Chirag Chamoli
# -*- coding: utf-8 -*-
from aahho.ext.pymongo import AMongoHelper
from aahho.models import db


class SitesModel(AMongoHelper):

    _collection_name_ = "sites"

    def __init__(self):
        super(SitesModel, self).__init__()
        self.conn = db[self._collection_name_]

    def create(self, user_id):
        return str(self.conn.insert_one({'user_id' : user_id}).inserted_id)

    def get_users_sites(self, user_id):
        return self.conn.find_one({'user_id': user_id})

