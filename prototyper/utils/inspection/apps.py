import os


def installed_apps_with_models():
    "django 1.7+ detection"
    from django.apps import apps
    cwd = os.getcwd()

    for app in apps.get_app_configs():
        path = os.path.abspath(app.path)
        external = not path.startswith(cwd) or app.name.startswith('django.')
        models = list(app.get_models())
        yield app.name, external, models
