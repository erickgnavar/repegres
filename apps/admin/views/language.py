from django.views.generic import ListView
from django.conf import settings

from common.views import LoginRequiredMixin
from repo.models import Language
from admin.views.student import StudentBase


class LanguageListView(LoginRequiredMixin, StudentBase, ListView):

    model = Language
    template_name = 'admin/language/list.html'
    paginate_by = settings.PAGE_SIZE
    context_object_name = 'languages'

    def get_queryset(self):
        qs = super(LanguageListView, self).get_queryset()
        qs = qs.filter(student=self.student)
        return qs
