<div align="center">

# DjangoProject

Aplicación web desarrollada con **Django 4.2.3** y **Python 3.8.10**, estructurada en tres módulos con funcionalidades distintas.

![Python](https://img.shields.io/badge/Python-3.8.10-blue)
![Django](https://img.shields.io/badge/Django-4.2.3-green)

</div>

## Características

- **Página principal** — Landing page de bienvenida.
- **Portfolio** — Listado de proyectos con detalle individual, almacenados en base de datos SQLite.
- **API** — Consumo de la API pública [FreeToGame](https://www.freetogame.com/api/games) con paginación de resultados.

## Requisitos

- Python 3.8.10
- virtualenv

## Instalación y uso

```bash
# 1. Clonar el repositorio
git clone <url-del-repositorio>
cd DjangoProject

# 2. Activar el entorno virtual
source proyectodjango/bin/activate

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. Aplicar migraciones
cd myproject
python manage.py migrate

# 5. Iniciar el servidor de desarrollo
python manage.py runserver
```

La aplicación estará disponible en `http://127.0.0.1:8000`.

## Estructura de URLs

| Ruta | Descripción |
|------|-------------|
| `/` | Página principal |
| `/portfolio/` | Lista de proyectos |
| `/portfolio/<id>/` | Detalle de un proyecto |
| `/api/` | Juegos gratuitos desde FreeToGame API |
| `/admin/` | Panel de administración de Django |

---

<div align="center">

Desarrollado con Django · Python 3.8.10

</div>
