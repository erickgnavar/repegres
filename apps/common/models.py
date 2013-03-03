class Seeker(object):

    model = None

    def seek(self, *args, **kwargs):
        if self.model is not None:
            result = self.model.objects.filter(**kwargs)
        else:
            raise SeekerException('model doesn\'t assigned')
        return result


class SeekerException(Exception):
    pass
