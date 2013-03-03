from django import forms
from django.contrib.auth import get_user_model

from crispy_forms.helper import FormHelper


class UserForm(forms.ModelForm):

    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput
    )
    password2 = forms.CharField(
        label='Password Confirmation',
        widget=forms.PasswordInput
    )

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Password don\'t match')
        return password2

    def save(self, commit=True):
        user = super(UserForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user

    class Meta:
        model = get_user_model()
        exclude = ('password', 'last_login')


class LoginForm(forms.Form):

    email = forms.EmailField(
        required=True
    )
    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput()
    )

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_show_errors = True
        super(LoginForm, self).__init__(*args, **kwargs)


class RegisterForm(forms.Form):

    first_name = forms.CharField(
        label='First Name',
        max_length=100
    )
    last_name = forms.CharField(
        label='Last Name',
        max_length=100
    )
    email = forms.EmailField(
        label='Email'
    )

    def clean_email(self):
        email = self.cleaned_data.get('email')
        User = get_user_model()
        if User.objects.filter(email=email).count():
            raise forms.ValidationError('Email exists')
        return email


class ChangePasswordForm(forms.Form):

    current_password = forms.CharField(
        label='Current Password',
        max_length=100,
        widget=forms.PasswordInput()
    )
    new_password = forms.CharField(
        label='New Password',
        max_length=100,
        widget=forms.PasswordInput()
    )
    confirm_password = forms.CharField(
        label='Confirm Password',
        max_length=100,
        widget=forms.PasswordInput()
    )

    def clean_confirm_password(self):
        new_password = self.cleaned_data.get('new_password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if confirm_password != new_password:
            raise forms.ValidationError('Password doesn\'t match')
        return confirm_password


class ResetPasswordForm(forms.Form):

    email = forms.EmailField(
        label='Email',
        max_length=200
    )
