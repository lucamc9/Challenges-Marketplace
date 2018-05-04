from django.contrib.auth import authenticate, login, get_user_model
from django.views.generic import CreateView, FormView, DetailView
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.utils.http import is_safe_url
from .forms import LoginForm, RegisterForm
from accounts.models import User


def activate_user_view(request, code=None, *args, **kwargs):
    if code:
        qs = User.objects.filter(activation_key=code)
        if qs.exists() and qs.count() == 1:
            account = qs.first()
            if not account.active:
                user_ = account.user
                user_.is_active = True
                user_.save()
                account.active = True
                account.activation_key = None
                account.save()
                return redirect("/login")
    return redirect("/login")

class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = "accounts/register.html"
    success_url = '/profile/sme/create'

class LoginView(FormView):
    form_class = LoginForm
    template_name = 'accounts/login.html'
    success_url = '/profile/'

    def form_valid(self, form):
        request = self.request
        next_ = request.GET.get('next')
        next_post = request.POST.get('next')
        redirect_path = next_ or next_post or None
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            try:
                del request.session['guest_email_id']
            except:
                pass
            if is_safe_url(redirect_path, request.get_host()):
                return redirect(redirect_path)
            else:
                return redirect("/")
        return super(LoginView, self).form_invalid(form)