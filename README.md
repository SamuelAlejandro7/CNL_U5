# Unidad 5 CLN - Integración, Pruebas y Calidad

Este proyecto contiene la suite automatizada de pruebas para el sistema de pedidos de nuestra empresa. El objetivo principal es garantizar la calidad del software mediante pruebas unitarias, de integración y de seguridad, alcanzando una cobertura mínima del 80%.

## Mapa de Arquitectura

El sistema sigue una arquitectura de Puertos y Adaptadores (Hexagonal) para aislar la lógica de negocio de las dependencias externas:

* **Usuario/API** → **Application Service** → **Entidades / Value Objects / Reglas de dominio**
* **Application Service** ↓ *puertos* → **Repositorio | Pasarela de pago | Bus de eventos**
* **Repositorio | Pasarela de pago | Bus de eventos** ↓ *adaptadores* → **SQLAlchemy | API externa | mensajería**

## Requisitos Previos

* Python 3.11 o superior.
* Git.

## Instalación y Configuración

1. Clonar el repositorio:
   git clone https://github.com/SamuelAlejandro7/CNL_U5.git
   cd CNL_U5

2. Crear y activar el entorno virtual (Windows PowerShell):
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1

3. Instalar dependencias:
   python -m pip install -r requirements.txt

## Ejecución de Pruebas

Para ejecutar la suite de pruebas y generar el reporte de cobertura:
   python -m pytest -v --cov=src --cov-report=term-missing --cov-report=html --cov-fail-under=80

Para verificar el estilo del código con Ruff:
   python -m ruff check src tests