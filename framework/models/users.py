# Author: Chirag Chamoli
# -*- coding: utf-8 -*-
from werkzeug.security import check_password_hash
from aahho.exceptions import DBException
from aahho.ext.pymongo import AMongoHelper
from aahho.models import db

users_fields = ["guid","full_name","email","phone","password","ver","create_at","updated_at","username","profile_image"]

class UserModel(AMongoHelper):
    _collection_name_ = "users"
    def __init__(self):
        super(UserModel, self).__init__()
        self.conn = db[self._collection_name_]

    def get_all(self):
        try:
            response = self.conn.find({})
            if response is None:
                return None
            else:
                return response
        except:
            raise DBException(DBException.messages['DB_CONNECTIONS_UNKNOWN'])

    def get_by_email(self,email):
        try:
            return self.conn.find_one({'email': email})
        except:
            return None
    def check_password(self,hashed,plain_text):
        return check_password_hash(hashed, plain_text)

    def login_required_fields(self):
        return ['type','email','password']

    def create(self,args):
        return self.conn.insert_one(args).inserted_id


# _Users_ = db.users