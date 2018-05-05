import os
import django
from django.conf import settings


def django_configure():
    BASE_DIR = os.path.dirname(__file__)

    SECRET_KEY = os.environ.get('SECRET_KEY', '{{ secret_key }}')
    # ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', 'localhost').split(',')
    ALLOWED_HOSTS = ['*']

    settings.configure(
        DEBUG=True,
        BASE_DIR=BASE_DIR,
        SECRET_KEY=SECRET_KEY,
        ALLOWED_HOSTS=ALLOWED_HOSTS,
        ROOT_URLCONF='prototyper.urls',
        INSTALLED_APPS=[
        ],
        TEMPLATES=[{
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
        }],
        MIDDLEWARE_CLASSES=(
            'django.middleware.common.CommonMiddleware',
            'django.middleware.csrf.CsrfViewMiddleware',
            'django.middleware.clickjacking.XFrameOptionsMiddleware',
        ),

        DEV_MODE=os.environ.get('PROTOTYPER_DEV', 'no') == 'yes'
    )


def run_server(bind):
    from django.core.management import call_command
    if not bind:
        bind = '8080'
    kwargs = {}
    DEV_MODE = os.environ.get('PROTOTYPER_DEV', 'no') == 'yes'
    if not DEV_MODE:
        kwargs['use_reloader'] = False
    call_command('runserver', bind, **kwargs)

