from django.conf.urls import url, include
from . import views
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CreateView, DetailsView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    url(r'^$', views.start, name='start'),
    url(r'^cat/$', views.cat, name='cat'),
    url(r'^badges/$', views.badges, name='badges'),
    url(r'^header/$', views.header, name='header'),
    url(r'^patient/$', views.patient, name='patient'),
    url(r'^schedule_prompt/$', views.schedule_prompt, name='schedule_prompt'),
    url(r'^provider/$', views.provider, name='provider'),
    url(r'^home/$', views.home, name='home'),
    url(r'^group/$', views.age_groups, name='age_groups'),
    url(r'^vaccinelists/$', CreateView.as_view(), name="create"),
    url(r'^vaccinelists/(?P<pk>[0-9]+)/$', DetailsView.as_view(), name="details"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
