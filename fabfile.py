from fabric.api import lcd, local, settings


def release():
    with lcd('frontend'):
        local('npm run build')
    local('cp frontend/dist/build.js prototyper/static/build.js')
    with settings(warn_only=True):
        local('rm dist/*.gz dist/*.whl')
    local('python setup.py bdist_wheel')
    local('python setup.py sdist')
    local('twine upload dist/*')
