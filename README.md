# Portfolio Django App

A responsive multi-page personal portfolio built with Django, WhiteNoise, and Gunicorn for deployment on Render.

## Features

- Overview landing page with featured content snippets
- Dedicated profile, skills, and projects pages
- Responsive dark-mode design
- Clean, production-ready Django configuration for deployment

## Local setup

```bash
cd portfolio_django
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Open http://127.0.0.1:8000

## Deployment on Render

1. Push this code to a GitHub repository.
2. Create a new Web Service on Render.
3. Connect the repository.
4. Use the following settings:
   - Build command: `./build.sh`
   - Start command: `gunicorn portfolio_site.wsgi:application`
5. Add environment variables:
   - `DEBUG=False`
   - `SECRET_KEY=<strong-random-value>`
6. Deploy the service.

## Structure

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
