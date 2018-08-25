# Author: Chirag Chamoli
# -*- coding: utf-8 -*-

# Author: Chirag Chamoli
# -*- coding: utf-8 -*-
import os

current_env = os.environ.get('EDYST_ENV_KEY', 'Environment is not defined')
ENVV = current_env
ED_SETTING_ROOT = os.path.abspath(os.path.dirname(__file__))
ENV_FOLDER = '/'+current_env+'/'
THIS_PATH = ED_SETTING_ROOT + ENV_FOLDER
PATH_TO_CERTS = ED_SETTING_ROOT + ENV_FOLDER + '/certs/'

class Config(object):
    SETTING_ROOT = os.path.abspath(os.path.dirname(__file__))
    URL_PREFIX = '/api'


class ProdConfig(Config):
    SECRET_KEY = '$-\xac\xc6\x12*\xec\xa0W\xc8\xcf\xc3<\xf5g\xbbC5\x13\x19i0\xf4\x87'
    DB_USER = 'postgres'
    DB_PASSWORD = 'facebook42EDYST'
    DB_NAME = 'production'
    DB_HOST = 'localhost'
    DB_PORT = 5432
    SQLALCHEMY_DATABASE_URI = 'postgresql://{user}:{password}@{host}:{port}/{name}'.format(
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT,
        name=DB_NAME,
    )


class StageConfig(Config):
    PORT = 9993
    HOST = '0.0.0.0'
    DEBUG = True
    USER_TOKEN_EXP_TIME = 86400
    SECRET_KEY = 'n53qw*ci9a(&06igg1ju^%klxq**(l!r-_)e(%-p0+v7$i#a&ep8ro3i)(7u3%13=nio2&o%q_ys1@1ivog)7q1-7%1--43(cdgi(3#k2@h8pxoa_z0fcier8w4e)60r'

    DB_USER = 'postgres'
    DB_PASSWORD = 'asdfasdf'
    DB_NAME = 'db9'
    DB_HOST = 'localhost'
    DB_PORT = 5432
    SQLALCHEMY_DATABASE_URI = 'postgresql://{user}:{password}@{host}:{port}/{name}'.format(
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT,
        name=DB_NAME,
    )

class LocalConfig(Config):
    PORT = 9991
    HOST = '0.0.0.0'
    DEBUG = True
    GOOGLE_BUCKET_NAME = 'dev_edyst'
    USER_TOKEN_EXP_TIME = 604800
    SECRET_KEY = '\x89\xac\x9ab\x8b_R\x9b\xe1\xd5<4]\x88\x98z\x8c\xc6\xd6\xc0\x80\xe4N{'
    DB_USER = 'localdev'
    DB_PASSWORD = 'asdfasdf'
    DB_NAME = 'noob111'
    DB_HOST = 'localhost'

    DB_PORT = 5432
    SQLALCHEMY_DATABASE_URI = 'postgresql://{user}:{password}@{host}:{port}/{name}'.format(
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT,
        name=DB_NAME,
    )


configs = {
  'local'  : LocalConfig,
  'staging' : StageConfig,
  'prod': ProdConfig
}
