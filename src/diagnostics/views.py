from django.contrib.auth import get_user_model
from django.views.generic import DetailView, CreateView
from .forms import DiagnosticsForm
from .models import Diagnostics
from django.contrib.auth.mixins import LoginRequiredMixin
from businessplan.utils import try_get_context
from django.shortcuts import get_object_or_404
from django.http import Http404

User = get_user_model()

class DiagnosticsDetailView(DetailView):
    def get_object(self):
        slug = self.kwargs.get("slug")
        if slug is None:
            raise Http404
        return get_object_or_404(Diagnostics, slug__iexact=slug)

    def get_context_data(self, *args, **kwargs):
        context = super(DiagnosticsDetailView, self).get_context_data(*args, **kwargs)
        slug = self.kwargs.get("slug")
        if slug:
            user = Diagnostics.objects.get(slug=slug).get_user()
        else:
            user = self.request.user
        full_context = try_get_context(context, user)
        return full_context

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
        slug = self.kwargs.get("slug")
        if slug:
            user = Diagnostics.objects.get(slug=slug).get_user()
        else:
            user = self.request.user
        full_context = try_get_context(context, user)
        return full_context

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