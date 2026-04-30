# 🌎 API Empresa Exportadora

Proyecto desarrollado con **FastAPI** para la gestión básica de una empresa de exportación internacional.

---

# 📖 Descripción

La API permite simular operaciones relacionadas con una empresa exportadora, manejando información de:

- 🌍 Clientes internacionales
- 📦 Productos exportados
- 🚚 Envíos internacionales
- 📄 Certificaciones

El proyecto fue creado como práctica de desarrollo backend utilizando:

- Python moderno
- FastAPI
- Docker
- Uvicorn
- Git y GitHub

---

# 🎯 Objetivos del Proyecto

Este proyecto tiene como finalidad aplicar conceptos fundamentales de:

- Creación de APIs REST
- Type hints
- Path parameters
- Query parameters
- Documentación automática
- Dockerización de aplicaciones

---

# 🗂️ Estructura del Proyecto

```text
3-proyecto/
│
├── README.md
│
├── starter/
│   ├── Dockerfile
│   ├── docker-compose.yml
│   ├── pyproject.toml
│   │
│   └── src/
│       └── main.py
│
└── solution/
```

---

# ⚙️ Tecnologías Utilizadas

| Tecnología | Descripción |
|---|---|
| Python 3.12 | Lenguaje principal |
| FastAPI | Framework backend |
| Uvicorn | Servidor ASGI |
| Docker | Contenedores |
| Git & GitHub | Control de versiones |

---

# 🚀 Instalación y Ejecución

## ▶️ Ejecutar localmente

Desde la carpeta `starter`:

```bash id="l8z8l7"
python -m uvicorn src.main:app --reload
```

---

## 🐳 Ejecutar con Docker

```bash id="rkg2pm"
docker compose up --build
```

---

# 🌐 Acceso a la API

Una vez iniciado el servidor:

```text id="3klsy6"
http://localhost:8000
```

---

# 📚 Documentación Automática

FastAPI genera automáticamente la documentación interactiva.

Acceder desde:

```text id="v6kv7e"
http://localhost:8000/docs
```

---

# 🔗 Endpoints Disponibles

## 🏠 Información General

```http id="hnuv2v"
GET /
```

Retorna información general de la API.

---

## 👥 Bienvenida a Clientes

```http id="ehn0dv"
GET /clients/{name}
```

### Ejemplo

```http id="cbql1x"
/clients/Carlos?language=en
```

---

## 📦 Información de Productos

```http id="8vrh3c"
GET /products/{product_name}
```

### Ejemplo

```http id="m9yj5x"
/products/Coffee
```

---

## 🚚 Horario de Envíos

```http id="qjlwmv"
GET /shipments/{shipment_id}/schedule?hour=10
```

---

## ❤️ Health Check

```http id="0f3cln"
GET /health
```

Verifica el estado actual de la API.

---

# ✅ Características Implementadas

- FastAPI application
- Type hints
- Path parameters
- Query parameters
- Funciones async
- Validaciones básicas
- Documentación automática
- Docker support

---

# 👩‍💻 Autor

Proyecto desarrollado para el Bootcamp **FastAPI Zero to Hero**.