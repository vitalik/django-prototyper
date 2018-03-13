

class PluginBase(object):

    def __init__(self, name):
        self.name = name
    
    def __repr__(self):
        return '<Plugin %s>' % self.name
    
    def set_build(self, build):
        self.build = build

    def on_build_complete(self):
        pass
