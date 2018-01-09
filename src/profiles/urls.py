from django.conf.urls import url
from .views import (
    ProfileListView,
    ProfileDetailView,
    ProfileCreateView,
    ProfileUpdateView
)

urlpatterns = [
    url(r'^$', ProfileListView.as_view(), name='list'),
    url(r'^create/$', ProfileCreateView.as_view(), name='create'),
    url(r'^(?P<slug>[\w-]+)/update/$', ProfileUpdateView.as_view(), name='update'),
    url(r'^(?P<slug>[\w-]+)/$', ProfileDetailView.as_view(), name='detail'),
]