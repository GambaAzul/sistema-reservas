from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from datetime import datetime
import mysql.connector
from loguru import logger

app = FastAPI()

# Configuración del logger para guardar en archivo con rotación y retención
logger.add("logs/backend.log", rotation="10 MB", retention="7 days", level="INFO", encoding="utf-8")

class Reserva(BaseModel):
    nombre: str
    fecha: str
    cancha: int

@app.post("/reservar")
def reservar(reserva: Reserva):
    hoy = datetime.now().date()
    fecha_reserva = datetime.strptime(reserva.fecha, "%Y-%m-%d").date()

    if fecha_reserva < hoy:
        logger.warning(f"Intento de reserva en fecha pasada: {reserva.fecha}")
        raise HTTPException(status_code=400, detail="No se puede reservar fechas pasadas.")

    if reserva.cancha < 1 or reserva.cancha > 5:
        logger.warning(f"Intento de reserva con cancha inválida: {reserva.cancha}")
        raise HTTPException(status_code=400, detail="Solo hay 5 canchas disponibles.")

    try:
        conexion = mysql.connector.connect(
            host="db",
            user="reservas_user",
            password="reservas_pass",
            database="reservas"
        )
        cursor = conexion.cursor()
        cursor.execute(
            "INSERT INTO reservas (nombre, fecha, cancha) VALUES (%s, %s, %s)",
            (reserva.nombre, reserva.fecha, reserva.cancha)
        )
        conexion.commit()
        cursor.close()
        conexion.close()

        logger.info(f"Reserva registrada: {reserva.nombre} - {reserva.fecha} - Cancha {reserva.cancha}")
    except Exception as e:
        logger.error(f"Error al registrar reserva: {e}")
        raise HTTPException(status_code=500, detail=str(e))

    return {"mensaje": "Reserva registrada correctamente"}
