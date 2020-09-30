from flask import abort, make_response, jsonify, request


def validate_request(request, schema, status):
    errors = schema.validate(request.json)
    if errors:
        abort(make_response(jsonify(errors), status))
