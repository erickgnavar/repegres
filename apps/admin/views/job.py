from django.views.generic import ListView
from django.conf import settings

from common.views import LoginRequiredMixin
from admin.views.student import StudentBase
from repo.models import Job


class JobListView(LoginRequiredMixin, StudentBase, ListView):

    model = Job
    template_name = 'admin/job/list.html'
    paginate_by = settings.PAGE_SIZE
    context_object_name = 'jobs'

    def get_queryset(self):
        qs = super(JobListView, self).get_queryset()
        qs = qs.filter(student=self.student)
        return qs
