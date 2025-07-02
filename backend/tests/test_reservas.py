from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)

def test_registrar_reserva_correcta():
    response = client.post("/reservas", json={
        # datos ejemplo
        "fecha": "2025-12-01",
        "hora": "10:00",
        "cancha": 1,
        "usuario": "usuario1"
    })
    # Bandit detecta assert, pero aquí es test, es aceptable
    # Agregamos # nosec para ignorar
    assert response.status_code == 200  # nosec
    assert response.json() == {"mensaje": "Reserva registrada correctamente"}  # nosec

def test_reservar_fecha_pasada():
    response = client.post("/reservas", json={
        "fecha": "2020-01-01",
        "hora": "10:00",
        "cancha": 1,
        "usuario": "usuario1"
    })
    assert response.status_code == 400  # nosec
    assert response.json()["detail"] == "No se puede reservar fechas pasadas."  # nosec

def test_limite_canchas_disponibles():
    response = client.post("/reservas", json={
        "fecha": "2025-12-01",
        "hora": "10:00",
        "cancha": 10,
        "usuario": "usuario1"
    })
    assert response.status_code == 400  # nosec
    assert response.json()["detail"] == "Solo hay 5 canchas disponibles."  # nosec

def test_reserva_ignorar_campos_extra():
    response = client.post("/reservas", json={
        "fecha": "2025-12-01",
        "hora": "10:00",
        "cancha": 1,
        "usuario": "usuario1",
        "campo_extra": "ignorado"
    })
    assert response.status_code == 200  # nosec
    assert response.json() == {"mensaje": "Reserva registrada correctamente"}  # nosec

def test_reserva_campos_invalidos():
    response = client.post("/reservas", json={
        "fecha": "fecha_invalida",
        "hora": "hora_invalida",
        "cancha": "no_numero",
        "usuario": 123
    })
    assert response.status_code == 422  # nosec

def test_reserva_faltan_campos():
    response = client.post("/reservas", json={
        "fecha": "2025-12-01",
        # falta hora
        "cancha": 1,
        "usuario": "usuario1"
    })
    assert response.status_code == 422  # nosec
