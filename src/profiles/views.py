from django.contrib.auth import get_user_model
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.http import Http404
from .forms import SMEForm
from .models import SMEProfile
from django.contrib.auth.mixins import LoginRequiredMixin

User = get_user_model()

class ProfileListView(ListView):
    def get_queryset(self):
        return SMEProfile.objects.filter(user=self.request.user)

class ProfileDetailView(DetailView):
    def get_queryset(self):
        return SMEProfile.objects.filter(user=self.request.user)

class ProfileCreateView(LoginRequiredMixin, CreateView):
    form_class = SMEForm

    def get_queryset(self):
        return SMEProfile.objects.filter(user=self.request.user)

class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'update_form.html'
    form_class = SMEForm

    def get_queryset(self):
        return SMEProfile.objects.filter(user=self.request.user)

    def get_context_data(self, *args, **kwargs):
        context = super(ProfileUpdateView, self).get_context_data(*args, **kwargs)
        context['title'] = "Update Profile"
        return context