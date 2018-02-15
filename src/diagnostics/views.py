from django.contrib.auth import get_user_model
from django.views.generic import DetailView, CreateView, UpdateView, TemplateView
from .forms import DiagnosticsForm
from .models import Diagnostics
from django.contrib.auth.mixins import LoginRequiredMixin

User = get_user_model()

class DiagnosticsDetailView(DetailView):
    def get_queryset(self):
        return Diagnostics.objects.filter(user=self.request.user)

class DiagnosticsCreateView(LoginRequiredMixin, CreateView):
    template_name = 'forms/diag_create_form.html'
    form_class = DiagnosticsForm

    def get_queryset(self):
        return Diagnostics.objects.filter(user=self.request.user)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        return super(DiagnosticsCreateView, self).form_valid(form)

    def get_context_data(self, *args, **kwargs):
        context = super(DiagnosticsCreateView, self).get_context_data(*args, **kwargs)
        context['title'] = "Create Diagnostics"
        return context

# class DiagnosticsUpdateView(LoginRequiredMixin, UpdateView):
#     template_name = 'forms/diag_update_form.html'
#     form_class = Diagnostics
#
#     def get_queryset(self):
#         return Diagnostics.objects.filter(user=self.request.user)
#
#     def get_context_data(self, *args, **kwargs):
#         context = super(DiagnosticsUpdateView, self).get_context_data(*args, **kwargs)
#         context['title'] = "Update Diagnostics"
#         return context