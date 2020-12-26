from django.apps import apps


def control_save(fn):
    def wrapper(self, save=True, *args, **kwargs):
        if not self:
            raise ValueError(f'Function {fn} must have at least one positional argument: `self`')

        if type(self) not in apps.get_models(include_auto_created=False):
            raise ValueError(f'Function {fn} must be method of django model')

        res = fn(self, *args, **kwargs)
        if save:
            self.save()
        return res

    return wrapper
