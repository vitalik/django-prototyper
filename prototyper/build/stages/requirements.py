from ..base import BuildStage
from pathlib import Path


class RequirementsStage(BuildStage):
    def run(self):
        req_txt_file = Path(self.build.build_path) / 'requirements.txt'
        requirements = set(['Django', 'Pillow'])
        for plugin in self.build.details['plugins']:
            for req in plugin.get('requirements', []):
                requirements.add(req)

        lines = '\n'.join(sorted(requirements)) + '\n'
        req_txt_file.write_text(lines)
