from fastapi import FastAPI

# ============================================
# CONFIGURACIÓN EMPRESA EXPORTADORA
# ============================================

MENSAJES_BIENVENIDA: dict[str, str] = {
    "es": "Bienvenido/a, {name}, a nuestra empresa exportadora.",
    "en": "Welcome, {name}, to our export company.",
    "fr": "Bienvenue, {name}, dans notre entreprise d'exportation.",
    "pt": "Bem-vindo(a), {name}, à nossa empresa exportadora.",
}

IDIOMAS_SOPORTADOS = list(MENSAJES_BIENVENIDA.keys())

# ============================================
# APLICACIÓN FASTAPI
# ============================================

app = FastAPI(
    title="API Empresa Exportadora",
    description="API para la gestión internacional de exportaciones",
    version="1.0.0",
)

# ============================================
# ENDPOINT RAÍZ
# ============================================

@app.get("/")
async def inicio() -> dict[str, str | list[str]]:
    """
    Retorna información general de la API.
    """

    return {
        "name": "API Empresa Exportadora",
        "version": "1.0.0",
        "docs": "/docs",
        "entities": [
            "products",
            "clients",
            "shipments",
            "certifications",
        ],
        "languages": IDIOMAS_SOPORTADOS,
    }

# ============================================
# ENDPOINT CLIENTES
# ============================================

@app.get("/clients/{name}")
async def bienvenida_cliente(
    name: str,
    language: str = "es",
) -> dict[str, str]:
    """
    Genera una bienvenida para clientes internacionales.
    """

    template = MENSAJES_BIENVENIDA.get(
        language,
        MENSAJES_BIENVENIDA["es"],
    )

    mensaje = template.format(name=name)

    return {
        "message": mensaje,
        "language": language,
        "client": name,
    }

# ============================================
# ENDPOINT PRODUCTOS
# ============================================

@app.get("/products/{product_name}")
async def informacion_producto(
    product_name: str,
    certification_level: str = "standard",
) -> dict[str, str]:
    """
    Retorna información de productos exportados.
    """

    return {
        "product": product_name,
        "certification_level": certification_level,
        "status": "available for export",
    }

# ============================================
# FUNCIÓN HORARIO DE ENVÍOS
# ============================================

def obtener_horario_envio(hour: int) -> tuple[str, str]:
    """
    Determina el horario del envío según la hora.
    """

    if 5 <= hour < 12:
        return ("Horario de envío en la mañana", "morning")

    if 12 <= hour < 18:
        return ("Horario de envío en la tarde", "afternoon")

    return ("Horario de envío en la noche", "night")

# ============================================
# ENDPOINT ENVÍOS
# ============================================

@app.get("/shipments/{shipment_id}/schedule")
async def horario_envio(
    shipment_id: str,
    hour: int,
) -> dict[str, str | int]:
    """
    Retorna información logística del envío.
    """

    if hour < 0 or hour > 23:
        return {
            "error": "La hora debe estar entre 0 y 23",
        }

    horario, periodo = obtener_horario_envio(hour)

    return {
        "shipment_id": shipment_id,
        "schedule": horario,
        "hour": hour,
        "period": periodo,
    }

# ============================================
# HEALTH CHECK
# ============================================

@app.get("/health")
async def estado_api() -> dict[str, str]:
    """
    Verifica el estado de la API.
    """

    return {
        "status": "healthy",
        "service": "export-company-api",
        "version": "1.0.0",
    }