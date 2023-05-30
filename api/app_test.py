import pytest
from app import app


@pytest.fixture
def client():
    app.config.update({'TESTING': True})
    with app.test_client() as client:
        yield client


def test_getcodes(client):
    resp = client.get('/getCodes')
    assert resp.status_code == 201
   
    
def test_getexchange(client):
    response = client.post("/getExchange", data={
        "amount": "100",
        "from": "EUR",
        "to": "USD",
    })
    assert response.status_code == 201
