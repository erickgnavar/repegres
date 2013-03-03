from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.utils.decorators import method_decorator

import json


class LoginRequiredMixin(object):
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(LoginRequiredMixin, self).dispatch(*args, **kwargs)


class JSONResponseMixin(object):

    def render_to_response(self, context):
        return self.get_json_response(self.convert_context_to_json(context))

    def get_json_response(self, content, **kwargs):
        return HttpResponse(content, content_type='application/json', **kwargs)

    def convert_context_to_json(self, context):
        return json.dumps(context)


class AccessMixin(object):  # TODO finish

    role = None

    def dispatch(self, request, *args, **kwargs):
        if self.role is None:
            return super(AccessMixin, self).dispatch(request, *args, **kwargs)
        if self.role.objects.filter(user=request.user).count():
            return super(AccessMixin, self).dispatch(request, *args, **kwargs)
        else:
            return HttpResponse('Hola')
