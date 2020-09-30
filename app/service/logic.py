import short_url

from app.service.dao import create_empty_link, fill_empty_link, get_link, update_link_counter


def create_short_link(server_url, long_url):
    if get_link(long_url, is_long_url_filter=True):
        return get_link(long_url, is_long_url_filter=True)

    link = create_empty_link()

    short_postfix = short_url.encode_url(link.id)
    short_link = server_url + short_postfix

    link = fill_empty_link(link.id, long_url, short_link, short_postfix)

    return link


def get_original_link(short_postfix):
    link = get_link(short_postfix, is_long_url_filter=False)
    if link:
        update_link_counter(link.id)
    return link
