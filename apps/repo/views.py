from django.views.generic.edit import FormView
from django.views.generic import UpdateView, TemplateView
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.conf import settings
from django.core.urlresolvers import reverse

from repo.forms import SignupForm, StudentForm
from repo import tasks
from repo.models import Student, Tmp


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
        return reverse('repo_academic_info', kwargs={'key': self.kwargs['key']})


class AcademicInfoView(TemplateView):

    template_name = 'repo/academic_info.html'
