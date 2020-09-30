from app.schemas import link_schema

from flask import request

from app import app
from app.service.logic import shorten_url_service


@app.route('/long_to_short', methods=['POST'])
def shorten_link():
    link = shorten_url_service(request.url_root, request.json.get('long_url'))
    return link_schema.dump(link)
