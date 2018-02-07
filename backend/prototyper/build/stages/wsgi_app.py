from ..base import BuildStage
from pathlib import Path

TPL = """\"\"\"
WSGI config for {0} project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
\"\"\"

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "{0}.settings")

application = get_wsgi_application()
"""


class WsgiStage(BuildStage):
    def run(self):
        wsgi_py = Path(self.build.settings_pckg_path) / 'wsgi.py'
        wsgi_py.write_text(TPL.format(self.build.project.name))
