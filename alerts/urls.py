from django.urls import path

from . import views


urlpatterns = [
    path("", views.alert_collection, name="alert-list-create"),
    path(
        "threshold/greater-than-100",
        views.alerts_with_threshold_over_100,
        name="alerts-threshold-over-100",
    ),
    path("<int:alert_id>/explain", views.explain_alert, name="alert-explain"),
    path("<int:alert_id>", views.alert_detail, name="alert-detail"),
]