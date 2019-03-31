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

from controllers import api
app.register_blueprint(api)


@app.route('/login', methods=['POST'])
def login():
    if not request.is_json:
        return jsonify({"msg": "Missing JSON in request"}), 400

    username = request.json.get('username', None)
    password = request.json.get('password', None)
    if not username:
        return jsonify({"msg": "Missing username parameter"}), 400
    if not password:
        return jsonify({"msg": "Missing password parameter"}), 400

    if username != 'test' or password != 'test':
        return jsonify({"msg": "Bad username or password"}), 401

    # Identity can be any data that is json serializable
    access_token = create_access_token(identity=username)
    return jsonify(access_token=access_token), 200

@app.route("/")
def home():
    response_object = {"msg":"Hello World!!!"}
    return jsonify(response_object)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
