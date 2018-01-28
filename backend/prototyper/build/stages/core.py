from ..base import BuildStage


class FirstStage(BuildStage):
    def run(self):
        self.log('manage.py')
