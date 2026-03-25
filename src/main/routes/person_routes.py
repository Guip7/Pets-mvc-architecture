from flask import Blueprint, jsonify, request
from ...view.hhtp_types.http_request import HttpRequest
from ..composer.person_creator_compose import person_creator_compose
from ..composer.person_finder_compose import person_finder_compose
from src.errors.error_handler import handle_errors


person_route_bp = Blueprint("person_routes", __name__)

@person_route_bp.route("/people", methods=["POST"])
def create_person():
    try:
        httpRequest = HttpRequest(body=request.json)
        view = person_creator_compose()
        http_response = view.handle(httpRequest)

        return jsonify(http_response.body), http_response.status_code
    except Exception as e:
        http_response = handle_errors(e)
        return jsonify(http_response.body), http_response.status_code

@person_route_bp.route("/people/<person_id>", methods=["GET"])
def find_person(person_id):
    try:
        httpRequest = HttpRequest(param={"person_id": person_id})
        view = person_finder_compose()

        http_response = view.handle(httpRequest)
        return jsonify(http_response.body), http_response.status_code
    except Exception as e:
        http_response = handle_errors(e)
        jsonify(http_response.body), http_response.status_code