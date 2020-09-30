from marshmallow import fields
from marshmallow.validate import URL, Length

from app import ma


# Input schemas
class CreateLinkSchema(ma.Schema):
    long_url = fields.Str(required=True, validate=URL(relative=False, require_tld=False))


class RedirectInputSchema(ma.Schema):
    short_postfix = fields.Str(required=True, validate=Length(equal=6))


# Output schemas
class CreateLinkResponseSchema(ma.Schema):
    class Meta:
        fields = ("short_link",)


create_link_schema = CreateLinkSchema()
redirect_link_schema = RedirectInputSchema()

create_link_output_schema = CreateLinkResponseSchema()
