# Troy Thai | Portfolio

A personal portfolio website built with Django to showcase my background, skills, and project work in a clean, professional format.

## About this project

This project is a simple but polished portfolio site designed to present who I am, what I can do, and the work I have built. It includes sections for an overview, profile, skills, and projects, making it easy to share my experience and connect with opportunities.

The site is built with Python and Django, and it is structured so it can be customized with personal content, links, and project details over time.

## Features

- Responsive portfolio layout
- Overview landing page
- Profile and background section
- Skills showcase
- Projects section
- Clean Django template structure for easy customization

## Local setup

```bash
cd portfolio_django
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Then open:

```text
http://127.0.0.1:8000/
```

## Project structure

```text
portfolio_django/
├── manage.py
├── requirements.txt
├── build.sh
├── Procfile
├── render.yaml
├── portfolio_site/
├── portfolio_app/
├── templates/
└── staticfiles/
```

## Deployment

This project is ready to be deployed to services like Render using the included build configuration.

## Contact

- Email: tri.t.thai404@gmail.com
- GitHub: https://github.com/Titania-Diablo
