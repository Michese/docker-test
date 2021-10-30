from flask import Flask, request, redirect, url_for, render_template, jsonify
from flask_cors import CORS

app = Flask(__name__, template_folder="app")
CORS(app, resources={r"/api/*": {"origins": "*"}})


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


# @app.errorhandler(404)
# def not_found(fasef):
#     return redirect('/')
#
#
# @app.errorhandler(500)
# def server_error():
#     """Internal server error."""
#     return render_template("index.html")


@app.route('/hello', methods=['POST'])
def indexPost():
    return "Hello, world!"


if __name__ == '__main__':
    app.debug = True
    app.run()
