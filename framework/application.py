# Author: Chirag Chamoli
# -*- coding: utf-8 -*-
# Author: Chirag Chamoli
# -*- coding: utf-8 -*-
import os
from flask import Flask

from aahho.ext.cors import cors
from aahho.framework.api.v1 import api_v1_bp, API_VERSION_V1
from aahho.configuration import Config, configs

env = os.environ.get("FLASK_ENV")

# aahho.configuration.configs[env]

def create_app():
    app = Flask(__name__)
    app.config.from_object(configs[env])
    register_extensions(app)
    register_blueprints(app)
    return app

def register_extensions(app):
    cors.init_app(app)
    pass

def register_blueprints(app):
    app.register_blueprint(
        api_v1_bp,
        url_prefix="{prefix}/v{version}".format(
            prefix=app.config["URL_PREFIX"], version=API_VERSION_V1
        ),
    )

application = create_app()

