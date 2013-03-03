from celery.task import task

from common.mail import Email


@task(name='send_email')
def send_email(*args, **kwargs):
    Email.send_email(**kwargs)
    print 'Email sent to %s' % kwargs['to']
