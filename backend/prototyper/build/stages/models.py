from ..base import BuildStage
from pathlib import Path


class ModelsStage(BuildStage):
    def run(self):
        for app in self.build.details['apps']:
            self._handle_app(app)
    
    def _handle_app(self, app):
        mdodels_py = Path(self.build.build_path) / app['name'] / 'models.py'

        contents = ['from django.db import models', '', '']
        for model in app['models']:
            contents.append('class %s(models.Model):' % model['name'])
            contents.append('    pass')
            contents.extend(['', ''])

        mdodels_py.write_text('\n'.join(contents))
