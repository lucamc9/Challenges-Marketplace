from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.views.generic import DetailView

User = get_user_model()

class ProfileDetailView(DetailView):
    queryset = User.objects.filter(is_active=True)