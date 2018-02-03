from django.conf.urls import url
from .views import (
    BusinessPlanDetailView,
    BusinessPlanCreateView,
    BusinessPlanUpdateView
)

urlpatterns = [
    url(r'^$', BusinessPlanDetailView.as_view(), name='detail'),
    url(r'^create/$', BusinessPlanCreateView.as_view(), name='create'),
    url(r'^update/$', BusinessPlanUpdateView.as_view(), name='update'),
]