from flask import Blueprint, request, jsonify
#import adapters
from src.main.adapters.request_adapter import request_adapter
#import composers
from src.main.composers.users_finder_composer import user_finder_composer
from src.main.composers.users_register_composer import user_register_composer
#import error handler
from src.errors.error_handler import handle_errors


user_route_bp = Blueprint("user_routes", __name__)

@user_route_bp.route("/user/find", methods=["GET"])
def find_user():
    http_response = None
    try:
        http_response = request_adapter(request, user_finder_composer())
    except Exception as e:
        http_response = handle_errors(e)

    return jsonify(http_response.body), http_response.status_code

@user_route_bp.route("/user", methods=["POST"])
def register_user():
    http_response = None
    try:
        http_response = request_adapter(request, user_register_composer())
    except Exception as e:
        http_response = handle_errors(e)

    return jsonify(http_response.body), http_response.status_code
