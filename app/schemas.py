from app import ma
from app.models import Link


class LinkSchema(ma.Schema):
    class Meta:
        model = Link


link_schema = LinkSchema()
