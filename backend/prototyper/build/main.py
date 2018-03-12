import shutil
from django.conf import settings
from .base import Build, BuildStage, pipeline
from . import stages
from ..plugins import load_plugins


def run_build():
    build = Build(settings.PROTOTYPER_PROJECT)
    plugins = _init_plugins(build)
    pipeline(build, plugins, [
        stages.FirstStage,
        stages.AppsPackages,
        stages.SettingsStage,
        stages.UrlsStage,
        stages.WsgiStage,
        stages.ModelsStage,
        stages.AdminStage,
    ])
    build.cleanup()
    return build


def _init_plugins(build):
    build.log('Loading plugins...')
    for klass in load_plugins():
        build.log(klass)
