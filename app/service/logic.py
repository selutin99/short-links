import short_url

from app.service.dao import create_empty_link, fill_empty_link, link_exist


def shorten_url_service(server_url, long_url):
    if link_exist(long_url):
        return link_exist(long_url)

    link = create_empty_link()

    short_postfix = short_url.encode_url(link.id)
    short_link = server_url + short_postfix

    link = fill_empty_link(link.id, long_url, short_link, short_postfix)

    return link
