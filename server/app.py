from flask import Flask, jsonify, request
from flask_cors import CORS
from config import DevelopmentConfig 

import logging


from flask_sqlalchemy import SQLAlchemy

from flask_jwt_extended import (
    JWTManager, jwt_optional, create_access_token,
    get_jwt_identity
)

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
