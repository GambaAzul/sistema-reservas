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

## Integraciones en el Proyecto

- IAM Role con Lambda (Policy and Role) Se creó un IAM Role personalizado que fue asignado a cada función Lambda. Este rol otorga permisos específicos como: •	PutItem y GetItem sobre DynamoDB •	Publish sobre SNS •	Acceso controlado a Step Functions y S3 (cuando aplica).
- API Gateway → Lambda (Trigger)
Se configuró API Gateway (HTTP) como disparador para varias funciones Lambda, especialmente crearReservaHandler.
Cuando el usuario envía el formulario desde la web, se ejecuta un POST /reservar, y API Gateway activa automáticamente la Lambda correspondiente.
Representado:
“HTTP Request (API Gateway)” → crearReservaHandler
- Lambda → DynamoDB
Todas las operaciones de reservas (crear, validar, listar, cancelar, actualizar) acceden a la base de datos DynamoDB desde Lambda.
Se creó la tabla Reservas con reservaId como clave principal.

## Integraciones Adicionales (Hay puntitos por el esfuerzo? xd
- Lambda → SNS (Correo de confirmación)
La función crearReservaHandler publica un mensaje en un SNS Topic, lo que dispara el envío automático de un correo electrónico al usuario.
Esta notificación se activa tras registrar exitosamente una reserva.

- Lambda → S3 (opcional desde Step Functions)
En el flujo de actualizarEstadoHandler, existe una escritura a S3 (por ejemplo, para logs o reportes).
Esto fue modelado dentro del flujo de Step Functions.

- Frontend (S3 Website) → API Gateway
La página index.html alojada en S3 envía solicitudes HTTP a la API REST a través de JavaScript (fetch()), con validación previa en el navegador.




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

## Lo queremos mucho profesor xd.
