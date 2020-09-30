from app import ma


class LinkSchema(ma.Schema):
    class Meta:
        fields = ("long_url", "short_link", "short_postfix", "counter")


link_schema = LinkSchema()
