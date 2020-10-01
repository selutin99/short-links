import short_url

from app.service.dao import create_empty_link, fill_empty_link, get_link, update_link_counter


def create_link_service(server_url, long_url):
    if get_link(long_url, is_long_url_filter=True):
        return get_link(long_url, is_long_url_filter=True)

    link = create_empty_link()

    short_postfix = short_url.encode_url(link.id, min_length=5)
    short_link = server_url + short_postfix

    link = fill_empty_link(link.id, long_url, short_link, short_postfix)

    return link


def get_link_service(short_postfix, is_statistics=False):
    link = get_link(short_postfix, is_long_url_filter=False)
    if not is_statistics and link:
        update_link_counter(link.id)
    return link
