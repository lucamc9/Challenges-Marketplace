from django.contrib.auth import get_user_model
from django.views.generic import DetailView, CreateView, UpdateView, TemplateView
from .forms import BusinessPlanForm
from .models import BusinessPlan
from django.contrib.auth.mixins import LoginRequiredMixin

User = get_user_model()

class BusinessPlanDetailView(TemplateView):
    template_name = 'businessplan_detail.html'
    def get_queryset(self):
        return BusinessPlan.objects.filter(user=self.request.user)

class BusinessPlanCreateView(LoginRequiredMixin, CreateView):
    template_name = 'forms/bp_create_form.html'
    form_class = BusinessPlanForm
    success_url = '/businessplan/'

    def get_queryset(self):
        return BusinessPlan.objects.filter(user=self.request.user)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        return super(BusinessPlanCreateView, self).form_valid(form)

    def get_context_data(self, *args, **kwargs):
        context = super(BusinessPlanCreateView, self).get_context_data(*args, **kwargs)
        context['title'] = "Create a business plan"
        return context

class BusinessPlanUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'forms/update_form.html'
    form_class = BusinessPlanForm

    def get_queryset(self):
        return BusinessPlan.objects.filter(user=self.request.user)

    def get_context_data(self, *args, **kwargs):
        context = super(BusinessPlanUpdateView, self).get_context_data(*args, **kwargs)
        context['title'] = "Update Business Plan"
        return context

class InfoView(LoginRequiredMixin, TemplateView):
    template_name = 'info_view.html'
