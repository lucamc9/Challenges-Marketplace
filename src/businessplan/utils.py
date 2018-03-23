from .models import BusinessPlan
from diagnostics.models import Diagnostics
from profiles.models import SMEProfile
from dataroom.models import Accordion
from diligence.models import DiligenceRoom

def try_get_context(context, request_user):
    # Get full context
    try:
        bp = BusinessPlan.objects.get(user=request_user)
        context['bp'] = bp
    except BusinessPlan.DoesNotExist:
        context['bp'] = None
    try:
        diag = Diagnostics.objects.filter(user=request_user)[0]
        context['diag'] = diag
    except Diagnostics.DoesNotExist:
        context['diag'] = None
    try:
        profile = SMEProfile.objects.get(user=request_user)
        context['profile'] = profile
    except SMEProfile.DoesNotExist:
        context['profile'] = None
    try:
        accordion = Accordion.objects.get(user=request_user)
        context['accordion'] = accordion
    except:
        context['accordion'] = None
    try:
        diligence = DiligenceRoom.objects.get(user=request_user)
        context['diligence'] = diligence
    except:
        context['diligence'] = None

    return context

