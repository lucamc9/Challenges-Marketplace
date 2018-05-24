from django.conf.urls import url
from .views import (
    KPIHomeView,
    KPIFollowerView,
    KPIBusinessView,
    get_data
)

urlpatterns = [
    url(r'^$', KPIHomeView.as_view(), name='home'),
    url(r'^follower/(?P<slug>[\w-]+)/$', KPIFollowerView.as_view(), name='detail-follower'),
    url(r'^business/(?P<slug>[\w-]+)/$', KPIBusinessView.as_view(), name='detail-business'),
    url(r'^follower/(?P<slug>[\w-]+)/api/data/$', get_data, name='api-f-data'),
    url(r'^business/(?P<slug>[\w-]+)/api/data/$', get_data, name='api-b-data'),
]