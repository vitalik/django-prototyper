#!/usr/bin/env python
import sys
import os
import argparse

import django
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


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('path_to_project')
    parser.add_argument('--build', action='store_true')
    return parser.parse_args()


def run_server():
    from django.core.management import call_command
    call_command('runserver', '0.0.0.0:8000') # TODO: get from args


def build():
    from prototyper.build import run_build
    run_build()


if __name__ == "__main__":
    args = parse_args()

    from prototyper.project import Project
    settings.PROTOTYPER_PROJECT = Project(args.path_to_project)
    django.setup()

    if args.build is True:
        build()
    else:
        run_server()
