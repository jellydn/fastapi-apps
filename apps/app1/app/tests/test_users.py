from fastapi.testclient import TestClient

from ..main import app

client = TestClient(app)


def test_create_user():
    response = client.post("/users")
    assert response.status_code == 200
    assert response.json() == {"message": "User received"}


def test_create_user_with_invalid_data():
    response = client.post("/users", json={"username": "Invalid User", "email": "invalid_email"})
    assert response.status_code == 422
    assert response.json() == {"detail": [{"loc": ["body", "email"], "msg": "value is not a valid email address", "type": "value_error.email"}]}


def test_create_user_with_missing_data():
    response = client.post("/users", json={"username": "Missing Email"})
    assert response.status_code == 422
    assert response.json() == {"detail": [{"loc": ["body", "email"], "msg": "field required", "type": "value_error.missing"}]}
