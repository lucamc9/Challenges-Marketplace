from django.conf.urls import url
from .views import (
    KPIHomeView,
    KPIDemoView,
    get_data
)

urlpatterns = [
    url(r'^$', KPIHomeView.as_view(), name='home'),
    url(r'^(?P<slug>[\w-]+)/$', KPIDemoView.as_view(), name='detail'),
    url(r'^(?P<slug>[\w-]+)/api/data/$', get_data, name='api-data'),
]