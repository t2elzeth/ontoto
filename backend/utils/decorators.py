from django.apps import apps


def control_save(fn):
    def wrapper(*args, **kwargs):
        if not args:
            raise ValueError(f'Function {fn} must have at least one positional argument: `self`')

        instance = args[0]
        if type(instance) not in apps.get_models(include_auto_created=False):
            raise ValueError(f'Function {fn} must be method of django model')

        fn(*args, **kwargs)
        if kwargs.get('save'):
            instance.save()

    return wrapper
