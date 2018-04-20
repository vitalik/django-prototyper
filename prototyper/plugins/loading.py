import os
from django.conf import settings


def load_py_plugins():
    results = []
    path = settings.PROTOTYPER_PROJECT.plugins_path
    if not os.path.exists(path):
        return results
    
    plugins = settings.PROTOTYPER_PROJECT.load()['plugins']
    installed_plugins = set([p['name'] for p in plugins])
    
    for p in os.listdir(path):
        if p not in installed_plugins:
            continue
        plugin_module = os.path.join(path, p, 'plugin.py')
        print(plugin_module)
        if os.path.exists(plugin_module):
            klass = load(plugin_module)
            plugin = klass(p)
            results.append(klass(p))
    return results


def load(path):
    module = _load_module('plugin', path)
    return module.Plugin


def _load_module(module, path):
    import importlib.util
    spec = importlib.util.spec_from_file_location(module, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module
