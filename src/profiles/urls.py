from django.conf.urls import url
from .views import ProfileDetailView
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^(?P<slug>[\w-]+)/$', ProfileDetailView.as_view(), name='detail'),
]