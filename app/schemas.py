from marshmallow import fields
from marshmallow.validate import URL

from app import ma


# Input schemas
class CreateLinkSchema(ma.Schema):
    long_url = fields.Str(required=True, validate=URL(relative=False, require_tld=False))


# Output schemas
class CreateLinkResponseSchema(ma.Schema):
    class Meta:
        fields = ("short_link",)


create_link_schema = CreateLinkSchema()
create_link_output_schema = CreateLinkResponseSchema()
