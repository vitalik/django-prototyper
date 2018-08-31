from ..base import BuildStage
from pathlib import Path
from prototyper.conf import DJANGO_TARGET

DJ_VER_REQ = '>={maj}.{min},<{maj}.{next}'.format(
    maj=DJANGO_TARGET[0],
    min=DJANGO_TARGET[1],
    next=DJANGO_TARGET[1] + 1,
)


class RequirementsStage(BuildStage):
    def run(self):
        req_txt_file = Path(self.build.build_path) / 'requirements.txt'
        requirements = set([
            'Django{0}'.format(DJ_VER_REQ),
            'Pillow',
        ])
        for plugin in self.build.details['plugins']:
            for req in plugin.get('requirements', []):
                requirements.add(req)

        lines = '\n'.join(sorted(requirements)) + '\n'
        req_txt_file.write_text(lines)
