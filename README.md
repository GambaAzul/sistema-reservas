# Sistema de Reservas de Canchas de Fútbol

## Descripción
Proyecto para la gestión eficiente de reservas de canchas de fútbol, con backend, pipeline CI/CD, análisis de seguridad y monitoreo.

## Arquitectura
- Backend en Node.js con pruebas unitarias.
- Pipeline con GitHub Actions que incluye Checkov, Bandit, Trivy y pruebas automatizadas.
- Contenedores Docker y monitoreo con Prometheus y Grafana.

## Características
- Gestión de usuarios y reservas.
- Pruebas automatizadas con Jest y Pytest.
- Escaneo de vulnerabilidades y análisis de infraestructura como código.
- Monitoreo y logging con métricas en dashboards.

## Pipeline
El pipeline se ejecuta en GitHub Actions y realiza:
- Escaneo de seguridad IaC con Checkov.
- Linter de seguridad para Python con Bandit.
- Análisis de vulnerabilidades en contenedores con Trivy.
- Ejecución de pruebas automatizadas.

## Documentación
Aquí se debe ampliar la documentación técnica y funcional del sistema.

## Cómo contribuir
1. Clona el repositorio.
2. Crea ramas para features.
3. Haz pull requests para revisión.
4. Ejecuta pruebas antes de enviar cambios.

## Contacto
Desarrollador: [Jefferson Anton Jacinto]
# Trigger pipeline
