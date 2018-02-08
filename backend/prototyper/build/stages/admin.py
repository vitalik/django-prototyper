from ..base import BuildStage
from pathlib import Path


class AdminStage(BuildStage):
    def run(self):
        for app in self.build.details['apps']:
            self._handle_app(app)
    
    def _handle_app(self, app):
        admin_py = Path(self.build.build_path) / app['name'] / 'admin.py'
        admin_py.write_text('from django.contrib import admin')
