import json
from flask import Blueprint, request, jsonify, make_response
from flask_jwt_extended import create_access_token, JWTManager
from models import User
from app import db, app

#, Question, Token, Response
jwt = JWTManager(app)
api = Blueprint('api', 'api', url_prefix='/api')

@api.route('/signup', methods=["POST"])
def sign_up():
    if request.method == 'POST':
        user_data = json.loads(request.data)
        new_user = User(username= user_data["username"], email= user_data["email"])
    try:
        new_user = User(username= user_data["username"], email= user_data["email"])
        new_user.set_password(user_data["password"])
        db.session.add(new_user)
        db.session.commit()
    except Exception as e:
        app.logger.error("Error occurred: {}".format(e) )
        app.logger.error("Rolling back transaction....")
        db.session.rollback()
        return "There was an issue with your request, please reformat and try again", 400
    
    access_token = create_access_token(identity=new_user.username)

    return jsonify(access_token=access_token), 201

@api.route('/login', methods=["POST"])
def login():
    if not request.is_json:
        return jsonify({"msg": "Missing JSON in request"}), 400

    username = request.json.get('username', None)
    password = request.json.get('password', None)
    if not username:
        return jsonify({"msg": "Missing username parameter"}), 400
    if not password:
        return jsonify({"msg": "Missing password parameter"}), 400

    user = User.query.filter_by(username=username).first()

    if not user or not user.check_password(password):
        return jsonify({"msg": "Bad username or password"}), 401

    # Identity can be any data that is json serializable
    access_token = create_access_token(identity=username)
    return jsonify(access_token=access_token), 200