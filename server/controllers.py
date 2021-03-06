import json
from flask import Blueprint, request, after_this_request,jsonify, make_response
from flask_jwt_extended import create_access_token, JWTManager, jwt_required
from models import User, Question, Token, Modifier, Response
from app import db, app
from flask_restless import APIManager
from flask_cors import cross_origin

manager = APIManager(app, flask_sqlalchemy_db=db)
jwt = JWTManager(app)
api = Blueprint('api', 'api', url_prefix='/api')

@jwt_required
def auth_func(*args, **kwargs):
    pass

def allow_control_headers(**kw):
    @after_this_request
    def add_headers(response):
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Access-Control-Allow-Credentials'] = 'true'
        return response

def generate_api_blueprint(resource):
    include_methods, include_columns = None, None
    if resource is Token:
        include_methods = ['value']
        include_columns = ["id","name"]
    elif resource is User:
        include_columns = ["id","username","email","is_admin"]
    elif resource is Response:
        include_columns = ["id","question","answer"]

    return manager.create_api_blueprint(
        resource, 
        methods=['GET', 'POST', 'PUT', 'PATCH', 'DELETE'], 
        preprocessors= dict( 
            GET_SINGLE=[auth_func, allow_control_headers], 
            GET_MANY=[auth_func, allow_control_headers],
            POST=[auth_func, allow_control_headers],
            PATCH_SINGLE=[auth_func, allow_control_headers], 
            PATCH_MANY=[auth_func, allow_control_headers],
            DELETE_SINGLE=[auth_func, allow_control_headers], 
            DELETE_MANY=[auth_func, allow_control_headers]),
        include_methods = include_methods,
        include_columns = include_columns
        ) 

api_blueprints = [generate_api_blueprint(resource) for resource in [User, Question, Modifier, Response, Token]] 


@api.route('/sanity')
def sanity_check():
    return jsonify({"msg": "sanity_checked"})

@api.route('/signup', methods=["POST"])
@cross_origin()
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
@cross_origin()
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