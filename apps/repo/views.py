from django.views.generic.edit import FormView
from django.views.generic import UpdateView, DetailView, ListView, CreateView, RedirectView
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.conf import settings
from django.core.urlresolvers import reverse
from django import forms

from repo.forms import SignupForm, StudentForm, LanguageForm, JobForm, CertificationForm
from repo import tasks
from repo.models import Student, Tmp, Language, Certification, Job


class HomeView(FormView):

    template_name = 'repo/home.html'
    form_class = SignupForm
    email_base = '@unmsm.edu.pe'

    def form_valid(self, form):
        code = form.cleaned_data['code']
        email = code + self.email_base
        tasks.send_email.delay(email=email, host=settings.SITE_URL)
        messages.success(self.request, 'A message will be sent your email')
        return super(HomeView, self).form_valid(form)

    def get_success_url(self):
        return '/'


class PersonalInfoView(UpdateView):

    model = Student
    template_name = 'repo/personal_info.html'
    form_class = StudentForm

    def get_object(self, queryset=None):
        key = self.kwargs['key']
        tmp = get_object_or_404(Tmp, key=key)
        return tmp.student

    def get_success_url(self):
        return reverse('repo_language_list', kwargs={'key': self.kwargs['key']})


class AcademicBase(object):

    def dispatch(self, request, *args, **kwargs):
        key = self.kwargs['key']
        tmp = get_object_or_404(Tmp, key=key)
        self.student = tmp.student
        self.key = key
        return super(AcademicBase, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(AcademicBase, self).get_context_data(**kwargs)
        context['student'] = self.student
        context['key'] = self.key
        return context


class LanguageListView(AcademicBase, ListView):

    template_name = 'repo/language/list.html'
    model = Language
    paginate_by = settings.PAGE_SIZE
    context_object_name = 'languages'

    def get_queryset(self):
        qs = super(LanguageListView, self).get_queryset()
        qs = qs.filter(student=self.student)
        return qs


class LanguageCreateView(AcademicBase, CreateView):

    template_name = 'repo/language/create.html'
    model = Language
    form_class = LanguageForm

    def get_form(self, form_class):
        form = super(LanguageCreateView, self).get_form(form_class)
        form.fields['student'].initial = self.student
        form.fields['student'].widget = forms.HiddenInput()
        return form

    def get_success_url(self):
        return reverse('repo_language_list', kwargs={'key': self.key})


class JobListView(AcademicBase, ListView):

    template_name = 'repo/job/list.html'
    model = Job
    paginate_by = settings.PAGE_SIZE
    context_object_name = 'jobs'

    def get_queryset(self):
        qs = super(JobListView, self).get_queryset()
        qs = qs.filter(student=self.student)
        return qs


class JobCreateView(AcademicBase, CreateView):

    template_name = 'repo/job/create.html'
    model = Job
    form_class = JobForm

    def get_form(self, form_class):
        form = super(JobCreateView, self).get_form(form_class)
        form.fields['student'].initial = self.student
        form.fields['student'].widget = forms.HiddenInput()
        return form

    def get_success_url(self):
        return reverse('repo_job_list', kwargs={'key': self.key})


class CertificationListView(AcademicBase, ListView):

    template_name = 'repo/certification/list.html'
    model = Certification
    paginate_by = settings.PAGE_SIZE
    context_object_name = 'certifications'

    def get_queryset(self):
        qs = super(CertificationListView, self).get_queryset()
        qs = qs.filter(student=self.student)
        return qs


class CertificationCreateView(AcademicBase, CreateView):

    template_name = 'repo/certification/create.html'
    model = Certification
    form_class = CertificationForm

    def get_form(self, form_class):
        form = super(CertificationCreateView, self).get_form(form_class)
        form.fields['student'].initial = self.student
        form.fields['student'].widget = forms.HiddenInput()
        return form

    def get_success_url(self):
        return reverse('repo_certification_list', kwargs={'key': self.key})


class ConfirmDataView(AcademicBase, DetailView):

    template_name = 'repo/resume.html'
    model = Student

    def get_object(self, queryset=None):
        return self.student


class SaveDataView(AcademicBase, RedirectView):

    permanent = False

    def get_redirect_url(self, key):
        messages.success(self.request, 'Data complete!')
        return '/'
