from django.conf.urls import url
from .views import (
    KPIHomeView,
    KPIDemoView,
    get_data,
    ChartData
)

urlpatterns = [
    url(r'^$', KPIHomeView.as_view(), name='home'),
    url(r'^chart-demo/$', KPIDemoView.as_view(), name='demo'),
    url(r'^chart-demo/api/data/$', get_data, name='api-data'),
    url(r'^chart-demo/api/chart/data/$', ChartData.as_view()),
]