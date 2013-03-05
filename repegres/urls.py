from django.conf.urls import patterns, include, url

handler404 = 'repo.views.handler_404'


urlpatterns = patterns('',
    url(r'^', include('accounts.urls')),
    url(r'^', include('repo.urls')),
    url(r'^admin/', include('admin.urls'))
)
