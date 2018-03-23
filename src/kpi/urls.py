from django.conf.urls import url
from .views import (
    KPIHomeView
)

urlpatterns = [
    url(r'^$', KPIHomeView.as_view(), name='home'),
]