from django.views.generic.edit import FormView
from django.contrib import messages

from repo.forms import SignupForm
from repo import tasks


class HomeView(FormView):

    template_name = 'repo/home.html'
    form_class = SignupForm
    email_base = '@unmsm.edu.pe'

    def form_valid(self, form):
        code = form.cleaned_data['code']
        email = code + self.email_base
        tasks.send_email.delay(email=email)
        messages.success(self.request, 'A message will be sent your email')
        return super(HomeView, self).form_valid(form)

    def get_success_url(self):
        return '/'
