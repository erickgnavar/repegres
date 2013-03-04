from uuid import uuid4

from celery.task import task

from common.mail import Email
from repo.models import Student, Tmp


@task
def send_email(*args, **kwargs):
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
    print 'email sent to %s' % kwargs['email']
    Email.send_email(**data_email)
