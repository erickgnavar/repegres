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
        unique=True
    )
    first_name = models.CharField(
        _('First Name'),
        max_length=200,
        default=''
    )
    last_name = models.CharField(
        _('Last Name'),
        max_length=200,
        default=''
    )
    address = models.CharField(
        _('Address'),
        max_length=400
    )
    phone = models.CharField(
        _('Phone'),
        max_length=10
    )
    mobile_phone = models.CharField(
        _('Mobile Phone'),
        max_length=10
    )
    email = models.EmailField(
        _('Email'),
        max_length=100
    )
    join_date = models.DateField(
        _('Join Date')
    )
    departure_date = models.DateField(
        _('Departure Date')
    )
    graduation_date = models.DateField(
        _('Graduation Date')
    )
    languages = models.ForeignKey(
        'Language',
        related_name='student_set'
    )

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        app_label = 'repo'
