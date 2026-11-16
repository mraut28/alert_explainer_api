# AI Intelligence Layer - Alert Explainer API

A Django JSON API for storing monitoring alerts and generating rule-based explanations. Alert data is stored in the local SQLite database `alerts.db`.

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

For a new database, create the schema with:

```bash
python manage.py migrate
```

To reuse an existing `alerts.db` created by the previous SQLAlchemy version, fake the initial migration after confirming the `alerts` table exists. This records the Django migration without recreating the table or removing its data:

```bash
python manage.py migrate --fake-initial
```

Run the development server with:

```bash
python manage.py runserver
```

## API

- `GET /` returns service status.
- `POST /alerts/` creates an alert. The JSON body requires `title`, `severity` (`critical`, `warning`, or `info`), `source`, `metric_name`, `metric_value`, and `threshold`.
- `GET /alerts/` lists alerts.
- `GET /alerts/threshold/greater-than-100` lists alerts with a threshold strictly greater than 100.
- `GET /alerts/{alert_id}` retrieves one alert.
- `POST /alerts/{alert_id}/explain` returns a rule-based explanation.

The API currently has no authentication. Configure `DJANGO_SECRET_KEY` and `ALLOWED_HOSTS`, and add authentication before exposing it publicly. `alerts.db` and `.venv` are excluded from Git.