import os
from django.conf import settings


def load_plugins():
    results = []
    path = settings.PROTOTYPER_PROJECT.plugins_path
    if not os.path.exists(path):
        return results
    for p in os.listdir(path):
        plugin_module = os.path.join(path, p, 'plugin.py')
        print (plugin_module)
        if os.path.exists(plugin_module):
            klass = load(plugin_module)
            results.append(klass)
    return results


def load(path):
    with open(path) as f:
        return f.read()
