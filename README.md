# Trackify API

Trackify API es un backend construido con **FastAPI** que permite gestionar hábitos, recordatorios y el progreso diario de los usuarios. El proyecto sigue una arquitectura por capas (routers → servicios → repositorios → modelos) que facilita el mantenimiento y la escalabilidad de la plataforma.

## 🚀 Características principales
- **Autenticación con JWT** para registro, inicio de sesión y consulta del perfil actual del usuario.【F:api/auth_router.py†L1-L31】【F:core/security.py†L1-L26】
- **Gestión completa de usuarios, hábitos, registros diarios y recordatorios** con operaciones CRUD protegidas mediante dependencias de autenticación.【F:api/base_router.py†L1-L44】【F:db/models/user.py†L1-L27】【F:db/models/habits.py†L1-L22】【F:db/models/habit_log.py†L1-L16】【F:db/models/reminder.py†L1-L15】
- **Creación automática de tablas** al iniciar la aplicación gracias al `lifespan` de FastAPI y a SQLAlchemy.【F:main.py†L1-L35】

## 🧱 Arquitectura del proyecto
```
TRACKIFY_BackEnd/
├── api/            # Routers HTTP y puntos finales
├── core/           # Configuración, seguridad y dependencias comunes
├── db/             # Modelos declarativos y sesión de SQLAlchemy
├── repositories/   # Acceso a datos y operaciones CRUD básicas
├── schemas/        # Validaciones y serialización con Pydantic
├── services/       # Lógica de negocio por recurso
└── main.py         # Punto de entrada FastAPI
```

Cada capa se comunica con la siguiente para mantener responsabilidades claras: los routers reciben las solicitudes HTTP, delegan en servicios que orquestan la lógica de negocio y estos, a su vez, utilizan repositorios para interactuar con la base de datos.【F:api/base_router.py†L1-L44】【F:services/base_service.py†L1-L27】【F:repositories/base_repository.py†L1-L35】

## ✅ Requisitos previos
- Python 3.10 o superior
- MySQL o MariaDB en ejecución
- `pip` y (opcional) `virtualenv`

## 🔧 Puesta en marcha rápida
1. **Clona el repositorio**
   ```bash
   git clone <url-del-repo>
   cd TRACKIFY_BackEnd
   ```
2. **Crea y activa un entorno virtual (opcional pero recomendado)**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # En Windows: .venv\Scripts\activate
   ```
3. **Instala las dependencias**
   ```bash
   pip install fastapi "uvicorn[standard]" sqlalchemy pymysql "python-jose[cryptography]" "passlib[bcrypt]" pydantic-settings
   ```
4. **Configura las variables de entorno** creando un archivo `.env` en la raíz con tus credenciales de base de datos (ver siguiente sección).
5. **Inicializa la base de datos** creando un esquema vacío llamado `TRACKIFY` (o el nombre que definas en `.env`).
6. **Inicia el servidor**
   ```bash
   uvicorn main:app --reload
   ```
7. Visita `http://127.0.0.1:8000/docs` para explorar la documentación interactiva generada automáticamente.

## 🔐 Variables de entorno
El proyecto utiliza `pydantic-settings` para cargar la configuración desde un archivo `.env`. Los campos disponibles son los siguientes, con sus valores por defecto:
```env
DB_USER=root
DB_PASSWORD=1234
DB_HOST=localhost
DB_PORT=3306
DB_NAME=TRACKIFY
```
Puedes ajustarlos según tu despliegue. A partir de estos valores se construye la URL de conexión `mysql+pymysql://<usuario>:<password>@<host>:<puerto>/<base>` consumida por SQLAlchemy.【F:core/config.py†L1-L22】

## ▶️ Ejecución y ciclo de vida
Al arrancar la aplicación, FastAPI invoca el `lifespan` definido en `main.py`, que crea automáticamente todas las tablas declaradas en los modelos si aún no existen. Esto facilita el arranque en entornos de desarrollo sin ejecutar migraciones manuales.【F:main.py†L8-L31】

## 📡 Endpoints principales
| Recurso | Prefijo | Descripción |
|---------|---------|-------------|
| Autenticación | `/auth` | Registro, login con OAuth2 y obtención del usuario autenticado actual.【F:api/auth_router.py†L1-L31】 |
| Usuarios | `/users` | CRUD completo de usuarios, protegido por autenticación JWT.【F:api/base_router.py†L16-L44】【F:api/user_router.py†L1-L10】 |
| Hábitos | `/habits` | Gestión de hábitos, frecuencia y metadatos visuales asociados a cada usuario.【F:api/habit_router.py†L1-L10】【F:db/models/habits.py†L1-L22】 |
| Registros de hábitos | `/habit_logs` | Seguimiento diario del cumplimiento y notas opcionales.【F:api/habit_log_router.py†L1-L10】【F:db/models/habit_log.py†L1-L16】 |
| Recordatorios | `/reminders` | Recordatorios programados para cada hábito con hora y mensaje personalizado.【F:api/reminder_router.py†L1-L10】【F:db/models/reminder.py†L1-L15】 |
| Salud del servicio | `/` | Mensaje de bienvenida para comprobar que la API está activa.【F:main.py†L33-L35】 |

> ℹ️ Las rutas CRUD utilizan dependencias que validan el token JWT mediante `get_current_user`, por lo que solo los usuarios autenticados pueden operar con sus recursos.【F:api/base_router.py†L16-L23】
