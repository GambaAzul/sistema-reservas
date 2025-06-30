# Sistema de Reservas - Proyecto EC2

## Descripción

Este proyecto es un sistema de reservas para alquiler de canchas deportivas, desarrollado con FastAPI y desplegado en AWS EC2. Incluye:

- API REST para gestión de reservas.
- Validaciones y manejo de errores.
- Pruebas unitarias.
- Pipeline CI para análisis de vulnerabilidades y pruebas.
- Integración con herramientas de monitoreo y logging.

## Arquitectura

- Backend: FastAPI + Uvicorn.
- Base de datos: MySQL (configurada en AWS).
- Infraestructura: AWS EC2 con Docker.
- CI/CD: GitHub Actions con análisis de seguridad (Checkov, Bandit, Trivy) y pruebas unitarias.
- Monitoreo: (Pendiente de integración con Grafana o CloudWatch).

## Requisitos

- Python 3.9+
- Docker y Docker Compose
- AWS CLI configurado

## Instalación y Ejecución Local

```bash
# Clonar repositorio
git clone https://github.com/GambaAzul/sistema-reservas.git
cd sistema-reservas/backend

# Crear y activar entorno virtual
python3 -m venv venv
source venv/bin/activate

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar aplicación
uvicorn main:app --reload --host 0.0.0.0 --port 8000

