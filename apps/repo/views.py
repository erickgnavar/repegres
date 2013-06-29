from linkedin import LinkedinAPI

from django.views.generic.edit import FormView
from django.views.generic import UpdateView, DetailView, ListView, CreateView, RedirectView
from django.contrib import messages
from django.shortcuts import get_object_or_404, render_to_response
from django.conf import settings
from django.core.urlresolvers import reverse

from repo.forms import SignupForm, StudentForm, LanguageForm, JobForm, CertificationForm
from repo import tasks
from repo.models import Student, Tmp, Language, Certification, Job


def handler_404(request):
    print '404'
    return render_to_response('repo/404.html')


class HomeView(FormView):

    template_name = 'repo/home.html'
    form_class = SignupForm
    email_base = '@unmsm.edu.pe'

    def form_valid(self, form):
        code = form.cleaned_data['code']
        email = code + self.email_base
        tasks.signup_email.delay(email=email, host=settings.SITE_URL)
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
        self.request.session['key'] = key
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

    def form_valid(self, form):
        language = form.save(commit=False)
        language.student = self.student
        return super(LanguageCreateView, self).form_valid(form)

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

    def form_valid(self, form):
        job = form.save(commit=False)
        job.student = self.student
        return super(JobCreateView, self).form_valid(form)

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

    def form_valid(self, form):
        certification = form.save(commit=False)
        certification.student = self.student
        return super(CertificationCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse('repo_certification_list', kwargs={'key': self.key})


class ConfirmDataView(AcademicBase, DetailView):

    template_name = 'repo/resume.html'
    model = Student

    def get_object(self, queryset=None):
        self.request.session['key'] = self.kwargs.get('key')
        return self.student


class SaveDataView(AcademicBase, RedirectView):

    permanent = False

    def get_redirect_url(self, key):
        messages.success(self.request, 'Data complete!')
        tasks.resume_email(student=self.student)
        tmp = Tmp.objects.get(key=self.key)
        tasks.resume_email.delay(student=self.student)
        tmp.delete()
        return '/'


class LinkedinRequestView(RedirectView):

    permanent = False

    def get_redirect_url(self, **kwargs):
        success_url = settings.SITE_URL + reverse('repo_linkedin_success')
        permissions = []
        config = {
            'api_key': settings.API_KEY,
            'api_secret': settings.API_SECRET,
            'callback_url': success_url,
            'permissions': permissions
        }
        api = LinkedinAPI(**config)
        auth_props = api.get_authentication_tokens()
        auth_url = auth_props['auth_url']
        self.request.session['oauth_token_secret'] = auth_props['oauth_token_secret']
        return auth_url


class LinkedinSuccessView(RedirectView):

    permanent = False

    def get_redirect_url(self, **kwargs):
        oauth_token = self.request.GET.get('oauth_token')
        oauth_verifier = self.request.GET.get('oauth_verifier')

        config = {
            'api_key': settings.API_KEY,
            'api_secret': settings.API_SECRET,
            'oauth_token': oauth_token,
            'oauth_token_secret': self.request.session['oauth_token_secret']
        }

        l = LinkedinAPI(**config)

        authorized_tokens = l.get_access_token(oauth_verifier)

        final_oauth_token = authorized_tokens['oauth_token']
        final_oauth_token_secret = authorized_tokens['oauth_token_secret']

        key = self.request.session.get('key')
        tmp = Tmp.objects.get(key=key)
        student = tmp.student
        student.linkedin_token = final_oauth_token
        student.linkedin_token_secret = final_oauth_token_secret
        student.save()
        messages.success(self.request, 'Linkedin active')
        return settings.SITE_URL + reverse('repo_confirm_data', kwargs={'key': key})


class LinkedinCancelView(RedirectView):
    pass
