from app.schemas import create_link_schema, create_link_output_schema
import status
from flask import request, abort, make_response, jsonify

from app import app
from app.service.logic import shorten_url_service


@app.route('/long_to_short', methods=['POST'])
def shorten_link():
    errors = create_link_schema.validate(request.json)
    if errors:
        abort(make_response(jsonify(errors), status.HTTP_400_BAD_REQUEST))

    link = shorten_url_service(request.url_root, request.json.get('long_url'))
    return create_link_output_schema.dump(link)
