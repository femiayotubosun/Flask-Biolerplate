from flask import Flask

def create_app(config_object='config.Config'):
    app = Flask(__name__)
    app.config.from_object(config_object)
    register_extensions(app)
    register_blueprints(app)
    return app


def register_extensions(app):
    pass


def register_blueprints(app):
    pass
