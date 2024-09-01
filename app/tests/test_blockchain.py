from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_get_blocks():
    response = client.get("/blockchain/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_add_block():
    response = client.post("/blockchain/", json={"data": "Novo bloco"})
    assert response.status_code == 200
    assert response.json()["data"] == "Novo bloco"
