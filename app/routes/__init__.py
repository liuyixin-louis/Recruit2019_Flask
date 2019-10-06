from .frontend import frontend_blueprint
from .myapi import api_blueprint
# ...

def init_app(app):
    # app.register_blueprint(frontend_blueprint)
    # app.register_blueprint(api_blueprint)
    app.register_blueprint(frontend_blueprint)
    app.register_blueprint(api_blueprint, url_prefix='/api')

# ...