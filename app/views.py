import status
from flask import request, redirect

from app import app
from app.schemas import create_link_output_schema, create_link_schema, redirect_link_schema
from app.service.logic import create_short_link, get_original_link
from app.service.utils import validate_request


@app.route('/long_to_short', methods=['POST'])
def shorten_link():
    validate_request(request, create_link_schema, status.HTTP_400_BAD_REQUEST)
    link = create_short_link(request.url_root, request.json.get('long_url'))
    return create_link_output_schema.dump(link)


@app.route('/<string:short_postfix>')
def redirect_link(short_postfix):
    validate_request(request, redirect_link_schema, status.HTTP_400_BAD_REQUEST)
    link = get_original_link(short_postfix)
    return redirect(link.long_url, code=status.HTTP_302_FOUND)
