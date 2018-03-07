from django.conf.urls import url
from django.views.generic import TemplateView
# from .views import (
#     RoomDetailView,
#     RoomCreateView,
# )

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name="forms/room_create_form.html")),
#     url(r'^(?P<slug>[\w-]+)/$', RoomDetailView.as_view(), name='detail'),
]