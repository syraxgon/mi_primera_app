# Temperature Monitoring System

Este proyecto es un sistema de monitoreo de temperatura que utiliza un sensor de temperatura resistivo conectado a un ESP32. Los datos del sensor se envían a un backend desarrollado con Django y se almacenan en una base de datos PostgreSQL. El frontend está desarrollado con React y Tailwind CSS para mostrar los datos de temperatura en una interfaz web.

## Tabla de Contenidos

- [Requisitos](#requisitos)
- [Instalación](#instalación)
  - [Backend](#backend)
  - [Frontend](#frontend)
- [Uso](#uso)
- [API](#api)
- [Contribuir](#contribuir)
- [Licencia](#licencia)

## Requisitos

- Python 3.x
- PostgreSQL
- Node.js
- ESP32 con MicroPython

## Instalación

### Backend

1. Clona el repositorio:

    ```bash
    git clone https://github.com/tuusuario/temp-monitor.git
    cd temp-monitor
    ```

2. Crea y activa un entorno virtual:

    ```bash
    python -m venv env
    source env/bin/activate  # En Windows usa `env\Scripts\activate`
    ```

3. Instala las dependencias:

    ```bash
    pip install django psycopg2-binary django-cors-headers
    ```

4. Configura la base de datos PostgreSQL en `temp_monitor/settings.py`:

    ```python
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'your_db_name',
            'USER': 'your_db_user',
            'PASSWORD': 'your_db_password',
            'HOST': 'localhost',
            'PORT': '5432',
        }
    }
    ```

5. Añade la configuración de CORS en `settings.py`:

    ```python
    INSTALLED_APPS = [
        ...
        'corsheaders',
        'sensors',
    ]

    MIDDLEWARE = [
        ...
        'corsheaders.middleware.CorsMiddleware',
        ...
    ]

    CORS_ALLOWED_ORIGINS = [
        "http://localhost:3000",
    ]
    ```

6. Aplica las migraciones y arranca el servidor:

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    python manage.py runserver
    ```

### Frontend

1. Ve al directorio del frontend:

    ```bash
    cd temp-monitor-frontend
    ```

2. Instala las dependencias:

    ```bash
    npm install
    ```

3. Instala Tailwind CSS:

    ```bash
    npm install -D tailwindcss
    npx tailwindcss init
    ```

4. Configura Tailwind CSS en `tailwind.config.js`:

    ```javascript
    module.exports = {
      content: [
        "./src/**/*.{js,jsx,ts,tsx}",
      ],
      theme: {
        extend: {},
      },
      plugins: [],
    }
    ```

5. Importa Tailwind CSS en `src/index.css`:

    ```css
    @tailwind base;
    @tailwind components;
    @tailwind utilities;
    ```

6. Arranca la aplicación React:

    ```bash
    npm start
    ```

## Uso

1. Asegúrate de que el servidor de Django y la aplicación React estén corriendo.
2. Navega a `http://localhost:3000` en tu navegador.
3. Podrás ver las lecturas de temperatura en la interfaz web.

## API

### `POST /api/sensors/record/`

Registra una nueva lectura de temperatura.

- **Request:**
  - Body: `{"temperature": float, "timestamp": "YYYY-MM-DDTHH:MM:SSZ"}`

- **Response:**
  - Success: `{"status": "success"}`

### `GET /api/sensors/temperatures/`

Obtiene todas las lecturas de temperatura.

- **Response:**
  - Success: `[{ "temperature": float, "timestamp": "YYYY-MM-DDTHH:MM:SSZ" }, ...]`

## Contribuir

1. Haz un fork del proyecto.
2. Crea una nueva rama (`git checkout -b feature/nueva-funcionalidad`).
3. Realiza tus cambios y haz commit (`git commit -am 'Añadir nueva funcionalidad'`).
4. Sube tus cambios (`git push origin feature/nueva-funcionalidad`).
5. Crea un Pull Request.

## Licencia

Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo [LICENSE](LICENSE) para más detalles.
