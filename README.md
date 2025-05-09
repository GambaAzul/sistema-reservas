# Sistema de Reservas Deportivas – Arquitectura Serverless en AWS

Este proyecto implementa un sistema completo de reservas deportivas 100% online, utilizando arquitectura serverless con servicios de Amazon Web Services.

## Tecnologías Usadas

- **Frontend**: HTML + JavaScript (fetch) alojado en Amazon S3
- **Backend**: 5 funciones Lambda en Python
- **API Gateway**: Exposición de endpoints HTTP
- **DynamoDB**: Base de datos NoSQL para reservas
- **SNS**: Envío de correos de confirmación
- **Step Functions**: Automatización de flujos (opcional)
- **IAM**: Roles y permisos por función
- **Terraform**: Infraestructura como código

## Estructura

- `frontend/`: Contiene `index.html`
- `backend/`: 5 funciones Lambda
- `infra/`: Archivos Terraform (`main.tf`, `variables.tf`, `outputs.tf`)
- `docs/`: Presentación, informe y diagrama

## Funcionalidades

- Validación de fechas en frontend
- Creación, cancelación, modificación y consulta de reservas
- Correos automáticos de confirmación
- Seguridad con IAM Roles
- Flujo automatizado con Step Functions

## Arquitectura

(Agrega aquí tu diagrama final)

## Lo queremos mucho profesor xd.