from django.contrib.auth import get_user_model
from django.views.generic import ListView, DetailView, CreateView, UpdateView
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
    template_name = 'forms/create_form.html'
    form_class = SMEForm

    def get_queryset(self):
        return SMEProfile.objects.filter(user=self.request.user)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        return super(ProfileCreateView, self).form_valid(form)

    def get_context_data(self, *args, **kwargs):
        context = super(ProfileCreateView, self).get_context_data(*args, **kwargs)
        context['title'] = "Create a basic profile"
        return context

class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'forms/update_form.html'
    form_class = SMEForm

    def get_queryset(self):
        return SMEProfile.objects.filter(user=self.request.user)

    def get_context_data(self, *args, **kwargs):
        context = super(ProfileUpdateView, self).get_context_data(*args, **kwargs)
        context['title'] = "Update Profile"
        return context