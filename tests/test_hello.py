from fastapi.testclient import TestClient
from playapp.main import app


client = TestClient(app)


def test_hello():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}