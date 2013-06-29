from uuid import uuid4

from celery.task import task
from django.core.urlresolvers import reverse

from common.mail import Email
from repo.models import Student, Tmp


@task
def signup_email(*args, **kwargs):
    code = kwargs['email'].split('@')[0]
    key = uuid4().hex
    student = Student()
    student.key = key
    student.code = code
    student.save()
    tmp = Tmp()
    tmp.student = student
    tmp.key = key
    tmp.save()
    data_email = {
        'context': {
            'key': key,
            'host': kwargs['host']
        },
        'template_name': 'repo/email/register.html',
        'subject': 'Register Successfully',
        'to': [kwargs['email']]
    }
    print reverse('repo_personal_info', kwargs={'key': tmp.key})
    print 'email sent to %s' % kwargs['email']
    Email.send_email(**data_email)


@task
def resume_email(*args, **kwargs):
    student = kwargs['student']
    emails = [student.email, '%s@unmsm.edu.pe' % student.code]
    data_email = {
        'context': {
            'student': student
        },
        'template_name': 'repo/email/resume.html',
        'subject': 'Register Complete',
        'to': emails
    }
    Email.send_email(**data_email)
    print 'email sent to: ' + str(emails)

