from django.urls import include, path

from alerts.views import root


urlpatterns = [
    path("", root, name="root"),
    path("alerts/", include("alerts.urls")),
]