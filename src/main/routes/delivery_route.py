from flask import Blueprint, jsonify, request

delivery_routes_bp = Blueprint("delivery_routes", __name__)

@delivery_routes_bp.route("/health", methods=["GET"])
def health():
    return jsonify({ "hello" : "mundo"}), 200


@delivery_routes_bp.route("/delivery/order", methods=["POST"])
def registry_order():
    print(request.json)
    return jsonify({ "hello" : "mundo"}), 200
