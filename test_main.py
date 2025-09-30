from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello from CI/CD demo!"}

def test_greet():
    response = client.get("/hello/Amir")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, Amir!"}