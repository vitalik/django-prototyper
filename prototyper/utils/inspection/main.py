import os
import json
from prototyper.project.initial import create_new_project
from .apps import installed_apps_with_models
from .model import get_model_details


def inspect(to_path):
    if os.path.exists(to_path):
        raise Exception("Directory '%s' already exist" % to_path)
    proj_name = os.path.basename(to_path)
    
    project = create_new_project(proj_name)
    project['apps'] = []  # clearnig default apps
    
    print('Bulding to %s' % to_path)
    for a, ext, models in installed_apps_with_models():

        app = {
            'name': a,
            'external': ext,
            'models': []
        }
        
        print(' %s %s' % (ext and '~' or '+', a))
        for m in models:
            res_model = get_model_details(m)
            if ext:
                res_model['fields'] = []
                res_model['admin']['generate'] = False
            app['models'].append(res_model)
        
        project['apps'].append(app)

    save(to_path, project)
    print('Done.')
    print('now run:\nprototyper %s' % to_path)


def save(to_path, data):
    store_path = os.path.join(to_path, '.djangoprototyper')
    os.makedirs(store_path)
    with open(os.path.join(store_path, 'project.json'), 'w') as f:
        json.dump(data, f, indent=1)
