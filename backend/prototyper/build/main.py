from .base import Project, BuildStage, pipeline


class FirstStage(BuildStage):
    def run(self):
        self.log('manage.py')


class SettingsStage(BuildStage):
    def run(self):
        self.log('settings.py')


class ModelsStage(BuildStage):
    def run(self):
        for i in ['app1', 'foobar', 'blogs']:
            self.log('%s/models.py' % i)
        self.project.logger.warn('test')
        #raise RuntimeError('oops')


class AdminStage(BuildStage):
    def run(self):
        for i in ['app1', 'foobar', 'blogs']:
            self.log('%s/admin.py' % i)


def run_build(settings):
    project = Project(settings, None)
    ok = pipeline(project, [
        FirstStage,
        SettingsStage,
        ModelsStage,
        AdminStage,
    ])
    project.success = ok
    return project
