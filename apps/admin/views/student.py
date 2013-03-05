from django.views.generic import ListView, UpdateView
from django.conf import settings
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404

from common.views import LoginRequiredMixin
from repo.models import Student
from repo.forms import StudentForm


class StudentBase(object):

    def dispatch(self, request, *args, **kwargs):
        student = get_object_or_404(Student, id=self.kwargs['student_pk'])
        self.student = student
        return super(StudentBase, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(StudentBase, self).get_context_data(**kwargs)
        context['student'] = self.student
        return context

class StudentListView(LoginRequiredMixin, ListView):

    model = Student
    template_name = 'admin/student/list.html'
    paginate_by = settings.PAGE_SIZE
    context_object_name = 'students'


class StudentUpdateView(LoginRequiredMixin, UpdateView):

    model = Student
    template_name = 'admin/student/edit.html'
    form_class = StudentForm

    def get_success_url(self):
        return reverse('admin_student_list')
