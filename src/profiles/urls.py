from django.conf.urls import url
from .views import (
    ProfileListView,
    SMEProfileDetailView,
    StaffProfileDetailView,
    SMEProfileCreateView,
    StaffProfileCreateView,
    SMEProfileUpdateView,
    StaffProfileUpdateView
)

urlpatterns = [
    url(r'^$', ProfileListView.as_view(), name='list'),
    url(r'^create-sme/$', SMEProfileCreateView.as_view(), name='create-sme'),
    url(r'^create-staff/$', StaffProfileCreateView.as_view(), name='create-staff'),
    url(r'^(?P<slug>[\w-]+)/update-sme/$', SMEProfileUpdateView.as_view(), name='update-sme'),
    url(r'^(?P<slug>[\w-]+)/update-staff/$', StaffProfileUpdateView.as_view(), name='update-staff'),
    url(r'^sme/(?P<slug>[\w-]+)/$', SMEProfileDetailView.as_view(), name='detail-sme'),
    url(r'^staff/(?P<slug>[\w-]+)/$', StaffProfileDetailView.as_view(), name='detail-staff'),
]