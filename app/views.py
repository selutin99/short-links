from app.schemas import link_schema

from flask import request

from app import app
from app.service.logic import url_shorten_service


@app.route('/long_to_short', methods=['POST'])
def shorten_link():
    link = url_shorten_service(request.url_root, request.json.get('long_url'))
    return link_schema.jsonify(link)
