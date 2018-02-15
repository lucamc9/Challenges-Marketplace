from django.conf.urls import url
from .views import (
    BusinessPlanDetailView,
    BusinessPlanCreateView,
    BusinessPlanUpdateView,
    download
)
from django.views.static import serve
from django.conf import settings

urlpatterns = [
    url(r'^$', BusinessPlanCreateView.as_view(), name='create'),
    url(r'^(?P<slug>[\w-]+)/update/$', BusinessPlanUpdateView.as_view(), name='update'),
    url(r'^(?P<slug>[\w-]+)/$', BusinessPlanDetailView.as_view(), name='detail'),
    #url(r'^download/(?P<path>.*)$', download)
]