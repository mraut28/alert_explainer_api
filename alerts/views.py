import json

from django.http import JsonResponse
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_GET, require_http_methods, require_POST

from services.explainer import generate_explanation

from .forms import AlertCreateForm
from .models import Alert


def _serialize_alert(alert: Alert) -> dict[str, object]:
    return {
        "id": alert.id,
        "title": alert.title,
        "severity": alert.severity,
        "source": alert.source,
        "metric_name": alert.metric_name,
        "metric_value": alert.metric_value,
        "threshold": alert.threshold,
        "created_at": alert.created_at.isoformat(),
    }


def _read_alert_payload(request):
    if request.content_type != "application/json":
        return None, JsonResponse(
            {"detail": "Content-Type must be application/json"}, status=415
        )
    try:
        payload = json.loads(request.body)
    except (json.JSONDecodeError, UnicodeDecodeError):
        return None, JsonResponse({"detail": "Invalid JSON body"}, status=400)
    if not isinstance(payload, dict):
        return None, JsonResponse({"detail": "JSON body must be an object"}, status=422)

    form = AlertCreateForm(payload)
    if not form.is_valid():
        return None, JsonResponse({"detail": form.errors.get_json_data()}, status=422)
    return form.cleaned_data, None


@require_GET
def root(request):
    return JsonResponse({"status": "AI Intelligence Layer is running"})


@csrf_exempt
@require_http_methods(["GET", "POST"])
def alert_collection(request):
    if request.method == "GET":
        alerts = Alert.objects.order_by("id")
        return JsonResponse([_serialize_alert(alert) for alert in alerts], safe=False)

    payload, error_response = _read_alert_payload(request)
    if error_response is not None:
        return error_response

    alert = Alert.objects.create(**payload)
    return JsonResponse(_serialize_alert(alert), status=201)


@require_GET
def alerts_with_threshold_over_100(request):
    alerts = Alert.objects.filter(threshold__gt=100).order_by("id")
    return JsonResponse([_serialize_alert(alert) for alert in alerts], safe=False)


@require_GET
def alert_detail(request, alert_id: int):
    try:
        alert = Alert.objects.get(pk=alert_id)
    except Alert.DoesNotExist:
        return JsonResponse({"detail": "Alert not found"}, status=404)
    return JsonResponse(_serialize_alert(alert))


@csrf_exempt
@require_POST
def explain_alert(request, alert_id: int):
    try:
        alert = Alert.objects.get(pk=alert_id)
    except Alert.DoesNotExist:
        return JsonResponse({"detail": "Alert not found"}, status=404)
    return JsonResponse(
        {
            "alert_id": alert.id,
            "explanation": generate_explanation(alert),
            "generated_at": timezone.now().isoformat(),
        }
    )