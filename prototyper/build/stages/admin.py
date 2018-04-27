from pathlib import Path

from ..base import BuildStage


class AdminStage(BuildStage):
    def run(self):
        for app in self.build.details['apps']:
            if app['external'] is False:
                self._handle_app(app)

    def _handle_app(self, app):
        contents = ['from django.contrib import admin', 'from .models import *']

        for model in app['models']:
            if model['admin']['generate']:
                model['admin'].pop('generate')
                contents.extend(['', ''])
                contents.extend(self._handle_model(app, model))

        contents.append('')  # empty line

        admin_py = Path(self.build.build_path) / app['name'] / 'admin.py'
        admin_py.write_text('\n'.join(contents))

    def _handle_model(self, app, model):
        admin = [
            "@admin.register(%s)" % model['name'],
            "class %sAdmin(admin.ModelAdmin):" % model['name'],
        ]
        lines = []
        if model['admin']:
            for name, attr in model['admin'].items():
                if attr['fields']:
                    if attr['single']:
                        lines.append("    {0} = '{1}'".format(name, attr['fields'][0]))
                    else:
                        fields = ["'%s'" % f for f in attr['fields']]
                        lines.append("    {0} = [{1}]".format(name, ', '.join(fields)))
        if not lines:
            lines.append("    pass")
        return admin + lines
