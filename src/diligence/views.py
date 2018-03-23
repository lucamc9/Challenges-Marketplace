from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
from django.views.generic import DetailView, CreateView, UpdateView, TemplateView
from .forms import DiligenceRoomForm
from .models import DiligenceRoom
from businessplan.utils import try_get_context
import os
from django.conf import settings
from django.http import HttpResponse, Http404

User = get_user_model()

class DiligenceRoomDetailView(DetailView):
    def get_queryset(self):
        return DiligenceRoom.objects.filter(user=self.request.user)

    def get_context_data(self, *args, **kwargs):
        context = super(DiligenceRoomDetailView, self).get_context_data(*args, **kwargs)
        full_context = try_get_context(context, self.request.user)
        return full_context

class DiligenceRoomCreateView(LoginRequiredMixin, CreateView):
    template_name = 'forms/diligence_create_form.html'
    form_class = DiligenceRoomForm

    def get_queryset(self):
        return DiligenceRoom.objects.filter(user=self.request.user)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        return super(DiligenceRoomCreateView, self).form_valid(form)

    def get_context_data(self, *args, **kwargs):
        context = super(DiligenceRoomCreateView, self).get_context_data(*args, **kwargs)
        context['title'] = "Create Diligence Room"
        full_context = try_get_context(context, self.request.user)
        return full_context

class DiligenceRoomUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'forms/diligence_update_form.html'
    form_class = DiligenceRoomForm

    def get_queryset(self):
        return DiligenceRoom.objects.filter(user=self.request.user)

    def get_context_data(self, *args, **kwargs):
        context = super(DiligenceRoomUpdateView, self).get_context_data(*args, **kwargs)
        context['title'] = "Update Diligence Room"
        full_context = try_get_context(context, self.request.user)
        return full_context