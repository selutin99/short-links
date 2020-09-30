import short_url

from app.service.dao import create_empty_link, fill_empty_link


def url_shorten_service(server_url, long_url):
    link = create_empty_link()

    short_postfix = short_url.encode_url(link.id)
    short_link = '{url}/{postfix}'.format(url=server_url, postfix=short_postfix)

    link = fill_empty_link(link.id, long_url, short_link, short_postfix)

    return link
