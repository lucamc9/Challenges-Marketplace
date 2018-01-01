from django.conf.urls import url
from .views import ProfileDetailView
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^$', ProfileDetailView.as_view(), name='detail'),
    #url(r'^$', TemplateView.as_view(template_name='profiles/user.html'), name='user')
]