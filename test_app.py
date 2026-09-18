import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_index_page(client):
    response = client.get('/')
    assert response.status_code == 200

def test_api_data(client):
    response = client.get('/api')
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, list)
    assert data[0]['name'] == 'Aakash'

def test_submit_missing_fields(client):
    response = client.post('/submit', data={'name': '', 'email': '', 'message': ''})
    assert response.status_code == 400
