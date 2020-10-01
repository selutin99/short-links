from flask_swagger_ui import get_swaggerui_blueprint

from app import app

SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
SWAGGER_UI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "short-links"
    }
)
app.register_blueprint(SWAGGER_UI_BLUEPRINT, url_prefix=SWAGGER_URL)
