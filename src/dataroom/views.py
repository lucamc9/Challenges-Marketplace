from django.contrib.auth import get_user_model
from django.views.generic import DetailView, CreateView, UpdateView, TemplateView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from businessplan.utils import try_get_context
from .forms import DataRoomForm
from .utils import add_accordion_context
from .models import Accordion, AccordionFileModel

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

    def get_context_data(self, *args, **kwargs):
        context = super(DataRoomFormView, self).get_context_data(*args, **kwargs)
        full_context = try_get_context(context, self.request.user)
        return full_context

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        if form.is_valid():
            questions_dict = form.get_model_questions()
            if not Accordion.objects.filter(user=request.user).exists():
                accordion = Accordion(user=request.user)
                accordion.save()
            else:
                accordion = Accordion.objects.get(user=request.user)
            for field_name, question in questions_dict.items():
                files = request.FILES.getlist(field_name)
                for file in files:
                    model = AccordionFileModel(user=request.user, file=file, label=question, accordion=accordion, sub_area=self.sub_area)
                    model.save()
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def get_form_kwargs(self):
        kwargs = super(DataRoomFormView, self).get_form_kwargs()
        kwargs.update({'sub_area': self.sub_area})
        return kwargs

class DataRoomDetailView(DetailView):

    def get_queryset(self):
        return Accordion.objects.filter(user=self.request.user)

    def get_context_data(self, *args, **kwargs):
        context = super(DataRoomDetailView, self).get_context_data(*args, **kwargs)
        full_context = try_get_context(context, self.request.user)
        full_context = add_accordion_context(full_context, self.request.user)
        return full_context
