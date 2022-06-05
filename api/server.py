import flask
from flask import Flask, jsonify, request
from api.repository.Repository import Repository

# from network.test import Network

# initialize the REST API

# initialize neural network
# neural_net = Network()

# Markups locations
markups = "./templates/"
app = Flask(__name__)
repository = Repository()


@app.route("/", methods=["GET"])
def serve_index():
    if request.method == 'GET':
        data = "Hello world"
        return jsonify({
            'data': data
        })


@app.route("/login", methods=["GET", "POST"])
def serve_login_page():
    try:
        if request.method == 'GET':
            return flask.render_template('login.html')
        if request.method == 'POST':
            json_data = request.get_json()
            username = json_data['username']
            password = json_data['password']
            repository.is_user(username, password)
            return json_data

    except:
        print("Error Occurred")


if __name__ == '__main__':
    app.run()
