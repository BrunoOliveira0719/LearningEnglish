from flask import Blueprint, request, jsonify

# Import Adapters
from basic_english.src.main.adapters.request_adapter import request_adapter

# Import Composers (Phrase)
from basic_english.src.main.composer.phrase_finder_composer import phrase_finder_composer
from basic_english.src.main.composer.phrase_insert_composer import phrase_insert_composer
from basic_english.src.main.composer.phrase_finder_all_composer import phrase_finder_all_composer
from basic_english.src.main.composer.phrase_finder_all_type_phrase_composer import finder_all_type_phrase_composer
from basic_english.src.main.composer.phrase_update_composer import phrase_update_composer
from basic_english.src.main.composer.phrase_delete_composer import phrase_delete_composer

# Import Composers (Word)
from basic_english.src.main.composer.word_finder_composer import word_finder_composer
from basic_english.src.main.composer.word_insert_composer import word_insert_composer
from basic_english.src.main.composer.word_finder_all_composer import word_finder_all_composer
from basic_english.src.main.composer.word_finder_all_type_phrase_composer import finder_all_type_word_composer
from basic_english.src.main.composer.word_update_composer import word_update_composer
from basic_english.src.main.composer.word_delete_composer import word_delete_composer

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

word_route_bp = Blueprint('word_route', __name__)
    
@word_route_bp.route('/word', methods=['POST'])
def word_insert():
    http_response = None

    try:
        http_response = request_adapter(request, word_insert_composer())

    except Exception as exception:
        http_response = handle_errors(exception)

    return jsonify(http_response.body), http_response.status_code

@word_route_bp.route('/word/find', methods=['GET'])
def word_find():
    http_response = None

    try:
        http_response = request_adapter(request, word_finder_composer())
        
    except Exception as exception:
        http_response = handle_errors(exception)

    return jsonify(http_response.body), http_response.status_code

@word_route_bp.route('/word/find_all', methods=['GET'])
def word_find_all():
    http_response = None

    try:
        http_response = request_adapter(request, word_finder_all_composer())
    
    except Exception as exception:
        http_response = handle_errors(exception)

    print()
    print(http_response)
    print(jsonify(str(http_response.body)), http_response.status_code)

    return jsonify(http_response.body), http_response.status_code

@word_route_bp.route('/word/find_all_type_word', methods=['GET'])
def word_finder_all_type_word_composer():
    http_response = None

    try:
        http_response = request_adapter(request, finder_all_type_word_composer())

    except Exception as exception:
        http_response = handle_errors(exception)

    print()
    print(http_response)
    print(jsonify(http_response.body), http_response.status_code)

    return jsonify(http_response.body), http_response.status_code
    
@word_route_bp.route('/word/update', methods=['PUT'])
def word_uodate():
    http_response = None

    try:
        http_response = request_adapter(request, word_update_composer())
        
    except Exception as exception:
        http_response = handle_errors(exception)

    return jsonify(http_response.body), http_response.status_code

@word_route_bp.route('/word/delete', methods=['DELETE'])
def word_delete():
    http_response = None

    try:
        http_response = request_adapter(request, word_delete_composer())

    except Exception as exception:
        http_response = handle_errors(exception)

    return jsonify(http_response.body), http_response.status_code