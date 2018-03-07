from django.conf.urls import url
from django.views.generic import TemplateView
from .views import (
    RoomCreateView,
)

urlpatterns = [
    url(r'^$', RoomCreateView.as_view(), name='create'),
#     url(r'^(?P<slug>[\w-]+)/$', RoomDetailView.as_view(), name='detail'),
]