import os
import pathlib
from django.conf import settings


def install(url):
    plugin = {'url': url, 'title': url, 'name': url}
    path = _plugin_path(plugin['name'])
    demo(path)
    return plugin


DEMO_PLUGIN = """from prototyper.plugins import PluginBase


class Plugin(PluginBase):
    
    def on_build_complete(self):
        print('on_build_complete')
"""


def demo(path):
    plugin_py = path / 'plugin.py'
    plugin_py.write_text(DEMO_PLUGIN)


def _plugin_path(name):
    path = os.path.join(settings.PROTOTYPER_PROJECT.plugins_path, name)
    path = pathlib.Path(path)
    path.mkdir(parents=True, exist_ok=True)
    return path
