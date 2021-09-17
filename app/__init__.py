from flask import Flask
from app.exts import db, migrate

def create_app(config_object='config.Config'):
    app = Flask(__name__)
    app.config.from_object(config_object)
    register_extensions(app)
    register_blueprints(app)
    return app


def register_extensions(app):
    db.init_app(app)
    migrate.init_app(app, db)
    from app import models
    
    return


def register_blueprints(app):
    pass
