import traceback
from .log import get_logger


class Project(object):
    def __init__(self, settings, details):
        self.logger = get_logger()
        self.success = False  # succesful build finished
    
    def log(self, message):
        self.logger.info(message)


class BuildStage(object):
    def __init__(self, project):
        self.project = project
    
    def run(self):
        raise NotImplementedError('please implement run')
    
    def log(self, message):
        self.project.log(message)


def pipeline(project, stages):
    for cls in stages:
        try:
            stage = cls(project)
            stage.run()
        except Exception as e:
            project.logger.error(traceback.format_exc())
            return False
    return True
