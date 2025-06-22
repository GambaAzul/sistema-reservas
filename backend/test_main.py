from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_reservar():
    response = client.post("/reservar", json={"nombre": "Test", "fecha": "2025-06-30", "cancha": 1})
    assert response.status_code == 200
    assert response.json() == {"mensaje": "Reserva registrada correctamente"}

