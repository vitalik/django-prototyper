import os
import traceback
import tempfile
import shutil
from .log import get_logger


class Build(object):
    def __init__(self, project):
        self.details = project.load()
        self.project = project
        self.build_path = tempfile.mkdtemp(prefix='djprototyper')
        self.settings_pckg_path = os.path.join(self.build_path, project.name)  # TODO: can be configurable
        self.logger = get_logger()
        self.success = False  # succesful build finished
    
    def log(self, message):
        self.logger.info(message)
    
    def save(self):
        result_path = os.path.join(self.project.path, self.project.name)
        assert len(result_path) > 3  # just in case making sure no root folder is ever removed :)
        if os.path.exists(result_path):
            self.log('Cleaning previous build {}'.format(result_path))
            shutil.rmtree(result_path)
        self.log('Saving to "{}"'.format(result_path))
        shutil.move(self.build_path, result_path)

    def cleanup(self):
        if os.path.exists(self.build_path):
            self.log('Cleaning: {}'.format(self.build_path))
            shutil.rmtree(self.build_path)


class BuildStage(object):
    def __init__(self, build):
        self.build = build
    
    def run(self):
        raise NotImplementedError('please implement run')
    
    def log(self, message):
        self.build.log(message)


def pipeline(build, plugins, stages):
    for cls in stages:
        assert issubclass(cls, BuildStage)
        try:
            build.log('Running ' + cls.__name__)
            stage = cls(build)
            stage.run()
        except Exception as e:
            build.logger.error(traceback.format_exc())
            return False
    
    for plug in plugins:
        plug.on_build_complete()

    build.save()
    build.success = True
    return True
