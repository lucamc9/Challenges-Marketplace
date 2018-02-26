# from django.contrib.auth import get_user_model
# from django.views.generic import DetailView, CreateView, UpdateView, TemplateView
#
# from django.contrib.auth.mixins import LoginRequiredMixin
# from businessplan.utils import try_get_context
#
# User = get_user_model()

# class RoomDetailView(DetailView):
#     def get_queryset(self):
#         return Room.objects.filter(user=self.request.user)
#
#     def get_context_data(self, *args, **kwargs):
#         context = super(RoomDetailView, self).get_context_data(*args, **kwargs)
#         full_context = try_get_context(context, self.request.user)
#         return full_context

# class RoomCreateView(LoginRequiredMixin, CreateView):
#     template_name = 'forms/room_create_form.html'
#     form_class = RoomForm
#
#     def get_queryset(self):
#         return Room.objects.filter(user=self.request.user)
#
#     def form_valid(self, form):
#         obj = form.save(commit=False)
#         obj.user = self.request.user
#         return super(RoomCreateView, self).form_valid(form)
#
#     def get_context_data(self, *args, **kwargs):
#         context = super(RoomCreateView, self).get_context_data(*args, **kwargs)
#         context['title'] = "Create Data Room"
#         full_context = try_get_context(context, self.request.user)
#         return full_context

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