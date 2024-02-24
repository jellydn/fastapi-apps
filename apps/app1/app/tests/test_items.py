from fastapi.testclient import TestClient

from ..main import app

client = TestClient(app)


def test_create_item():
    response = client.post("/items")
    assert response.status_code == 200
    assert response.json() == {"message": "Item received"}


def test_get_items():
    response = client.get("/items")
    assert response.status_code == 200
    assert response.json() == [
        {"name": "Plumbus", "price": 3},
        {"name": "Portal Gun", "price": 9001},
    ]
