from django.views.generic import DetailView, CreateView, UpdateView, TemplateView
from businessplan.utils import try_get_context
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import GraphData, ExcelTemplate
from accounts.models import User # temporary solution
from .utils import get_graph_elements_flow, get_graph_elements_gn, get_diagnostics_scores
from .forms import ExcelTemplateForm

class KPIHomeView(LoginRequiredMixin, CreateView):
    template_name = 'home_view.html'
    form_class = ExcelTemplateForm
    success_url = '#'

    def get_queryset(self):
        return ExcelTemplate.objects.filter(user=self.request.user)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        return super(KPIHomeView, self).form_valid(form)

    def get_context_data(self, *args, **kwargs):
        context = super(KPIHomeView, self).get_context_data(*args, **kwargs)
        slug = self.kwargs.get("slug")
        if slug:
            user = GraphData.objects.get(slug=slug).get_user()
        else:
            user = self.request.user
        full_context = try_get_context(context, user)
        return full_context

class KPIDemoView(LoginRequiredMixin, TemplateView):
    template_name = 'demo_view.html'

    def get_context_data(self, *args, **kwargs):
        context = super(KPIDemoView, self).get_context_data(*args, **kwargs)
        slug = self.kwargs.get("slug")
        if slug:
            user = GraphData.objects.get(slug=slug).get_user()
        else:
            user = self.request.user
        full_context = try_get_context(context, user)
        return full_context

    # def get(self, request, *args, **kwargs):
    #     response = super(KPIDemoView, self).get(request, *args, **kwargs)
    #     response['X_EMAIL'] = request.user.email
    #     print(response['X_EMAIL'])
    #     return response


def get_data(request, *args, **kwargs):
    kpis = GraphData.objects.filter(user=request.user)
    years, gross_values, net_values = get_graph_elements_gn(kpis)
    revenues, expenditures, cash_flow, flow_labels = get_graph_elements_flow(kpis)
    diag_scores, diag_scores_improv = get_diagnostics_scores(request.user)
    data = {
        "labels": years,
        "gross_values": gross_values,
        "net_values": net_values,
        "revenues": revenues,
        "expenditures": expenditures,
        "cash_flow": cash_flow,
        "flow_labels": flow_labels,
        "diag_scores": diag_scores,
        "diag_scores_improv": diag_scores_improv
    }
    return JsonResponse(data)

# Not using REST for now: this project has custom user and can't get the email from headers
# class ChartData(APIView):
#     authentication_classes = []
#     permission_classes = []
#
#     def get(self, request, format=None):
#         temporary_user = User.objects.get(email='lemac_cw@lemac.com') # temporary solution
#         print(request.META.get('HTTP_X_EMAIL'))
#         gross_and_nets = GrossAndNet.objects.filter(user=temporary_user)
#         years = []
#         gross_values = []
#         net_values = []
#         for gn in gross_and_nets:
#             years.append(gn.get_year())
#             gross_values.append(gn.get_gross())
#             net_values.append(gn.get_net())
#         data = {
#             "labels": years,
#             "gross_values": gross_values,
#             "net_values": net_values,
#         }
#         return Response(data)

