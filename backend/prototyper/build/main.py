from .base import Build, BuildStage, pipeline
from .stages import FirstStage
from django.conf import settings


class SettingsStage(BuildStage):
    def run(self):
        self.log('settings.py')


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
    ok = pipeline(build, [
        FirstStage,
        SettingsStage,
        ModelsStage,
        AdminStage,
    ])
    build.success = ok
    return build
