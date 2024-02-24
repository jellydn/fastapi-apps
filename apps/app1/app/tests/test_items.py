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
def test_create_item_with_invalid_data():
    response = client.post("/items", json={"name": "Invalid Item", "price": "abc"})
    assert response.status_code == 422
    assert response.json() == {"detail": [{"loc": ["body", "price"], "msg": "value is not a valid float", "type": "type_error.float"}]}

def test_create_item_with_missing_data():
    response = client.post("/items", json={"name": "Missing Price"})
    assert response.status_code == 422
    assert response.json() == {"detail": [{"loc": ["body", "price"], "msg": "field required", "type": "value_error.missing"}]}

def test_get_items_empty_list():
    response = client.get("/items")
    assert response.status_code == 200
    assert response.json() == []

def test_get_items_with_items():
    response = client.post("/items", json={"name": "Item 1", "price": 10.0})
    assert response.status_code == 200
    response = client.post("/items", json={"name": "Item 2", "price": 20.0})
    assert response.status_code == 200

    response = client.get("/items")
    assert response.status_code == 200
    assert response.json() == [
        {"name": "Item 1", "price": 10.0},
        {"name": "Item 2", "price": 20.0},
    ]
def test_create_item_with_invalid_data():
    response = client.post("/items", json={"name": "Invalid Item", "price": "abc"})
    assert response.status_code == 422
    assert response.json() == {"detail": [{"loc": ["body", "price"], "msg": "value is not a valid float", "type": "type_error.float"}]}

def test_create_item_with_missing_data():
    response = client.post("/items", json={"name": "Missing Price"})
    assert response.status_code == 422
    assert response.json() == {"detail": [{"loc": ["body", "price"], "msg": "field required", "type": "value_error.missing"}]}

def test_get_items_empty_list():
    response = client.get("/items")
    assert response.status_code == 200
    assert response.json() == []

def test_get_items_with_items():
    response = client.post("/items", json={"name": "Item 1", "price": 10.0})
    assert response.status_code == 200
    response = client.post("/items", json={"name": "Item 2", "price": 20.0})
    assert response.status_code == 200

    response = client.get("/items")
    assert response.status_code == 200
    assert response.json() == [
        {"name": "Item 1", "price": 10.0},
        {"name": "Item 2", "price": 20.0},
    ]
