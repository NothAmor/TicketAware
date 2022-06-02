from flask import Flask
from flask_restplus import Api


def create_app():
    from candidates_backend.api_namespace import api_namespace
    from candidates_backend.admin_namespace import admin_namespace

    application = Flask(__name__)
    api = Api(application, version='0.1', title='Candidates Backend API',
              description='A Simple CRUD API')

    from candidates_backend.db import db, db_config
    application.config['RESTPLUS_MASK_SWAGGER'] = False
    application.config.update(db_config)
    db.init_app(application)
    application.db = db

    api.add_namespace(api_namespace)
    api.add_namespace(admin_namespace)

    return application
