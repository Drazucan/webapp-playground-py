from fastapi.testclient import TestClient
from playapp.main import app


client = TestClient(app)


def test_get_all_users():
    response = client.get("/v1alpha1/users/")
    assert response.status_code == 200
    # assert response.json() == {"message": "Hello World"}
