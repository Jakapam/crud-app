from flask import Flask, jsonify, request
from flask_cors import CORS

DEBUG=True

app = Flask(__name__)
app.config.from_object(__name__)

CORS(app)

@app.route("/")
def home():
    response_object = {"msg":"Hello World!!!"}
    return jsonify(response_object)


if __name__ == '__main__':
    app.run()
