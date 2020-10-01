from marshmallow import fields
from marshmallow.validate import URL, Length

from app import ma


# Serialization schemas
class CreateLinkRequestSchema(ma.Schema):
    long_url = fields.Str(required=True, validate=URL(relative=False, require_tld=False))


class GetLinkRequestSchema(ma.Schema):
    short_postfix = fields.Str(validate=Length(equal=5))


# Deserialization schemas
class CreateLinkResponseSchema(ma.Schema):
    class Meta:
        fields = ("short_link",)


class GetLinkResponseSchema(ma.Schema):
    long_url = fields.Str(required=True, validate=URL(relative=False, require_tld=False))


create_link_request_schema = CreateLinkRequestSchema()
get_link_request_schema = GetLinkRequestSchema()

create_link_response_schema = CreateLinkResponseSchema()
get_link_response_schema = GetLinkResponseSchema()
