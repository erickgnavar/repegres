from django.conf.urls import patterns, url

from repo.views import HomeView

urlpatterns = patterns('',

    url(r'^$', HomeView.as_view(), name='repo_home')

)
