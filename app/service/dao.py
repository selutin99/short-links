from app import db
from app.models import Link


def create_empty_link():
    link = Link()

    db.session.add(link)
    db.session.commit()

    return link


def fill_empty_link(id, long_url, short_url, short_postfix):
    link = Link.query.get(id)

    link.long_url = long_url
    link.short_link = short_url
    link.short_postfix = short_postfix

    db.session.add(link)
    db.session.commit()

    return link


def get_link(predicate, is_long_url_filter=True):
    return db.session.query(Link).filter(
        Link.long_url == predicate if is_long_url_filter else Link.short_postfix == predicate
    ).first()


def update_link_counter(id):
    link = Link.query.get(id)
    link.count = link.count + 1

    db.session.add(link)
    db.session.commit()

    return link
