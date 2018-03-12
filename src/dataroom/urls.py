from django.conf.urls import url
from django.views.generic import TemplateView
from .views import (
    RedirectView,
    DataRoomFormView
)


urlpatterns = [
    url(r'^$', RedirectView.as_view(), name='redirect'),
    url(r'^compliance-form/$', DataRoomFormView.as_view(sub_area='Compliance'), name='compliance'),
    url(r'^legal-form/$', DataRoomFormView.as_view(sub_area='Legal'), name='compliance'),
#     url(r'^(?P<slug>[\w-]+)/$', RoomDetailView.as_view(), name='detail'),
]