from django import forms

from repo.models import Student, Job, Language, Certification


class SignupForm(forms.Form):

    code = forms.CharField(
        max_length=8,
    )

    def clean_code(self):
        code = self.cleaned_data['code']
        try:
            int(code)
            if Student.objects.filter(code=code).count():
                raise forms.ValidationError('Code registered previously')
            return code
        except ValueError:
            raise forms.ValidationError('Code does\'nt format required')


class StudentForm(forms.ModelForm):

    class Meta:
        model = Student
        exclude = ('languages', )

    def __init__(self, *args, **kwargs):
        super(StudentForm, self).__init__(*args, **kwargs)
        self.fields['join_date'].widget.attrs['class'] = 'datepicker'
        self.fields['departure_date'].widget.attrs['class'] = 'datepicker'
        self.fields['graduation_date'].widget.attrs['class'] = 'datepicker'


class JobForm(forms.ModelForm):

    class Meta:
        model = Job

    def __init__(self, *args, **kwargs):
        super(JobForm, self).__init__(*args, **kwargs)
        self.fields['beginning_date'].widget.attrs['class'] = 'datepicker'
        self.fields['end_date'].widget.attrs['class'] = 'datepicker'


class LanguageForm(forms.ModelForm):

    class Meta:
        model = Language


class CertificationForm(forms.ModelForm):

    class Meta:
        model = Certification
