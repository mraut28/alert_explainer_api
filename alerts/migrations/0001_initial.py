from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Alert",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.TextField()),
                (
                    "severity",
                    models.CharField(
                        choices=[
                            ("critical", "Critical"),
                            ("warning", "Warning"),
                            ("info", "Info"),
                        ],
                        max_length=10,
                    ),
                ),
                ("source", models.TextField()),
                ("metric_name", models.TextField()),
                ("metric_value", models.FloatField()),
                ("threshold", models.FloatField()),
                ("created_at", models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                "db_table": "alerts",
                "ordering": ["id"],
            },
        ),
    ]