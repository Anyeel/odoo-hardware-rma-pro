# Odoo Hardware RMA Pro

![Odoo Version](https://img.shields.io/badge/Odoo-17.0-purple?style=flat&logo=odoo)
![Docker](https://img.shields.io/badge/Docker-Containerized-blue?style=flat&logo=docker)
![CI/CD](https://img.shields.io/badge/GitHub%20Actions-Passing-brightgreen?style=flat&logo=githubactions)
![Security](https://img.shields.io/badge/Cloudflare-Zero%20Trust-orange?style=flat&logo=cloudflare)

Solución ERP integral para la gestión de devoluciones y garantías de hardware (RMA). Este proyecto no es solo un módulo, es una **arquitectura de microservicios completa** basada en Odoo 17, diseñada para entornos de producción modernos.

## Características Premium

Este sistema supera una implementación estándar académica incluyendo funcionalidades de consultoría real:

1.  **⚡ Flujo de Trabajo (Workflow) con Bloqueo:**
    * Estados lógicos: *Borrador ➝ Confirmado ➝ Diagnóstico ➝ Reparación ➝ Entregado*.
    * **Seguridad:** Los tickets se bloquean (Read-only) automáticamente al finalizar para garantizar la integridad de los datos.
2.  **🎨 Vista Kanban Interactiva:**
    * Gestión visual tipo "Trello" con columnas fijas y *Drag & Drop* para mover tickets entre estados.
3.  **📄 Reportes QWeb PDF Inteligentes:**
    * Generación de resguardos de reparación con **Código de Barras** dinámico y términos legales.
4.  **🔢 Secuenciación Automática:**
    * Generación de IDs únicos profesionales (ej: `RMA/2026/0045`) mediante reglas de secuencia XML.
5.  **🤖 DevOps & CI/CD:**
    * Despliegue automatizado con **Docker Compose**.
    * Pipeline de Integración Continua con **GitHub Actions** para testear el código en cada *push*.

---

## 🛠️ Stack Tecnológico

| Capa | Tecnología | Descripción |
| :--- | :--- | :--- |
| **Orquestación** | Docker Compose | Contenedores aislados para Web y Base de Datos. |
| **Backend** | Python 3.10 + Odoo ORM | Lógica de negocio, Restricciones y Modelos. |
| **Frontend** | XML + QWeb | Vistas Form, Tree, Kanban y Reportes PDF. |
| **Base de Datos** | PostgreSQL 16 | Persistencia de datos gestionada por Docker. |
| **Red & Seguridad** | Cloudflare Tunnel | Exposición segura HTTPS sin abrir puertos (CGNAT friendly). |

---

## 📂 Estructura del Proyecto

El repositorio sigue las mejores prácticas de "Clean Code" ignorando archivos binarios de Odoo:

```text
odoo-hardware-rma-pro/
├── .github/workflows/      # 🤖 Pipeline CI/CD (Tests automáticos)
├── custom_addons/          # 📦 Módulos desarrollados a medida
│   └── hardware_rma/
│       ├── models/         # Lógica Python (Tickets, Productos)
│       ├── views/          # Interfaz XML (Kanban, Menús)
│       ├── report/         # Plantillas PDF y Códigos de Barras
│       ├── data/           # Secuencias automáticas (No Update)
│       └── security/       # ACLs (Permisos de acceso)
├── docker-compose.yml      # 🐳 Infraestructura como Código (IaC)
└── README.md               # Documentación

```

---

## 🚀 Guía de Despliegue (Deployment)

Existen dos formas de arrancar este proyecto:

### Opción A: Despliegue en Producción (Demo Remota)

Para la presentación en clase, se utiliza una arquitectura **Zero Trust** mediante Cloudflare.

1. **Arrancar servicios:**
```bash
docker compose up -d

```


2. **Abrir Túnel Seguro (HTTPS):**
```bash
cloudflared tunnel --url http://localhost:8069

```

*Esto generará una URL pública temporal (ej: `https://demo-rma.trycloudflare.com`) accesible desde la red del instituto.*

### Opción B: Despliegue Local (Contingencia)

Si no hay internet, el sistema funciona 100% offline:

1. Clonar y levantar:
```bash
git clone [https://github.com/Anyeel/odoo-hardware-rma-pro.git](https://github.com/Anyeel/odoo-hardware-rma-pro.git)
cd odoo-hardware-rma-pro
docker compose up -d

```

2. Acceder vía navegador:
* URL: `http://localhost:8069`

---

*Proyecto desarrollado por Ángel Millán para el módulo de Sistemas de Gestión Empresarial (SGE) - Desarrollo de Aplicaciones Multiplataforma.*

