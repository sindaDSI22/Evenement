from flask import jsonify, Flask, request
from flask_cors import cross_origin, CORS

from base import Session
from . import app
from .model import User

@app.route("/get_user/<login>", methods=["GET"])
def get_user(login):

    data = User(login=login).get()
    return jsonify(data)

@app.route("/login", methods=["POST"])
def login():
    req = request.get_json()
    user = User(**req)
    # import pdb;pdb.set_trace()
    try:
        res = user.checkLogin()
        if res:
            return jsonify({"error": False,"msg": "connexion avec succée"}), 200
        else:
            return jsonify({"error": True,"msg": "impossible de se connecter"}), 406
    except:
        return jsonify({"error": True}), 406