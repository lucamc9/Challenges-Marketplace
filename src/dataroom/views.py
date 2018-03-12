from django.contrib.auth import get_user_model
from django.views.generic import DetailView, CreateView, UpdateView, TemplateView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from businessplan.utils import try_get_context
from .forms import DataRoomForm
from .utils import save_dataroom_models

User = get_user_model()

class RedirectView(LoginRequiredMixin, TemplateView):
    template_name = 'redirect_view.html'

    def get_context_data(self, *args, **kwargs):
        context = super(RedirectView, self).get_context_data(*args, **kwargs)
        full_context = try_get_context(context, self.request.user)
        return full_context

class DataRoomFormView(FormView):
    form_class = DataRoomForm
    template_name = 'room_create_form.html'
    success_url = '#'
    sub_area = None

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        if form.is_valid():
            questions_dict = form.get_model_questions()
            for field_name, question in questions_dict.items():
                files = request.FILES.getlist(field_name)
                save_dataroom_models(files, request.user, question, self.sub_area)
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def get_form_kwargs(self):
        kwargs = super(DataRoomFormView, self).get_form_kwargs()
        kwargs.update({'sub_area': self.sub_area})
        return kwargs
