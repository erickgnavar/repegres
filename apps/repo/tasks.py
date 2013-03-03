from uuid import uuid4

from celery.task import task

from common.mail import Email


@task
def send_email(*args, **kwargs):
    data_email = {
        'context': {
            'key': uuid4().hex
        },
        'template_name': 'repo/email/register.html',
        'subject': 'Register Successfully',
        'to': [kwargs['email']]
    }
    Email.send_email(**data_email)
    print 'hello', kwargs['email']
