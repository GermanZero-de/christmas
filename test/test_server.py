import pytest
import json

from christmas.server import app


def test_request_deputy_postcode_not_existent():
    data = 'postcode=12345'
    request, response = app.test_client.post('/', data=data)
    assert response.status == 204
    data = 'postcode=99999'
    request, response = app.test_client.post('/', data=data)
    assert response.status == 204
    assert response.text == ''

def test_request_deputy_postcode_existent():
    data = 'postcode=12589'
    request, response = app.test_client.post('/', data=data)
    assert response.status == 200
    assert response.json == {"first_name": "Gregor", "last_name": "Gysi", "degree": "Dr.", "picture_url": "https://www.abgeordnetenwatch.de/sites/abgeordnetenwatch.de/files/dr_gregor_gysi_13.jpg", "party": "DIE LINKE"}
    data = 'postcode=17489'
    request, response = app.test_client.post('/', data=data)
    assert response.status == 200
    assert response.json == {'degree': 'Dr.', 'first_name': 'Angela', 'last_name': 'Merkel', 'party': 'CDU', 'picture_url': 'https://www.abgeordnetenwatch.de/sites/abgeordnetenwatch.de/files/users/merkel_angela_chaperon_ci_110195_0.png'}
    data = 'postcode=01561'
    request, response = app.test_client.post('/', data=data)
    assert response.status == 200
    assert response.json == {'degree': 'Dr.', 'first_name': 'Thomas', 'last_name': 'de Maiziére', 'party': 'CDU', 'picture_url': 'https://www.abgeordnetenwatch.de/sites/abgeordnetenwatch.de/files/users/thomas_de_maiziere.jpg'}

def test_request_deputy_malformed():
    data = 'postcode=foobar'
    request, response = app.test_client.post('/', data=data)
    assert response.status == 204
    data = 'postcode=#$%^'
    request, response = app.test_client.post('/', data=data)
    assert response.status == 204
    data = 'postcode=sys.exit()'
    request, response = app.test_client.post('/', data=data)
    assert response.status == 204
