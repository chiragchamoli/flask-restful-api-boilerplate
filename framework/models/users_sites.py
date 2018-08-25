# Author: Chirag Chamoli
# -*- coding: utf-8 -*-
from aahho.ext.pymongo import AMongoHelper
from aahho.models import db
from aahho.models import SitesModel
sites = SitesModel()


class UsersSitesModel(AMongoHelper):
    _collection_name_ = "users_sites"

    def __init__(self):
        super(UsersSitesModel, self).__init__()
        self.conn = db[self._collection_name_]

    def get_users_sites(self,user_id):
        try:
            return self.conn.find_one({'user_id': user_id})
        except:
            return []

    def new_site(self,user_id):
        site_id = sites.create(user_id)

        try:

            id = self.conn.insert({
                "user_id":  user_id,
                "site_id":  site_id
                }).inserted_id

            print user_id, id
            return str(id)
        except:
            return []
