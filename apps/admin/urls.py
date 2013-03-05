from django.conf.urls import patterns, url

from admin.views import HomeView
from admin.views import student as s
from admin.views import language as l
from admin.views import job as j
from admin.views import certification as c

urlpatterns = patterns('',
    url(r'^$', HomeView.as_view(), name='admin_home'),
    url(r'^students/$', s.StudentListView.as_view(), name='admin_student_list'),
    url(
        regex=r'^student/(?P<pk>\d+)/edit/$',
        view=s.StudentUpdateView.as_view(),
        name='admin_student_edit'
    ),
    url(
        regex=r'^student/(?P<student_pk>\d+)/languages/$',
        view=l.LanguageListView.as_view(),
        name='admin_language_list'
    ),
    url(
        regex=r'^student/(?P<student_pk>\d+)/jobs/$',
        view=j.JobListView.as_view(),
        name='admin_job_list'
    ),
    url(
        regex=r'^student/(?P<student_pk>\d+)/certifications/$',
        view=c.CertificationListView.as_view(),
        name='admin_certification_list'
    ),

)
