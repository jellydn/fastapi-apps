from fastapi.testclient import TestClient
from fastapi_app_demo.main import app

client = TestClient(app)


def test_add_process_time_header():
    # Test the behavior of the add_process_time_header middleware function
    response = client.get("/")
    assert response.status_code == 200
    assert "X-Process-Time" in response.headers

    # Add additional test cases here to cover different scenarios and edge cases
    # Test different types of requests
    response = client.post("/")
    assert response.status_code == 200
    assert "X-Process-Time" in response.headers

    response = client.put("/")
    assert response.status_code == 200
    assert "X-Process-Time" in response.headers

    response = client.delete("/")
    assert response.status_code == 200
    assert "X-Process-Time" in response.headers

    # Test different headers in the request
    headers = {"Authorization": "Bearer token"}
    response = client.get("/", headers=headers)
    assert response.status_code == 200
    assert "X-Process-Time" in response.headers

    # Test different values for the call_next parameter
    async def mock_call_next(request):
        return {"message": "Mock response"}

    response = await app.add_process_time_header(None, mock_call_next)
    assert response == {"message": "Mock response"}
    assert "X-Process-Time" in response.headers
