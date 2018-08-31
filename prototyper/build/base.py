import os
import traceback
import tempfile
import shutil
from .log import get_logger


class Build(object):
    def __init__(self, project):
        self.details = project.load()
        self.project = project
        self.temp_folder = tempfile.mkdtemp(prefix='djprototyper')
        self.build_path = os.path.join(self.temp_folder, project.name)
        os.mkdir(self.build_path)

        self.settings_pckg_path = self.build_path
        if self.is_settings_py_separate():
            self.settings_pckg_path = os.path.join(self.settings_pckg_path, project.name)
        
        self.logger = get_logger()
        self.success = False  # succesful build finished
    
    def log(self, message):
        self.logger.info(message)
    
    def save(self):
        self.log('Cleaning previous build {}'.format(self.project.path))
        for i in os.listdir(self.project.path):
            if i == '.djangoprototyper':
                continue
            name = os.path.join(self.project.path, i)
            if os.path.isdir(name):
                shutil.rmtree(name)
            else:
                os.remove(name)
        
        for f in os.listdir(self.temp_folder):
            self.log('Saving {}'.format(f))
            src = os.path.join(self.temp_folder, f)
            dst = os.path.join(self.project.path, f)
            shutil.move(src, dst)

    def cleanup(self):
        if os.path.exists(self.temp_folder):
            self.log('Cleaning: {}'.format(self.temp_folder))
            shutil.rmtree(self.temp_folder)
    
    def is_settings_py_separate(self):
        return self.details['build_settings'].get('settings_path', 'separate') == 'separate'


class BuildStage(object):
    def __init__(self, build):
        self.build = build
    
    def run(self):
        raise NotImplementedError('please implement run')
    
    def log(self, message):
        self.build.log(message)
    
    def settings_module(self, module):
        "returns py module path based on settings_path build setting"
        if self.build.is_settings_py_separate():
            return '{0}.{1}'.format(self.build.project.name, module)
        return module


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
        plug.set_build(build)
        plug.on_build_complete()

    build.save()
    build.success = True
    return True
