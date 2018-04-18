from ..base import BuildStage
from pathlib import Path


class AdminStage(BuildStage):
    def run(self):
        for app in self.build.details['apps']:
            if app['external'] is False:
                self._handle_app(app)
    
    def _handle_app(self, app):
        contents = ['from django.contrib import admin', 'from .models import *']
        
        for model in app['models']:
            contents.extend(['', ''])
            contents.extend(self._handle_model(app, model))

        contents.append('')  # empty line

        admin_py = Path(self.build.build_path) / app['name'] / 'admin.py'
        admin_py.write_text('\n'.join(contents))
    
    def _handle_model(self, app, model):
        return [
            '@admin.register(%s)' % model['name'],
            'class %sAdmin(admin.ModelAdmin):' % model['name'],
            '    pass',
        ]
