# Author: Chirag Chamoli
# -*- coding: utf-8 -*-

from flask import request
import logging
import os
import yaml

from aahho.application import application as app
import aahho.framework.routes

with open('globals.yaml', 'r') as f:
    globals = yaml.load(f)

def server_shutdown(msg):
    raise RuntimeError(msg)

if __name__ == "__main__":
    with app.app_context():
        possible_envs = ['local','staging','prod']
        env = os.environ.get("FLASK_ENV")
        if env in possible_envs :
            pass
        else:
            # app.logger.error("Environment is set incorrectly!.")
            server_shutdown("Please configure environment properly!.")

        if env == 'local':
            context = (globals['local_certs']['crt'], globals['local_certs']['key'])
            app.run(host=app.config['HOST'], port=app.config['PORT'],ssl_context=context, use_reloader = True)
        else:
            #init_db(True)
            #app.logger.handlers.extend(gunicorn_error_logger.handlers)
            #app.logger.setLevel(logging.DEBUG)
            #app.run(host=app.config['HOST'], port=app.config['PORT'], threaded=app.config['IS_THREADED'])
            pass
