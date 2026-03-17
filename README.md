<div align="center">

# DjangoProject

Aplicación web desarrollada con **Django 4.2.3** y **Python 3**, estructurada en tres módulos con funcionalidades distintas.

![Python](https://img.shields.io/badge/Python-3.12+-blue)
![Django](https://img.shields.io/badge/Django-4.2.3-green)
![Bootstrap](https://img.shields.io/badge/Bootstrap-4.6.2-purple)

</div>

## Características

- **Página principal** — Landing page con acceso directo a las secciones del proyecto.
- **Portfolio** — Listado de proyectos con detalle individual, almacenados en base de datos SQLite.
- **API** — Consumo de la API pública [FreeToGame](https://www.freetogame.com/api/games) con paginación y búsqueda integrada mediante DataTables.

## Stack

| Tecnología    | Versión |
| ------------- | ------- |
| Python        | 3.12+   |
| Django        | 4.2.3   |
| Bootstrap     | 4.6.2   |
| jQuery        | 3.7.1   |
| DataTables    | 1.13.6  |
| Base de datos | SQLite  |

## Requisitos

- Python 3.12+
- pip

## Instalación y uso

```bash
# 1. Clonar el repositorio
git clone <url-del-repositorio>
cd DjangoProject

# 2. Crear y activar el entorno virtual
python3 -m venv proyectodjango
source proyectodjango/bin/activate

# 3. Instalar dependencias
pip install "Django==4.2.3" requests

# 4. Aplicar migraciones
cd myproject
python manage.py migrate

# 5. Iniciar el servidor de desarrollo
python manage.py runserver
```

La aplicación estará disponible en `http://127.0.0.1:8000`.

## Estructura de URLs

| Ruta               | Descripción                           |
| ------------------ | ------------------------------------- |
| `/`                | Página principal                      |
| `/portfolio/`      | Lista de proyectos                    |
| `/portfolio/<id>/` | Detalle de un proyecto                |
| `/api/`            | Juegos gratuitos desde FreeToGame API |
| `/admin/`          | Panel de administración de Django     |

---

<div align="center">

Desarrollado con Django · Python 3 · Bootstrap 4.6.2

</div>
