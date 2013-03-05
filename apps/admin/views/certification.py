from django.views.generic import ListView
from django.conf import settings

from common.views import LoginRequiredMixin
from admin.views.student import StudentBase
from repo.models import Certification


class CertificationListView(LoginRequiredMixin, StudentBase, ListView):

    model = Certification
    template_name = 'admin/certification/list.html'
    paginate_by = settings.PAGE_SIZE
    context_object_name = 'certifications'

    def get_queryset(self):
        qs = super(CertificationListView, self).get_queryset()
        qs = qs.filter(student=self.student)
        return qs
