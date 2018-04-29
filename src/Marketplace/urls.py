from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.views import logout
from django.views.generic import TemplateView
from accounts.views import RegisterView, LoginView
from profiles.views import SearchSMEView, HomePageView
from businessplan.views import InfoView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', HomePageView.as_view(), name='base_home'),
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^logout/$', logout, {'next_page': '/login/'}, name='logout'),
    url(r'^register/$', RegisterView.as_view(), name='register'),
    url(r'^info/(?P<slug>[\w-]+)/$', InfoView.as_view(), name='info'),
    url(r'^profile/', include('profiles.urls', namespace='profiles')),
    url(r'^businessplan/', include('businessplan.urls', namespace='businessplan')),
    url(r'^diagnostics/', include('diagnostics.urls', namespace='diagnostics')),
    url(r'^dataroom/', include('dataroom.urls', namespace='accordion')),
    url(r'^diligenceroom/', include('diligence.urls', namespace='diligence')),
    url(r'^kpi/', include('kpi.urls', namespace='kpi')),
    url(r'^search-companies/', SearchSMEView.as_view(), name='search-companies')
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

