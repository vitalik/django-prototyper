import sys
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

CURRENT_PYTHON = sys.version_info[:2]
REQUIRED_PYTHON = (3, 5)

if CURRENT_PYTHON < REQUIRED_PYTHON:
    sys.stderr.write("""
==========================
Unsupported Python version
==========================
Django Prototyper requires Python {}.{}, but you're trying to
install it on Python {}.{}.
""".format(*(REQUIRED_PYTHON + CURRENT_PYTHON)))
    sys.exit(1)


here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()


version = __import__('prototyper').VERSION

setup(
    name='django-prototyper',
    version=version,
    description='Django prototyping tool',
    long_description=long_description,
    url='https://github.com/vitalik/django-prototyper',
    author='Vitaliy Kucheryaviy',
    author_email='p.p.r.vitaly@gmail.com',

    packages=find_packages(exclude=['tests']),

    install_requires=['django'],

    package_data={'prototyper': [
        'static/build.js', 'static/logo.png', 'static/welcome.png',  # TODO: make it automatic
        'demo_plugins/**/*.json',
    ]},
    include_package_data=True,

    entry_points={
        'console_scripts': [
            'prototyper=prototyper.cli:main',
        ],
    },


    classifiers=[
        'Development Status :: 3 - Alpha',  # 3 - Alpha, 4 - Beta, 5 - Production

        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    keywords='django prototype boilerplate development uml diagrams',
)
