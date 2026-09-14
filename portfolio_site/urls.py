from django.contrib import admin
from django.urls import include, path

# This is the top-level URL config for the entire project.
# It tells Django which URLs belong to the admin panel and which belong to your app.
urlpatterns = [
    # Django admin site lives at /admin/
    path("admin/", admin.site.urls),

    # Everything else is routed to the portfolio_app URLs.
    # For example: /, /profile/, /skills/, /projects/
    path("", include("portfolio_app.urls")),
]
