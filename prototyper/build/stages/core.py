from ..base import BuildStage
from pathlib import Path


MANAGE_PY = """#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "{0}.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
"""


class FirstStage(BuildStage):
    def run(self):
        root = Path(self.build.build_path)
        manage_py = root / 'manage.py'
        manage_py.touch(0o755)
        contents = MANAGE_PY.format(self.build.project.name)
        manage_py.write_text(contents)


class AppsPackages(BuildStage):
    def run(self):
        root = Path(self.build.build_path)
        for app in self.build.details['apps']:
            if not app['external']:
                app_pkg = root / app['name']
                app_pkg.mkdir()
                (app_pkg / '__init__.py').touch()
