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


def code_string(s):
    q = "'" in s and '"' or "'"
    return q + s + q


class ModelsStage(BuildStage):
    def run(self):
        self.use_ugettext = self.build.details['build_settings'].get('ugettext_lazy', True)
        for app in self.build.details['apps']:
            if not app['external']:
                self._handle_app(app)
    
    def _handle_app(self, app):
        mdodels_py = Path(self.build.build_path) / app['name'] / 'models.py'
        contents = ['from django.db import models']
        if self.use_ugettext:
            contents.append('from django.utils.translation import ugettext_lazy as _')
        
        self._inheritance_imports(app, contents)

        for model in app['models']:
            contents.extend(['', ''])
            model_lines = ModelBuilder(self, app, model)
            contents.extend(model_lines)
        
        contents.append('')  # last empty line

        # self.log('\n'.join(contents))

        mdodels_py.write_text('\n'.join(contents))
    
    def _inheritance_imports(self, app, contents):
        all_classes = set()
        for model in app['models']:
            for m in model.get('inheritance', []):
                all_classes.add(m)
        for cls in sorted(all_classes):
            app, model = cls.split('.')
            contents.append('from %s.models import %s' % (app, model))


class ModelBuilder(codelines):
    def __init__(self, stage, app, model):
        super(ModelBuilder, self).__init__()
        self.stage, self.app, self.model = stage, app, model
        self._create()

    def _create(self):
        self.append('class %s(%s):' % (self.model['name'], self._inheritance()))

        for field in self.model['fields']:
            self.extend_indent(self._handle_field(field))

        self.extend_indent(self._handle_meta())
        self.extend_indent([''])
        self.extend_indent(self._handle_str_output())
        
        if len(self) == 1:
            self.append('    pass')
    
    def _inheritance(self):
        classes = self.model.get('inheritance', [])
        if not classes:
            return 'models.Model'
        return ', '.join([i.split('.')[-1] for i in classes])
    
    def _handle_field(self, field):
        line = FieldBuilder(self, field).render()
        return [line]

    def _handle_meta(self):
        lines = codelines([''])
        lines.append('class Meta:')

        v_name = camel_to_spaces(self.model['name']).lower()
        v_name_plural = v_name
        if v_name_plural.endswith('y'):
            v_name_plural = v_name_plural[:-1] + 'ies'
        elif not v_name_plural.endswith('s'):
            v_name_plural += 's'
        lines.extend_indent([
            "verbose_name = %s" % self._trans_str(v_name),
            "verbose_name_plural = %s" % self._trans_str(v_name_plural),
        ])
        
        return lines
    
    def _handle_str_output(self):
        "Renders the __str__ method"
        if len(self.model['fields']) == 0:
            return []
        non_rel_fields = [i for i in self.model['fields'] if not i['relation']]
        if len(non_rel_fields) == 0:
            return []
        
        fld = 'self.' + non_rel_fields[0]['name']
        if non_rel_fields[0]['type'] not in ('CharField', 'TextField', 'SlugField', 'EmailField'):
            fld = 'str(%s)' % fld

        return [
            'def __str__(self):',
            '    return %s' % fld
        ]
    
    def _trans_str(self, s):
        "Returns either _('<s>' or '<s>' based on build settings)"
        result = code_string(s)
        if self.stage.use_ugettext:
            return '_(' + result + ')'
        return result


ONLY_COMMON_ATTRS = [
    'AutoField', 'BigAutoField', 'BigIntegerField',
    'BinaryField', 'BooleanField',
    'DurationField', 'EmailField', 'FloatField',
    'IntegerField', 'NullBooleanField',
    'PositiveIntegerField', 'PositiveSmallIntegerField',
    'SlugField', 'SmallIntegerField',
    'TextField', 'URLField', 'UUIDField',
]


class FieldBuilder(object):
    def __init__(self, model_builder, field):
        self.model_builder = model_builder
        self.name = field['name']
        self.type = field['type']
        self.attrs = field['attrs']
        self.relation = field['relation']
    
    def render(self):
        if self.type in ONLY_COMMON_ATTRS:
            attrs = self._common_attrs()
        else:
            method = getattr(self, '_attrs_%s' % self.type)
            attrs = method()
        return '%s = models.%s(%s)' % (self.name, self.type, ', '.join(attrs))
    
    def _common_attrs(self, verbose_name_kv=False):
        attributes = []

        _trans = self.model_builder._trans_str

        verbose_name = _trans(self.name.replace('_', ' '))
        if verbose_name_kv:
            verbose_name = 'verbose_name=' + verbose_name

        attributes.append(verbose_name)

        if self.attrs.get('primary_key') is True:
            attributes.append('primary_key=True')
        if self.attrs.get('null') is True:
            attributes.append('null=True')
        if self.attrs.get('blank') is True:
            attributes.append('blank=True')
        if self.attrs.get('unique') is True:
            attributes.append('unique=True')
        if self.attrs.get('db_index') is True:
            attributes.append('db_index=True')
        if self.attrs.get('editable') is False:
            attributes.append('editable=False')
        if self.attrs.get('default') is True:
            val = code_string(self.attrs['default'])
            if self.type in ('BigIntegerField', 'BooleanField', 'FloatField', 'IntegerField', 'IntegerField', 'NullBooleanField', 'PositiveIntegerField', 'PositiveSmallIntegerField', 'SmallIntegerField'):
                val = self.attrs['default']
            attributes.append('default=%s' % val)
        if self.attrs.get('help_text'):
            attributes.append('help_text=%s' % _trans(self.attrs['help_text']))
        return attributes
    
    def _attrs_CharField(self):
        build_settings = self.model_builder.stage.build.details['build_settings']
        attrs = self._common_attrs()
        if self.attrs.get('max_length'):
            max_length = self.attrs['max_length']
        else:
            max_length = build_settings.get('charfield_max_length', 200)
        attrs.append('max_length=%s' % max_length)
        return attrs
    
    def _relational(self):
        attrs = [code_string(self.relation)]
        attrs.extend(self._common_attrs(verbose_name_kv=True))
        if self.type in ('OneToOneField', 'ForeignKey'):
            attrs.append('on_delete=models.CASCADE')
        return attrs
    
    _attrs_ManyToManyField = _relational
    _attrs_OneToOneField = _relational
    _attrs_ForeignKey = _relational

    def _attrs_DecimalField(self):
        attrs = self._common_attrs()
        # TODO: maybe build settings ?
        attrs.extend(['max_digits=10', 'decimal_places=2'])
        return attrs
    
    def _attrs_DateTimeField(self):
        attrs = self._common_attrs()
        if self.attrs.get('auto_now') is True:
            attrs.append('auto_now=True')
        if self.attrs.get('auto_now_add') is True:
            attrs.append('auto_now_add=True')
        return attrs
    
    _attrs_DateField = _attrs_DateTimeField
    _attrs_TimeField = _attrs_DateTimeField

    def _attrs_FileField(self):
        attrs = self._common_attrs()
        if self.attrs.get('upload_to'):
            attrs.append('upload_to=%s' % code_string(self.attrs['upload_to']))
        return attrs

    _attrs_ImageField = _attrs_FileField

    def _attrs_FilePathField(self):
        # TODO
        return self._common_attrs()
    
    def _attrs_GenericIPAddressField(self):
        # TODO
        return self._common_attrs()
