from flask import Flask, jsonify, request
from flask_cors import CORS
from config import DevelopmentConfig 

DEBUG=True

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
CORS(app)

@app.route("/")
def home():
    response_object = {"msg":"Hello World!!!"}
    return jsonify(response_object)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
