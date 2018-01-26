#!/usr/bin/env python
import sys
import os
import argparse

from django.conf import settings

BASE_DIR = os.path.dirname(__file__)

SECRET_KEY = os.environ.get('SECRET_KEY', '{{ secret_key }}')
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', 'localhost').split(',')


settings.configure(
    DEBUG=True,
    SECRET_KEY=SECRET_KEY,
    ALLOWED_HOSTS=ALLOWED_HOSTS,
    ROOT_URLCONF='prototyper.urls',
    INSTALLED_APPS=[
        'webpack_loader',
    ],
    WEBPACK_LOADER={
        'DEFAULT': {
            'BUNDLE_DIR_NAME': os.path.join(BASE_DIR, '..', 'frontend', 'dist'),
            'STATS_FILE': os.path.join(BASE_DIR, '..', 'frontend', 'webpack-stats.json'),
        }
    },
    TEMPLATES=[{
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
    }],
    MIDDLEWARE_CLASSES=(
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ),
)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('path_to_project')

    from prototyper.project import Project

    settings.PROTOTYPER_PROJECT = Project(parser.parse_args().path_to_project)

    import django
    django.setup()
    from django.core.management import call_command

    call_command('runserver')
