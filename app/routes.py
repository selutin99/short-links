import status
from flask import request, redirect, make_response, jsonify

from app import app
from app.schemas import create_link_request_schema, create_link_response_schema, get_link_response_schema,\
    get_link_statistics_schema, get_link_request_schema
from app.service.logic import create_link_service, get_link_service
from app.service.utils import validate_request, preformat_request


@app.route('/long_to_short', methods=['POST'])
def create_short_url():
    validate_request(request.json, create_link_request_schema, status.HTTP_400_BAD_REQUEST, validate_schema=True)
    link = create_link_service(request.url_root, request.json.get('long_url'))
    return create_link_response_schema.dump(link)


@app.route('/<string:short_postfix>')
def get_original_url(short_postfix):
    validate_request(
        request.path,
        preformat_request({"short_postfix": short_postfix}, get_link_request_schema),
        status.HTTP_400_BAD_REQUEST, validate_schema=False
    )
    link = get_link_response_schema.dump(get_link_service(short_postfix, is_statistics=False))

    if link:
        return redirect(link.get('long_url'), code=status.HTTP_302_FOUND)
    else:
        return make_response(jsonify(errors=['Link not found']), status.HTTP_404_NOT_FOUND)


@app.route('/statistics/<string:short_postfix>')
def get_url_statistics(short_postfix):
    validate_request(
        request.path,
        preformat_request({"short_postfix": short_postfix}, get_link_request_schema),
        status.HTTP_400_BAD_REQUEST, validate_schema=False
    )
    link = get_link_statistics_schema.dump(get_link_service(short_postfix, is_statistics=True))

    if link:
        return make_response(jsonify(link))
    else:
        return make_response(jsonify(errors=['Link not found']), status.HTTP_404_NOT_FOUND)
