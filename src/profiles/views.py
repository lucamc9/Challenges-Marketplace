from django.contrib.auth import get_user_model
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, CreateView
from django.http import Http404

from .models import SMEProfile

User = get_user_model()

class ProfileDetailView(DetailView):
    template_name = 'profiles/user.html'

    # def get_object(self, *args, **kwargs):
    #     email = self.kwargs.get("email")
    #     print(email)
    #     if email is None:
    #         raise Http404
    #     obj = get_object_or_404(User, email__iexact=email, is_active=True)
    #     return obj

    def get_object(self, queryset=None):
        obj = super(ProfileDetailView, self).get_object(queryset=queryset)
        if obj.user != User:
            raise Http404()
        return obj

    def get_queryset(self):
        return SMEProfile.objects.filter(user=self.request.user)