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
        admin = [f"@admin.register({model['name']})", f"class {model['name']}Admin(admin.ModelAdmin):"]
        if model['admin']:
            for name, attr in model['admin'].items():
                if attr['fields']:
                    if attr['single']:
                        admin.append(f"  {name} = '{attr['fields'][0]}'")
                    else:
                        fields = [f'"{field}"' for field in attr['fields']]
                        admin.append(f"  {name} = [{', '.join(fields)}]")
        else:
            admin.append("  pass")
        return admin
