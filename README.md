# 🚀 Odoo Hardware RMA Management

![Odoo Version](https://img.shields.io/badge/Odoo-17.0-purple) ![Python](https://img.shields.io/badge/Python-3.12-blue) ![Status](https://img.shields.io/badge/Status-Development-green)

Este proyecto implementa una solución ERP personalizada sobre **Odoo 17 Community Edition** para una empresa de hardware. El núcleo del proyecto es el desarrollo de un módulo *ad-hoc* (`hardware_rma`) que extiende la funcionalidad nativa de inventario para gestionar devoluciones, garantías y diagnósticos técnicos.

## 📋 Descripción del Proyecto

A diferencia de una implementación estándar, este proyecto incluye desarrollo **Backend (Python)** y **Frontend (XML Views)** para cubrir necesidades específicas del sector IT:
1.  **Validación Automática de Garantías:** Cálculo de vigencia basado en nº de serie y fecha de compra.
2.  **Flujo de Trabajo RMA:** Pipeline de estados (Borrador -> Diagnóstico -> Reparación -> Entregado).
3.  **Trazabilidad:** Historial completo de intervenciones por componente.

## 🛠️ Stack Tecnológico

* **Core:** Odoo 17.0 (Source Install)
* **Base de Datos:** PostgreSQL 16
* **Lenguaje:** Python 3.12 + XML (QWeb)
* **DevOps:** Docker (opcional), Cloudflare Tunnel
* **Automatización:** AutoHotkey v2 (para flujos de desarrollo y mantenimiento)

## 📂 Estructura del Módulo (`hardware_rma`)

El desarrollo sigue la arquitectura MVC estricta de Odoo:

```text
hardware_rma/
├── models/
│   ├── rma_ticket.py       # Lógica de negocio y estados del ticket
│   └── product_inherit.py  # Herencia del modelo product.template
├── views/
│   ├── rma_views.xml       # Vistas Form, Tree y Kanban
│   └── rma_menus.xml       # Estructura de menús en Odoo
├── security/
│   └── ir.model.access.csv # Listas de control de acceso (ACLs)
├── __manifest__.py         # Metadatos y dependencias
└── __init__.py

```

## 🚀 Estrategia de Despliegue (Deployment)

Para la presentación y uso en producción, se ha diseñado una arquitectura de **Self-Hosting** accesible públicamente sin exponer puertos vulnerables.

### 1. Servidor Principal (Tunneled)

El sistema corre en un servidor local protegido, expuesto a internet mediante **Cloudflare Tunnel**. Esto garantiza:

* Conexión **HTTPS/SSL** segura.
* Sin necesidad de abrir puertos en el router (CGNAT friendly).
* Acceso global mediante URL dedicada.

Comando de despliegue:

```bash
cloudflared tunnel --url http://localhost:8069

```

### 2. Plan de Recuperación ante Desastres (DRP)

En caso de fallo de conectividad en el servidor principal, el proyecto cuenta con una réplica local completa en el equipo de presentación (Laptop), sincronizada vía Git, asegurando la continuidad de la demostración.

## 🔧 Herramientas de Desarrollo (DevTools)

Se desarrollan scripts en **AutoHotkey v2** para optimizar el ciclo de vida del desarrollo (Hot-reloading):

* **`server_reload.ahk`**: Automatiza el reinicio del servicio Odoo y la actualización del módulo tras cambios en Python/XML (`-u hardware_rma`).
* **`keep_alive.ahk`**: Garantiza la disponibilidad del servidor evitando la suspensión del sistema anfitrión durante el despliegue.

## 📦 Instalación Local

1. Clonar el repositorio:
```bash
git clone [https://github.com/Anyeel/odoo-hardware-rma-pro.git](https://github.com/Anyeel/odoo-hardware-rma-pro.git)

```

2. Crear entorno virtual e instalar dependencias:
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

```

3. Ejecutar Odoo apuntando al directorio de módulos custom:
```bash
python odoo-bin -c odoo.conf --addons-path=addons,./custom_addons

```

*Proyecto desarrollado para el módulo de Sistemas de Gestión Empresarial (SGE) - DAM.*
