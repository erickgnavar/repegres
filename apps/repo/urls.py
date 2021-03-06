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
    url(r'^academic_info/(?P<key>\w+)/certification/create/$', repo.CertificationCreateView.as_view(), name='repo_certification_create'),
    url(r'^confirm_data/(?P<key>\w+)/$', repo.ConfirmDataView.as_view(), name='repo_confirm_data'),
    url(r'^save_data/(?P<key>\w+)/$', repo.SaveDataView.as_view(), name='repo_save_data'),
    url(
        r'linkedin/request/',
        repo.LinkedinRequestView.as_view(),
        name='repo_linkedin_request'
    ),
    url(
        r'linkedin/success/',
        repo.LinkedinSuccessView.as_view(),
        name='repo_linkedin_success'
    ),
    url(
        r'linkedin/cancel/',
        repo.LinkedinCancelView.as_view(),
        name='repo_linkedin_cancel'
    ),

)
