from fastapi import FastAPI
from pydantic import BaseModel
import mysql.connector
from loguru import logger
import time  # <--- Agregado para usar time.sleep()

app = FastAPI()

class Reserva(BaseModel):
    nombre: str
    fecha: str
    cancha: int

# Configuración de logging
logger.add("logs/backend.log", rotation="10 MB", retention="7 days", level="INFO", encoding="utf-8")

# Datos de conexión MySQL
config_db = {
    "host": "172.18.0.3",      # IP del contenedor MySQL (puede ser el nombre del servicio "db")
    "user": "reservas_user",   # Usuario correcto según docker-compose.yml
    "password": "reservas_pass", # Contraseña correcta según docker-compose.yml
    "database": "reservas"
}

@app.post("/reservar")
def reservar(reserva: Reserva):
    intentos = 5
    espera_segundos = 3

    for i in range(intentos):
        try:
            conexion = mysql.connector.connect(**config_db)
            cursor = conexion.cursor()
            sql = "INSERT INTO reservas (nombre, fecha, cancha) VALUES (%s, %s, %s)"
            valores = (reserva.nombre, reserva.fecha, reserva.cancha)
            cursor.execute(sql, valores)
            conexion.commit()
            cursor.close()
            conexion.close()
            logger.info(f"Reserva registrada: {reserva.nombre} - {reserva.fecha} - Cancha {reserva.cancha}")
            return {"mensaje": "Reserva registrada correctamente"}
        except mysql.connector.Error as err:
            logger.error(f"Error al registrar reserva: {err}")
            if i < intentos - 1:
                time.sleep(espera_segundos)  # Espera antes de reintentar
            else:
                return {"error": str(err)}
