from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)

def test_reserva_exitosa():
    response = client.post("/reservar", json={
        "nombre": "Test Usuario",
        "fecha": "2025-07-01",
        "cancha": "Cancha 1"
    })
    assert response.status_code == 200
    assert response.json() == {"mensaje": "Reserva registrada correctamente"}

def test_reserva_fecha_pasada():
    response = client.post("/reservar", json={
        "nombre": "Test Usuario",
        "fecha": "2020-01-01",
        "cancha": "Cancha 1"
    })
    assert response.status_code == 400
    assert response.json()["detail"] == "No se puede reservar fechas pasadas."

def test_reserva_cancha_no_valida():
    response = client.post("/reservar", json={
        "nombre": "Test Usuario",
        "fecha": "2025-07-01",
        "cancha": "Cancha X"
    })
    assert response.status_code == 400
    assert response.json()["detail"] == "Solo hay 5 canchas disponibles."

def test_reserva_campo_extra():
    response = client.post("/reservar", json={
        "nombre": "Test Usuario",
        "fecha": "2025-07-01",
        "cancha": "Cancha 1",
        "extra": "dato innecesario"
    })
    # Debe ignorar campos extra y registrar bien
    assert response.status_code == 200
    assert response.json() == {"mensaje": "Reserva registrada correctamente"}

def test_reserva_fecha_invalida():
    response = client.post("/reservar", json={
        "nombre": "Test Usuario",
        "fecha": "fecha-invalida",
        "cancha": "Cancha 1"
    })
    assert response.status_code == 422

def test_reserva_nombre_vacio():
    response = client.post("/reservar", json={
        "nombre": "",
        "fecha": "2025-07-01",
        "cancha": "Cancha 1"
    })
    assert response.status_code == 422
