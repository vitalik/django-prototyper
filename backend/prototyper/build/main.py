import shutil
from django.conf import settings
from .base import Build, BuildStage, pipeline
from . import stages


def run_build():
    build = Build(settings.PROTOTYPER_PROJECT)
    pipeline(build, [
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
