import sys
import os
import argparse
import django
from django.conf import settings
from prototyper import VERSION
from prototyper.server import django_configure, run_server


def _parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('path_to_project')
    parser.add_argument('--build', action='store_true')
    parser.add_argument('--bind', help='HOST:PORT to bind http server on.  example  --bind=0.0.0.0:8000')
    return parser.parse_args()


def build():
    from prototyper.build import run_build
    run_build()


def main():
    print('Django Prototyper %s' % VERSION)
    args = _parse_args()
    django_configure()

    from prototyper.project import Project
    settings.PROTOTYPER_PROJECT = Project(args.path_to_project)
    django.setup()

    if args.build is True:
        build()
    else:
        run_server(args.bind)
