import status

from app import db
from app.models import Link

long_url = 'https://tproger.ru/translations/guide-into-python-imports/'


def test_create_link_route_valid_case(client):
    mock_request_data = {'long_url': long_url}
    response = client.post('/long_to_short', json=mock_request_data)
    assert response.status_code == status.HTTP_200_OK


def test_create_link_route_invalid_case(client):
    mock_request_data = {'long_url': 'test'}
    response = client.post('/long_to_short', json=mock_request_data)
    assert response.status_code == status.HTTP_400_BAD_REQUEST


def test_get_link_route_valid_case(client):
    link = db.session.query(Link).filter(Link.long_url == long_url).first()
    response = client.get('/' + link.short_postfix)
    assert response.status_code == status.HTTP_302_FOUND


def test_get_link_route_invalid_input_case(client):
    response = client.get('/q')
    assert response.status_code == status.HTTP_400_BAD_REQUEST


def test_get_link_route_invalid_found_case(client):
    response = client.get('/dfgdf')
    assert response.status_code == status.HTTP_404_NOT_FOUND


def test_statistic_route(client):
    link = db.session.query(Link).filter(Link.long_url == long_url).first()
    response = client.get('/statistics/' + link.short_postfix)
    assert response.json == {"count": link.count}
