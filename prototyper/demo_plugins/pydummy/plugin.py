from prototyper.plugins import PluginBase


class Plugin(PluginBase):
    
    def on_build_complete(self):
        print('Dummy plugin on_build_complete')
