import uuid

from django.conf import settings
from django.contrib import auth
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.core.urlresolvers import reverse
from django.views.generic import RedirectView
from django.views.generic.edit import FormView
from django.http import HttpResponseRedirect

from accounts.forms import LoginForm, RegisterForm, ChangePasswordForm, ResetPasswordForm
from accounts.tasks import send_email
from common.views import LoginRequiredMixin

User = get_user_model()


class LoginView(FormView):

    template_name = 'accounts/login.html'
    form_class = LoginForm

    def form_valid(self, form):
        data = form.cleaned_data
        user = auth.authenticate(
            username=data.get('email', ''),
            password=data.get('password', '')
        )
        if user is not None:
            auth.login(self.request, user)
            self.request.session['store_id'] = 2
            return super(LoginView, self).form_valid(form)
        else:
            messages.error(self.request, 'Email or password is wrong')
            return self.form_invalid(form)

    def get_success_url(self):
        if self.request.GET.get('next'):
            return self.request.GET.get('next')
        return '/'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return HttpResponseRedirect('/')
        else:
            return super(LoginView, self).dispatch(request, *args, **kwargs)


class LogoutView(RedirectView):

    url = settings.LOGIN_URL

    def get(self, request, *args, **kwargs):
        auth.logout(request)
        return super(LogoutView, self).get(request, *args, **kwargs)


class RegisterView(FormView):

    template_name = 'accounts/register.html'
    form_class = RegisterForm

    def form_valid(self, form):
        data = form.cleaned_data
        params = {
            'email': data['email'],
            'first_name': data['first_name'],
            'last_name': data['last_name']
        }
        user = User(**params)
        password = uuid.uuid4().hex
        user.set_password(password)
        user.save()
        user.password = password
        email_data = {
            'to': [user.email],
            'subject': 'Registration Successfully',
            'context': {'user': user},
            'template_name': 'accounts/reset_password.html'
        }
        send_email.delay(**email_data)
        return super(RegisterView, self).form_valid(form)

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return HttpResponseRedirect('/')
        else:
            return super(RegisterView, self).dispatch(request, *args, **kwargs)

    def get_success_url(self):
        messages.success(self.request, 'A email was sent to email address, please check your email!')
        return reverse('login')


class ChangePasswordView(LoginRequiredMixin, FormView):

    template_name = 'accounts/change_password.html'
    form_class = ChangePasswordForm

    def form_valid(self, form):
        data = form.cleaned_data
        current_password = data['current_password']
        if not self.request.user.check_password(current_password):
            messages.error(self.request, 'Current Password incorrect')
            return self.form_invalid(form)
        self.request.user.set_password(data['new_password'])
        self.request.user.save()
        return super(ChangePasswordView, self).form_valid(form)

    def get_success_url(self):
        return '/'


class ResetPasswordView(FormView):

    template_name = 'accounts/reset_password.html'
    form_class = ResetPasswordForm

    def form_valid(self, form):
        email = form.cleaned_data['email']
        try:
            user = User.objects.get(email=email)
            password = uuid.uuid4().hex
            user.set_password(password)
            user.save()
            user.password = password
            email_data = {
                'to': [user.email],
                'subject': 'Reset Password',
                'context': {'user': user},
                'template_name': 'accounts/email/register_notification.html'
            }
            send_email.delay(**email_data)
            return super(ResetPasswordView, self).form_valid(form)
        except:
            messages.error(self.request, 'Email doesn\'t exists')
            return self.form_invalid(form)

    def get_success_url(self):
        messages.success(self.request, 'A email was sent to email address, please check your email!')
        auth.logout(self.request)
        return reverse('login')
