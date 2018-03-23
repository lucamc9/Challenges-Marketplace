from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.views.generic import DetailView, CreateView, UpdateView, TemplateView
from businessplan.utils import try_get_context
from diagnostics.models import Diagnostics
from django.contrib.auth.mixins import LoginRequiredMixin
import os
from django.conf import settings
from django.http import HttpResponse, Http404

class KPIHomeView(LoginRequiredMixin, TemplateView):
    template_name = 'home_view.html'

    def get_context_data(self, *args, **kwargs):
        context = super(KPIHomeView, self).get_context_data(*args, **kwargs)
        full_context = try_get_context(context, self.request.user)
        return full_context