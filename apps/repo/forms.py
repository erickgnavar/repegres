from django import forms


class SignupForm(forms.Form):

    code = forms.CharField(
        max_length=8,
        label='Codigo'
    )
