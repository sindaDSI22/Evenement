from flask import jsonify, Flask, request
from flask_cors import cross_origin, CORS

from base import Session
from . import app
from .models import Evenement

@app.route("/get_event", methods=["GET"])
def get_event():
    data = Evenement().get()
    return jsonify(data)

@app.route("/get_event_id/<id>", methods=["GET"])
def get_event_id(id):
    data = Evenement(id=id).getbyid()
    return jsonify(data)


@app.route("/suppEvent/<id>", methods=["DELETE"])
def suppEvent(id):
    event = Session.query(Evenement).filter(Evenement.id == id).first()
    if event:
        Session.delete(event)
        Session.commit()
        return jsonify({"error": False, "msg": "suppression evenement avec succées"}), 200
    else:
        return jsonify({"error": True, "msg": "suppression evenement impossible"}), 406


@app.route("/addEvent", methods=["POST"])
def addEvent():
    req = request.get_json()
    try:
        event = Evenement(**req)
        Session.add(event)
        Session.commit()
        return jsonify({"error": False, "msg": "ajout evenement avec succées"}), 200
    except Exception as e:
        return jsonify({"error": True, "msg": str(e)}), 406

@app.route("/updateEvent/<idE>", methods=["POST"])
def updateEvent(idE):
    req = request.get_json()
    evt = Evenement(**req).updateEvent(idE)
    if evt:
        return jsonify({"error": False, "msg": "modification  avec succées", "data": evt}), 200
    return jsonify({"error": True, "msg": "Une erreur se produit lors de la modification"}), 406

