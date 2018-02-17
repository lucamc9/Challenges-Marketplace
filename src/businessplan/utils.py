from .models import BusinessPlan
from diagnostics.models import Diagnostics
from profiles.models import SMEProfile

def try_get_context(context, request_user):
    # Get full context
    try:
        bp = BusinessPlan.objects.get(user=request_user)
        context['bp'] = bp
    except BusinessPlan.DoesNotExist:
        context['bp'] = None
    try:
        diag = Diagnostics.objects.get(user=request_user)
        context['diag'] = diag
    except Diagnostics.DoesNotExist:
        context['diag'] = None
    try:
        profile = SMEProfile.objects.get(user=request_user)
        context['profile'] = profile
    except SMEProfile.DoesNotExist:
        context['profile'] = None

    return context