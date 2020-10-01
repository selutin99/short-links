from flask import abort, make_response, jsonify
from marshmallow import ValidationError


def validate_request(request_part, schema, status, validate_schema=True):
    if validate_schema:
        errors = schema.validate(request_part)
    else:
        errors = schema

    if errors:
        abort(make_response(jsonify(errors=errors), status))


def preformat_request(load_dict, schema):
    try:
        schema.load(load_dict),
    except ValidationError as e:
        return e.messages
