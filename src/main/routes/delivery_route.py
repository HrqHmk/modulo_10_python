from flask import Blueprint, jsonify, request
from src.main.http_types.http_request import HttpRequest
from src.main.http_types.http_response import HttpResponse

delivery_routes_bp = Blueprint("delivery_routes", __name__)

@delivery_routes_bp.route("/health", methods=["GET"])
def health():
    return jsonify({ "hello" : "mundo"}), 200


@delivery_routes_bp.route("/delivery/order", methods=["POST"])
def registry_order():
    http_request = HttpRequest()
    return jsonify({ "hello" : "mundo"}), 200
