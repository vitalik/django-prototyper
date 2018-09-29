DJANGO_FIELDS = set([
    'AutoField',
    'BigAutoField',
    'BigIntegerField',
    'BinaryField',
    'BooleanField',
    'CharField',
    'DateField',
    'DateTimeField',
    'DecimalField',
    'DurationField',
    'EmailField',
    'FileField',
    'FilePathField',
    'FloatField',
    'ForeignKey',
    'GenericIPAddressField',
    'ImageField',
    'IntegerField',
    'ManyToManyField',
    'NullBooleanField',
    'OneToOneField',
    'PositiveIntegerField',
    'PositiveSmallIntegerField',
    'SlugField',
    'SmallIntegerField',
    'TextField',
    'TimeField',
    'URLField',
    'UUIDField',
])

REL_FIELDS = set(['ManyToManyField', 'ForeignKey', 'OneToOneField'])


def get_field_details(fld):
    field_type = fld.__class__.__name__
    if field_type not in DJANGO_FIELDS:
        field_type = get_original_field_type(fld)
    
    relation = None
    if field_type in REL_FIELDS:
        rel_app = fld.rel.to._meta.app_label
        rel_model = fld.rel.to.__name__
        relation = '%s.%s' % (rel_app, rel_model)

    return {
        'name': fld.name,
        'type': field_type,
        'relation': relation,
        'attrs': {},
    }


def get_original_field_type(fld):
    "Custom fields we cannot determine, so just try to find from which field it inherited"
    for ft in fld.__class__.__bases__:
        if ft.__name__ in DJANGO_FIELDS:
            return ft.__name__
    return fld.get_internal_type()
