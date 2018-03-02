from ..base import BuildStage
from pathlib import Path


class codelines(list):
    def __init__(self, initial=None):
        super(codelines, self).__init__(initial or [])
    
    def extend_indent(self, lines, indent=1):
        spaces = ' ' * (4 * indent)
        for l in lines:
            self.append(spaces + l)


def camel_to_spaces(s):
    import re
    return re.sub("([a-z])([A-Z])", "\g<1> \g<2>", s)


class ModelsStage(BuildStage):
    def run(self):
        self.use_ugettext = self.build.details['build_settings'].get('ugettext_lazy', True)
        for app in self.build.details['apps']:
            self._handle_app(app)
    
    def _handle_app(self, app):
        mdodels_py = Path(self.build.build_path) / app['name'] / 'models.py'
        contents = ['from django.db import models']
        if self.use_ugettext:
            contents.append('from django.utils.translation import ugettext_lazy as _')

        for model in app['models']:
            contents.extend(['', ''])
            model_lines = ModelBuilder(self, app, model)
            contents.extend(model_lines)
        
        contents.append('')  # last empty line

        self.log('\n'.join(contents))

        mdodels_py.write_text('\n'.join(contents))


class ModelBuilder(codelines):
    def __init__(self, stage, app, model):
        super(ModelBuilder, self).__init__()
        self.stage, self.app, self.model = stage, app, model
        self._create()

    def _create(self):
        self.append('class %s(models.Model):' % self.model['name'])

        for field in self.model['fields']:
            self.extend_indent(self._handle_field(field))

        self.extend_indent(self._handle_meta())
        
        if len(self) == 1:
            self.append('    pass')
    
    def _handle_field(self, field):
        lines = []
        lines.append('%s = %s()' % (field['name'], field['type']))
        return lines

    def _handle_meta(self):
        lines = codelines([''])
        lines.append('class Meta:')

        v_name = camel_to_spaces(self.model['name']).lower()
        v_name_plural = v_name
        if v_name_plural.endswith('y'):
            v_name_plural = v_name_plural[:-1] + 'ies'
        elif not v_name_plural.endswith('s'):
            v_name_plural += 's'
        lines.extend_indent(["verbose_name = %s" % self._trans_str(v_name)])
        lines.extend_indent(["verbose_name_plural = %s" % self._trans_str(v_name_plural)])
        
        return lines
    
    def _trans_str(self, s):
        "Returns either _('<s>' or '<s>' based on build settings)"
        q = "'" in s and '"' or "'"
        result = q + s + q
        if self.stage.use_ugettext:
            return '_(' + result + ')'
        return result
