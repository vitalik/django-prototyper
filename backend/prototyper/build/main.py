import shutil
from django.conf import settings
from .base import Build, BuildStage, pipeline
from .stages import FirstStage, AppsPackages, SettingsStage, UrlsStage, WsgiStage


class ModelsStage(BuildStage):
    def run(self):
        for i in self.build.details['apps']:
            self.log('%s/models.py' % i['name'])
        self.build.logger.warn('test')


class AdminStage(BuildStage):
    def run(self):
        for i in self.build.details['apps']:
            self.log('%s/admin.py' % i['name'])


def run_build():
    build = Build(settings.PROTOTYPER_PROJECT)
    pipeline(build, [
        FirstStage,
        AppsPackages,
        SettingsStage,
        UrlsStage,
        WsgiStage,
        ModelsStage,
        AdminStage,
    ])
    build.cleanup()
    return build
