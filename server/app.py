import os
import logging
from flask import Flask, jsonify, request
from flask_cors import CORS
from config import DevelopmentConfig, ProductionConfig, StagingConfig, TestingConfig
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import (
    JWTManager, jwt_optional, create_access_token,
    get_jwt_identity
)

env = os.environ["ENVIRONMENT"]

if env == "DEV":
    config = DevelopmentConfig
elif env == "STAGING":
    config = StagingConfig
elif env == "TEST":
    config = TestingConfig
elif env == "PROD":
    config = ProductionConfig
else:
    raise Exception("No environment (DEV, STAGING, TEST, PROD) is set through ENV. Unable to set Configuration.")

logging.getLogger('flask_cors').level = logging.DEBUG

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
db = SQLAlchemy(app)
CORS(app)

from controllers import api, api_blueprints
app.register_blueprint(api)

for blueprint in api_blueprints:
    app.register_blueprint(blueprint) 

if __name__ == '__main__':
    app.run(host='0.0.0.0')
