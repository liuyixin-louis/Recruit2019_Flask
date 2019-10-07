
from flask import Flask

def create_app(config):
    from . import models, routes,utility
    app = Flask(__name__,static_folder='static')
    app.config.from_object(config)
    models.init_app(app)
    routes.init_app(app)
    utility.init_tool(app)
    return app