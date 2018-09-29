from .field import get_field_details


def get_model_details(model):
    name = model.__name__
    fields = []
    for f in model._meta.fields:
        if f.name == 'id' and f.primary_key:
            continue
        
        fld = get_field_details(f)
        fields.append(fld)
    return {
        'name': name,
        'fields': fields,
        'admin': {'generate': True},
    }
