from django.urls import path

from . import views

# This file maps each URL to a view function.
# In Django, a URL route is like a doorway to a page.
urlpatterns = [
    # The homepage: "" means the root URL such as http://127.0.0.1:8000/
    path("", views.home, name="home"),

    # Example: http://127.0.0.1:8000/profile/
    path("profile/", views.profile, name="profile"),

    # Example: http://127.0.0.1:8000/skills/
    path("skills/", views.skills, name="skills"),

    # Example: http://127.0.0.1:8000/projects/
    path("projects/", views.projects, name="projects"),

    # Beginner learning page: http://127.0.0.1:8000/learning/
    path("learning/", views.learning, name="learning"),
]
