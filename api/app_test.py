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
   
    

