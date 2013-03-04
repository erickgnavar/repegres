from django.db import models
from django.utils.translation import ugettext_lazy as _


class Language(models.Model):

    ENGLISH = 1
    SPANISH = 2
    FRENCH = 3

    BASIC = 1
    MEDIUM = 2
    ADVANCED = 3

    NAME_CHOICES = (
        (ENGLISH, 'English'),
        (SPANISH, 'Spanish'),
        (FRENCH, 'French'),
    )

    LEVEL_CHOICES = (
        (BASIC, 'Basic'),
        (MEDIUM, 'Medium'),
        (ADVANCED, 'Advanced'),
    )

    name = models.CharField(
        _('Name'),
        max_length=20,
        choices=NAME_CHOICES,
        default=SPANISH
    )
    level = models.IntegerField(
        _('Level'),
        choices=LEVEL_CHOICES,
        default=BASIC
    )

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        app_label = 'repo'


class Student(models.Model):

    code = models.CharField(
        _('Code'),
        max_length=8,
        editable=False,
        unique=True
    )
    first_name = models.CharField(
        _('First Name'),
        max_length=200,
        default='',
        null=True
    )
    last_name = models.CharField(
        _('Last Name'),
        max_length=200,
        default='',
        null=True
    )
    address = models.CharField(
        _('Address'),
        max_length=400,
        null=True
    )
    phone = models.CharField(
        _('Phone'),
        max_length=10,
        null=True
    )
    mobile_phone = models.CharField(
        _('Mobile Phone'),
        max_length=10,
        null=True
    )
    email = models.EmailField(
        _('Email'),
        max_length=100,
        null=True
    )
    join_date = models.DateField(
        _('Join Date'),
        null=True
    )
    departure_date = models.DateField(
        _('Departure Date'),
        null=True
    )
    graduation_date = models.DateField(
        _('Graduation Date'),
        null=True
    )
    languages = models.ManyToManyField(
        'Language',
        null=True
    )

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        app_label = 'repo'


class Tmp(models.Model):

    key = models.CharField(
        _('Key'),
        max_length=100,
        unique=True
    )
    student = models.OneToOneField(
        'Student'
    )

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        app_label = 'repo'


class Job(models.Model):

    student = models.ForeignKey(
        'Student',
        related_name='job_set'
    )
    company = models.CharField(
        _('Company'),
        max_length=100
    )
    position = models.CharField(
        _('Position'),
        max_length=100
    )
    place = models.CharField(
        _('Place'),
        max_length=100
    )
    beginning_date = models.DateField(
        _('Beginning')
    )
    end_date = models.DateField(
        _('End')
    )

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        app_label = 'repo'


class Certification(models.Model):

    student = models.ForeignKey(
        'Student',
        related_name='certification_set'
    )
    name = models.CharField(
        _('Name'),
        max_length=100
    )
    year = models.IntegerField(
        _('Year')
    )
    institution = models.CharField(
        _('Institution'),
        max_length=100
    )

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        app_label = 'repo'
