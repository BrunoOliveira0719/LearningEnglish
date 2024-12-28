from flask import Blueprint, request, jsonify

# Import Adapters
from basic_english.src.main.adapters.request_adapter import request_adapter

# Import Composers
from basic_english.src.main.composer.phrase_finder_composer import phrase_finder_composer
from basic_english.src.main.composer.phrase_insert_composer import phrase_insert_composer
from basic_english.src.main.composer.phrase_finder_all_composer import phrase_finder_all_composer
from basic_english.src.main.composer.phrase_finder_all_type_phrase_composer import finder_all_type_phrase_composer
from basic_english.src.main.composer.phrase_update_composer import phrase_update_composer
from basic_english.src.main.composer.phrase_delete_composer import phrase_delete_composer

from basic_english.src.errors.error_handler import handle_errors

phrase_route_bp = Blueprint('phrase_route', __name__)
    
@phrase_route_bp.route('/phrase', methods=['POST'])
def phrase_insert():
    http_response = None

    try:
        http_response = request_adapter(request, phrase_insert_composer())

    except Exception as exception:
        http_response = handle_errors(exception)

    return jsonify(http_response.body), http_response.status_code

@phrase_route_bp.route('/phrase/find', methods=['GET'])
def phrase_find():
    http_response = None

    try:
        http_response = request_adapter(request, phrase_finder_composer())

    except Exception as exception:
        http_response = handle_errors(exception)

    return jsonify(http_response.body), http_response.status_code

@phrase_route_bp.route('/phrase/find_all', methods=['GET'])
def phrase_find_all():
    http_response = None

    try:
        http_response = request_adapter(request, phrase_finder_all_composer())
    
    except Exception as exception:
        http_response = handle_errors(exception)

    return jsonify(http_response.body), http_response.status_code

@phrase_route_bp.route('/phrase/find_all_type_phrase', methods=['GET'])
def phrase_finder_all_type_phrase_composer():
    http_response = None

    try:
        http_response = request_adapter(request, finder_all_type_phrase_composer())

    except Exception as exception:
        http_response = handle_errors(exception)

    return jsonify(http_response.body), http_response.status_code
    
@phrase_route_bp.route('/phrase/update', methods=['PUT'])
def phrase_uodate():
    http_response = None

    try:
        http_response = request_adapter(request, phrase_update_composer())
        
    except Exception as exception:
        http_response = handle_errors(exception)

    return jsonify(http_response.body), http_response.status_code

@phrase_route_bp.route('/phrase/delete', methods=['DELETE'])
def phrase_delete():
    http_response = None

    try:
        http_response = request_adapter(request, phrase_delete_composer())

    except Exception as exception:
        http_response = handle_errors(exception)

    return jsonify(http_response.body), http_response.status_code