from django.conf.urls import patterns, url

from repo import views as repo

urlpatterns = patterns('',

    url(r'^$', repo.HomeView.as_view(), name='repo_home'),
    url(r'^personal_info/(?P<key>\w+)/$', repo.PersonalInfoView.as_view(), name='repo_personal_info'),
    url(r'^academic_info/(?P<key>\w+)/languages/$', repo.LanguageListView.as_view(), name='repo_language_list'),
    url(r'^academic_info/(?P<key>\w+)/languages/create/$', repo.LanguageCreateView.as_view(), name='repo_language_create'),
    url(r'^academic_info/(?P<key>\w+)/jobs/$', repo.JobListView.as_view(), name='repo_job_list'),
    url(r'^academic_info/(?P<key>\w+)/jobs/create/$', repo.JobCreateView.as_view(), name='repo_job_create'),
    url(r'^academic_info/(?P<key>\w+)/certifications/$', repo.CertificationListView.as_view(), name='repo_certification_list'),
    url(r'^academic_info/(?P<key>\w+)/certification/create/$', repo.CertificationCreateView.as_view(), name='repo_certification_create')

)
