from django.contrib.auth import get_user_model
from django.views.generic import DetailView, CreateView, UpdateView, TemplateView, FormView
from .forms import RoomForm, CompetitionForm, ComplianceForm, LegalForm, FinanceForm
from django.contrib.auth.mixins import LoginRequiredMixin
from businessplan.utils import try_get_context

User = get_user_model()

# class RoomDetailView(DetailView):
#     def get_queryset(self):
#         return Room.objects.filter(user=self.request.user)
#
#     def get_context_data(self, *args, **kwargs):
#         context = super(RoomDetailView, self).get_context_data(*args, **kwargs)
#         full_context = try_get_context(context, self.request.user)
#         return full_context

class RoomCreateView(LoginRequiredMixin, FormView):
    template_name = 'forms/room_create_form.html'
    form_class = RoomForm

    # def get_queryset(self):
    #     return Competition.objects.filter(user=self.request.user)

    def form_valid(self, form):
        # compliance = form['compliance'].save(commit=False)
        # finance = form['finance'].save(commit=False)
        # legal = form['legal'].save(commit=False)
        # competition = form['competition'].save(commit=False)
        # compliance.user = self.request.user
        # finance.user = self.request.user
        # legal.user = self.request.user
        # competition.user = self.request.user
        obj = form.save(commit=False)
        obj.user = self.request.user
        return super(RoomCreateView, self).form_valid(form)

    # def get_context_data(self, *args, **kwargs):
    #     context = super(RoomCreateView, self).get_context_data(*args, **kwargs)
    #     context['title'] = "Create Data Room"
    #     full_context = try_get_context(context, self.request.user)
    #     return full_context

    # def post(self, request, *args, **kwargs):
    #     form_class = self.get_form_class()
    #     form = self.get_form(form_class)
    #     files = request.FILES.getlist('file')
    #     if form.is_valid():
    #         for f in files:
    #             print(f)
    #         return self.form_valid(form)
    #     else:
    #         return self.form_invalid(form)

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