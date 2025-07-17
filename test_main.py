from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_launch_valid():
    response = client.post("/launches/", json={"vehicle": "Falcon 9", "date": "2025-07-18T12:00:00", "status": "Scheduled"})
    assert response.status_code == 200
    data = response.json()
    assert data["vehicle"] == "Falcon 9"
    assert "id" in data

def test_create_launch_invalid_status():
    response = client.post("/launches/", json={"vehicle": "Falcon 9", "date": "2025-07-18T12:00:00", "status": "Invalid"})
    assert response.status_code == 400
    assert response.json()["detail"] == "Invalid status. Must be 'Scheduled', 'Launched', or 'Failed'."

def test_get_all_launches():
    response = client.get("/launches/")
    assert response.status_code == 200
    assert isinstance(response.json(), list) 