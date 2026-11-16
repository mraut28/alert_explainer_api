from django.db import models
from django.utils import timezone


class Alert(models.Model):
    SEVERITY_CHOICES = [
        ("critical", "Critical"),
        ("warning", "Warning"),
        ("info", "Info"),
    ]

    title = models.TextField()
    severity = models.CharField(max_length=10, choices=SEVERITY_CHOICES)
    source = models.TextField()
    metric_name = models.TextField()
    metric_value = models.FloatField()
    threshold = models.FloatField()
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = "alerts"
        ordering = ["id"]