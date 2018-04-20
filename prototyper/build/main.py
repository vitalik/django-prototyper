import shutil
import traceback
from django.conf import settings
from .base import Build, BuildStage, pipeline
from . import stages
from ..plugins import load_py_plugins


def run_build():
    build = Build(settings.PROTOTYPER_PROJECT)
    try:
        return _run_build(build)
    except Exception as e:
        build.logger.error(traceback.format_exc())
        return build


def _run_build(build):
    plugins = _init_py_plugins(build)
    pipeline(build, plugins, [
        stages.FirstStage,
        stages.AppsPackages,
        stages.SettingsStage,
        stages.UrlsStage,
        stages.WsgiStage,
        stages.ModelsStage,
        stages.AdminStage,
        stages.RequirementsStage,
    ])
    build.cleanup()
    return build


def _init_py_plugins(build):
    build.log('Loading plugins...')
    plugins = []
    for plugin in load_py_plugins():
        plugins.append(plugin)
    build.log(str(plugins))
    return plugins
