from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    url(r'^', include('accounts.urls')),
    url(r'^', include('repo.urls')),
)
