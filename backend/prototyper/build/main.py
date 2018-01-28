from .base import BuildProject, BuildStage, pipeline
from django.conf import settings


class FirstStage(BuildStage):
    def run(self):
        self.log('manage.py')


class SettingsStage(BuildStage):
    def run(self):
        self.log('settings.py')


class ModelsStage(BuildStage):
    def run(self):
        for i in self.project.details['apps']:
            self.log('%s/models.py' % i['name'])
        self.project.logger.warn('test')


class AdminStage(BuildStage):
    def run(self):
        for i in self.project.details['apps']:
            self.log('%s/admin.py' % i['name'])


def run_build():
    project = BuildProject(settings.PROTOTYPER_PROJECT)
    ok = pipeline(project, [
        FirstStage,
        SettingsStage,
        ModelsStage,
        AdminStage,
    ])
    project.success = ok
    return project
