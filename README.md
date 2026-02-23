# 🚀 Odoo Hardware RMA & PC Configurator Pro

![Odoo Version](https://img.shields.io/badge/Odoo-17.0-purple?style=flat&logo=odoo)
![Docker](https://img.shields.io/badge/Docker-Containerized-blue?style=flat&logo=docker)
![CI/CD](https://img.shields.io/badge/GitHub%20Actions-Passing-brightgreen?style=flat&logo=githubactions)
![Security](https://img.shields.io/badge/Cloudflare-Zero%20Trust-orange?style=flat&logo=cloudflare)

Solución ERP integral para empresas de hardware y montaje de equipos. Este proyecto no es solo un módulo, es una **arquitectura de microservicios completa** basada en Odoo 17, diseñada para entornos de producción modernos. Incluye dos módulos *core* desarrollados a medida: Gestión de Garantías (RMA) y un Configurador Avanzado de PCs.

## 🌟 Características Premium

Este sistema supera una implementación estándar académica incluyendo funcionalidades de consultoría real:

### 🛠️ Módulo RMA (Gestión de Devoluciones y Garantías)
1.  **⚡ Flujo de Trabajo (Workflow) con Bloqueo:**
    * Estados lógicos: *Borrador ➝ Confirmado ➝ Diagnóstico ➝ Reparación ➝ Entregado*.
    * **Seguridad:** Los tickets se bloquean (Read-only) automáticamente al finalizar para garantizar la integridad de los datos.
2.  **🎨 Vista Kanban Interactiva:**
    * Gestión visual tipo "Trello" con columnas fijas y *Drag & Drop* para mover tickets entre estados.
3.  **📄 Reportes QWeb PDF Inteligentes:**
    * Generación de resguardos de reparación con **Código de Barras** dinámico y términos legales.
4.  **🔢 Secuenciación Automática:**
    * Generación de IDs únicos profesionales (ej: `RMA/2026/0045`) mediante reglas de secuencia XML.

### 💻 Módulo PC Configurator (Ensamblaje a Medida)
5.  **🧠 Motor de Reglas de Compatibilidad (Inteligencia de Negocio):**
    * Algoritmo de 3 capas que valida en tiempo real: Socket (CPU ↔ Placa Base), Tecnología (Placa Base ↔ RAM) y Vataje (GPU ↔ Fuente de Alimentación).
6.  **🔍 Extracción Dinámica de Atributos:**
    * Uso de Expresiones Regulares (`re`) en Python para aislar datos matemáticos (ej: extraer "750" de un atributo de texto "750W") directamente desde el "ADN" nativo del producto en Odoo.
7.  **🛡️ Prevención de Errores UX:**
    * Auto-vaciado de campos y bloqueo de UI con alertas preventivas detalladas al detectar mezclas incompatibles (Riesgo Físico o Cuello de Botella energético).

### 🤖 Arquitectura y DevOps
8.  **DevOps & CI/CD:**
    * Despliegue automatizado con **Docker Compose**.
    * Pipeline de Integración Continua con **GitHub Actions** para testear el código en cada *push*.

---

## 🛠️ Stack Tecnológico

| Capa | Tecnología | Descripción |
| :--- | :--- | :--- |
| **Orquestación** | Docker Compose | Contenedores aislados para Web y Base de Datos. |
| **Backend** | Python 3.10 + RegEx + Odoo ORM | Lógica de negocio, Restricciones, Helpers y Modelos. |
| **Frontend** | XML + QWeb | Vistas Form (Notebooks 2 columnas), Tree, Kanban y Reportes PDF. |
| **Base de Datos** | PostgreSQL 16 | Persistencia de datos gestionada por Docker. |
| **Red & Seguridad** | Cloudflare Tunnel | Exposición segura HTTPS sin abrir puertos (CGNAT friendly). |

---

## 📂 Estructura del Proyecto

El repositorio sigue las mejores prácticas de "Clean Code" estructurando la lógica en múltiples módulos:

```text
odoo-hardware-rma-pro/
├── .github/workflows/      # 🤖 Pipeline CI/CD (Tests automáticos)
├── custom_addons/          # 📦 Módulos desarrollados a medida
│   ├── hardware_rma/       # 🛠️ APP: Gestión de Garantías
│   │   ├── models/         # Lógica Python (Tickets)
│   │   ├── views/          # Interfaz XML (Kanban, Menús)
│   │   ├── report/         # Plantillas PDF
│   │   ├── data/           # Secuencias automáticas
│   │   └── security/       # ACLs
│   └── pc_configurator/    # 💻 APP: Configurador de PCs
│       ├── models/         # Motor de Reglas y lógica RegEx
│       ├── views/          # Formularios y Vistas interactivas
│       └── security/       # ACLs
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
