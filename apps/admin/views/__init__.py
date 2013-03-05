from django.views.generic import TemplateView

from common.views import LoginRequiredMixin


class HomeView(LoginRequiredMixin, TemplateView):

    template_name = 'admin/home.html'

