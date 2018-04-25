import os
import re
import json
from .initial import create_new_project


class Project(object):
    def __init__(self, path):
        self.path = os.path.abspath(path)
        self.name = self.get_name(path)
        self.storage_path = os.path.join(self.path, '.djangoprototyper')
        self.storage_file = os.path.join(self.storage_path, 'project.json')
        self.plugins_path = os.path.join(self.storage_path, 'plugins')
        self.init_storage()
    
    def init_storage(self):
        if os.path.exists(self.path) and not os.path.exists(self.storage_path):
            raise RuntimeError('Cannot init project. Path "%s" already exist and it is not djangoprototyper' % self.path)
        if not os.path.exists(self.path):
            self.init_new()
        else:
            self.load()  # pasing check
    
    def init_new(self):
        print('Creating new project', self.name)
        os.makedirs(self.storage_path)
        data = create_new_project(self.name)
        self.save(data)
    
    def load(self):
        with open(self.storage_file, 'r') as f:
            data = json.load(f)
        data['name'] = self.name
        data['path'] = self.path
        return data
    
    def save(self, data):
        with open(self.storage_file, 'w') as f:
            json.dump(data, f, indent=1)
    
    def get_name(self, path):
        name = os.path.basename(self.path)
        return re.sub(r'[^a-z\d_]', '', name)
