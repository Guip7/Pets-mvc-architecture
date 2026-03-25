from flask import Blueprint, jsonify, request
from ...view.hhtp_types.http_request import HttpRequest
from ..composer.pet_finder_compose import pet_finder_compose
from ..composer.pet_deleter_compose import pet_deleter_compose
from src.errors.error_handler import handle_errors

pet_route_bp = Blueprint("pets_routes", __name__)

@pet_route_bp.route("/pets", methods=["GET"])
def list_pets():
    try:
        httpRequest = HttpRequest()
        view = pet_finder_compose()
        http_response = view.handle(httpRequest)

        return jsonify(http_response.body), http_response.status_code
    except Exception as e:
        http_response = handle_errors(e)
        return jsonify(http_response.body), http_response.status_code

@pet_route_bp.route("/pets/<pet_name>", methods=["DELETE"])
def delete_pet(pet_name):
    try:
        httpRequest = HttpRequest(param={"name": pet_name})
        view = pet_deleter_compose()

        http_response = view.handle(httpRequest)
        return jsonify(http_response.body), http_response.status_code
    except Exception as e:
        http_response = handle_errors(e)
        return jsonify(http_response.body), http_response.status_code