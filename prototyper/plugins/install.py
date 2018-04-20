import os
import shutil
import json
import zipfile
import re
from django.conf import settings


def install(name, url):
    _validate(name, url)
    plugins_path = settings.PROTOTYPER_PROJECT.plugins_path
    installer = get_installer(name, url, plugins_path)
    installer.clean()
    installer.install()
    return installer.config()


def _validate(name, url):
    # we do not allow any other characters for plugin name so that user do no play with "/etc/passwd" sort of names
    assert re.match(r'^[a-z-_]+$', name.lower()), "Invalid plugin name"


def get_installer(name, url, plugins_path):
    if os.path.exists(url):
        if url.lower().endswith('.zip'):
            return ZipFileInstaller(name, url, plugins_path)
        if os.path.isdir(url):
            return PathInstaller(name, url, plugins_path)
    elif url.lower().startswith('http'):
        if url.lower().endswith('.zip'):
            return ZipUrlInstaller(name, url, plugins_path)
        # TODO: github/git ?
    raise NotImplementedError('Do not know how to install %s, should be url/path to .zip file or path to directory')


class Installer(object):
    def __init__(self, name, url, plugins_path):
        self.name = name
        self.url = url
        # basename is important so that users do not play with unsecure names
        self.plugin_dest = os.path.join(plugins_path, os.path.basename(name))
    
    def config(self):
        with open(os.path.join(self.plugin_dest, 'config.json')) as f:
            return json.load(f)
    
    def clean(self):
        if os.path.exists(self.plugin_dest):
            shutil.rmtree(self.plugin_dest)
    
    def install(self):
        raise NotImplementedError('Please implement install')


class PathInstaller(Installer):
    def install(self):
        shutil.copytree(self.url, self.plugin_dest)


class ZipFileInstaller(Installer):
    def install(self):
        with zipfile.ZipFile(self.url, 'r') as z:
            z.extractall(self.plugin_dest)


class ZipUrlInstaller(Installer):
    def install(self):
        path = self.download()
        with zipfile.ZipExtFile(path, 'r') as z:
            z.extractall(self.plugin_dest)


# DEMO_PLUGIN = """from prototyper.plugins import PluginBase


# class Plugin(PluginBase):
    
#     def on_build_complete(self):
#         print('on_build_complete')
# """


# def demo(path):
#     plugin_py = path / 'plugin.py'
#     plugin_py.write_text(DEMO_PLUGIN)


# def _plugin_path(name):
#     path = os.path.join(settings.PROTOTYPER_PROJECT.plugins_path, name)
#     path = pathlib.Path(path)
#     path.mkdir(parents=True, exist_ok=True)
#     return path
