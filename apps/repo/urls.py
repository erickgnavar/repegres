from django.conf.urls import patterns, url

from repo.views import HomeView, PersonalInfoView, AcademicInfoView

urlpatterns = patterns('',

    url(r'^$', HomeView.as_view(), name='repo_home'),
    url(r'^personal_info/(?P<key>\w+)/$', PersonalInfoView.as_view(), name='repo_personal_info'),
    url(r'^academic_info/(?P<key>\w+)/$', AcademicInfoView.as_view(), name='repo_academic_info')

)
