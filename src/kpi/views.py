from django.views.generic import DetailView, CreateView, UpdateView, TemplateView
from businessplan.utils import try_get_context
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import GrossAndNet
from accounts.models import User # temporary solution

class KPIHomeView(LoginRequiredMixin, TemplateView):
    template_name = 'home_view.html'

    def get_context_data(self, *args, **kwargs):
        context = super(KPIHomeView, self).get_context_data(*args, **kwargs)
        full_context = try_get_context(context, self.request.user)
        return full_context

class KPIDemoView(LoginRequiredMixin, TemplateView):
    template_name = 'demo_view.html'

    def get_context_data(self, *args, **kwargs):
        context = super(KPIDemoView, self).get_context_data(*args, **kwargs)
        full_context = try_get_context(context, self.request.user)
        return full_context

    def get(self, request, *args, **kwargs):
        response = super(KPIDemoView, self).get(request, *args, **kwargs)
        response['X_EMAIL'] = request.user.email
        print(response['X_EMAIL'])
        return response


def get_data(request, *args, **kwargs):
    gross_and_nets = GrossAndNet.objects.filter(user=request.user)
    years = []
    gross_values = []
    net_values = []
    for gn in gross_and_nets:
        years.append(gn.get_year())
        gross_values.append(gn.get_gross())
        net_values.append(gn.get_net())
    data = {
        "labels": years,
        "gross_values": gross_values,
        "net_values": net_values,
    }
    return JsonResponse(data)

# Not using REST for now: this project has custom user and can't get the email from headers
class ChartData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        temporary_user = User.objects.get(email='lemac_cw@lemac.com') # temporary solution
        print(request.META.get('HTTP_X_EMAIL'))
        gross_and_nets = GrossAndNet.objects.filter(user=temporary_user)
        years = []
        gross_values = []
        net_values = []
        for gn in gross_and_nets:
            years.append(gn.get_year())
            gross_values.append(gn.get_gross())
            net_values.append(gn.get_net())
        data = {
            "labels": years,
            "gross_values": gross_values,
            "net_values": net_values,
        }
        return Response(data)

