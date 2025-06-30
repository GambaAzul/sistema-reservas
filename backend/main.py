from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel, field_validator
from datetime import datetime
import logging
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI()

# Configurar logging
logger = logging.getLogger("backend_logger")
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler("logs/backend.log")
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

# Instrumentación Prometheus
instrumentator = Instrumentator()
instrumentator.instrument(app).expose(app)

class Reserva(BaseModel):
    nombre: str
    fecha: str
    cancha: str
    extra: str | None = None

    @field_validator('fecha')
    def fecha_valida(cls, v):
        try:
            datetime.strptime(v, "%Y-%m-%d")
        except:
            raise ValueError("Fecha inválida")
        return v

@app.post("/reservar")
async def reservar(reserva: Reserva, request: Request):
    if not reserva.nombre:
        logger.warning("Intento de reserva con nombre vacío")
        raise HTTPException(status_code=422, detail="Nombre vacío")

    canchas_validas = ["Cancha 1", "Cancha 2", "Cancha 3", "Cancha 4", "Cancha 5"]
    if reserva.cancha not in canchas_validas:
        logger.warning(f"Intento de reserva en cancha inválida: {reserva.cancha}")
        raise HTTPException(status_code=400, detail="Solo hay 5 canchas disponibles.")

    fecha_reserva = datetime.strptime(reserva.fecha, "%Y-%m-%d")
    if fecha_reserva < datetime.now():
        logger.warning(f"Intento de reserva en fecha pasada: {reserva.fecha}")
        raise HTTPException(status_code=400, detail="No se puede reservar fechas pasadas.")

    logger.info(f"Reserva registrada: {reserva.nombre}, {reserva.fecha}, {reserva.cancha}")
    return {"mensaje": "Reserva registrada correctamente"}
