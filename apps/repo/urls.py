from django.conf.urls import patterns, url

from repo.views import HomeView, PersonalInfoView, LanguageListView, LanguageCreateView

urlpatterns = patterns('',

    url(r'^$', HomeView.as_view(), name='repo_home'),
    url(r'^personal_info/(?P<key>\w+)/$', PersonalInfoView.as_view(), name='repo_personal_info'),
    url(r'^academic_info/(?P<key>\w+)/languages/$', LanguageListView.as_view(), name='repo_language_list'),
    url(r'^academic_info/(?P<key>\w+)/languages/create/$', LanguageCreateView.as_view(), name='repo_language_create')

)
