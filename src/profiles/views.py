from django.contrib.auth import get_user_model
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .forms import SMEForm, StaffForm
from .models import SMEProfile, StaffProfile
from django.contrib.auth.mixins import LoginRequiredMixin

User = get_user_model()

class ProfileListView(ListView):
    def get_queryset(self):
        return SMEProfile.objects.filter(user=self.request.user)

class SMEProfileDetailView(DetailView):
    def get_queryset(self):
        return SMEProfile.objects.filter(user=self.request.user)


class StaffProfileDetailView(DetailView):
    def get_queryset(self):
        return StaffProfile.objects.filter(user=self.request.user)

class SMEProfileCreateView(LoginRequiredMixin, CreateView):
    template_name = 'forms/create_form.html'
    form_class = SMEForm

    def get_queryset(self):
        return SMEProfile.objects.filter(user=self.request.user)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        return super(SMEProfileCreateView, self).form_valid(form)

    def get_context_data(self, *args, **kwargs):
        context = super(SMEProfileCreateView, self).get_context_data(*args, **kwargs)
        context['title'] = "Create a basic profile"
        return context

class StaffProfileCreateView(LoginRequiredMixin, CreateView):
    template_name = 'forms/create_form.html'
    form_class = StaffForm

    def get_queryset(self):
        return SMEProfile.objects.filter(user=self.request.user)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        return super(StaffProfileCreateView, self).form_valid(form)

    def get_context_data(self, *args, **kwargs):
        context = super(StaffProfileCreateView, self).get_context_data(*args, **kwargs)
        context['title'] = "Create a basic profile"
        return context

class SMEProfileUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'forms/update_form.html'
    form_class = SMEForm

    def get_queryset(self):
        return SMEProfile.objects.filter(user=self.request.user)

    def get_context_data(self, *args, **kwargs):
        context = super(SMEProfileUpdateView, self).get_context_data(*args, **kwargs)
        context['title'] = "Update Profile"
        return context

class StaffProfileUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'forms/update_form.html'
    form_class = StaffForm

    def get_queryset(self):
        return StaffProfile.objects.filter(user=self.request.user)

    def get_context_data(self, *args, **kwargs):
        context = super(StaffProfileUpdateView, self).get_context_data(*args, **kwargs)
        context['title'] = "Update Profile"
        return context