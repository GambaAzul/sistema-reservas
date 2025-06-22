from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, field_validator
from datetime import datetime

app = FastAPI()

class Reserva(BaseModel):
    nombre: str
    fecha: str
    cancha: str
    extra: str | None = None

    @field_validator('fecha')
    @classmethod
    def fecha_valida(cls, v):
        try:
            datetime.strptime(v, '%Y-%m-%d')
        except:
            raise ValueError("Fecha inválida")
        return v

@app.post("/reservar")
async def reservar(reserva: Reserva):
    if not reserva.nombre:
        raise HTTPException(status_code=422, detail="Nombre vacío")
    
    canchas_validas = ["Cancha 1", "Cancha 2", "Cancha 3", "Cancha 4", "Cancha 5"]
    if reserva.cancha not in canchas_validas:
        raise HTTPException(status_code=400, detail="Solo hay 5 canchas disponibles.")
    
    fecha_reserva = datetime.strptime(reserva.fecha, '%Y-%m-%d')
    if fecha_reserva < datetime.now():
        raise HTTPException(status_code=400, detail="No se puede reservar fechas pasadas.")
    
    return {"mensaje": "Reserva registrada correctamente"}
