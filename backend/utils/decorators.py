from django.apps import apps


def save_method(fn):
    def wrapper(self, save=True, *args, **kwargs):
        if type(self) not in apps.get_models(include_auto_created=False):
            raise ValueError(f'Function {fn} must be method of django model')

        res = fn(self, *args, **kwargs)
        if save:
            self.save()
        return res

    return wrapper
