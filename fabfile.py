import os
import re
from fabric.api import lcd, local, settings


def release():
    version_bump()

    with lcd('frontend'):
        local('npm run build')
    local('cp frontend/dist/build.js prototyper/static/build.js')
    with settings(warn_only=True):
        local('rm dist/*.gz dist/*.whl')
    local('python setup.py bdist_wheel')
    local('python setup.py sdist')
    local('twine upload dist/*')


def version_bump():
    ver_file = os.path.join(os.path.dirname(__file__), 'prototyper/version.py')
    with open(ver_file) as f:
        contents = f.read()
    assert len(contents.splitlines()) == 1  # we expect only 1 line as this is automaticlly generated
    ver = re.findall(r'\d+\.\d+\.\d+', contents)[0]
    ver = map(int, ver.split('.'))
    ver[-1] += 1
    with open(ver_file, 'w') as f:
        f.write("VERSION = '%d.%d.%d'\n" % tuple(ver))
    
    local('git add prototyper/version.py')
    local('git commit -m "version %s"' % ver)
