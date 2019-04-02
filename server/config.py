import os
class Config(object):
    print(os.environ['DB_CONN_STRING'])
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'this-really-needs-to-be-changed'
    JWT_SECRET_KEY = 'this-also-really-needs-to-be-changed'
    SQLALCHEMY_DATABASE_URI = os.environ['DB_CONN_STRING']
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_ACCESS_TOKEN_EXPIRES = False

class ProductionConfig(Config):
    DEBUG = False

class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True

class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True

class TestingConfig(Config):
    TESTING = True