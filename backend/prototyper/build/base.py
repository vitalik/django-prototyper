import os
import traceback
from .log import get_logger


class Build(object):
    def __init__(self, project):
        self.details = project.load()
        self.project = project
        self.build_path = os.path.join(project.path, project.name)
        self.logger = get_logger()
        self.success = False  # succesful build finished
    
    def log(self, message):
        self.logger.info(message)


class BuildStage(object):
    def __init__(self, build):
        self.build = build
    
    def run(self):
        raise NotImplementedError('please implement run')
    
    def log(self, message):
        self.build.log(message)


def pipeline(build, stages):
    for cls in stages:
        try:
            stage = cls(build)
            stage.run()
        except Exception as e:
            build.logger.error(traceback.format_exc())
            return False
    return True
