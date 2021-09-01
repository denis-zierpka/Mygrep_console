from os.path import dirname, join

from setuptools import find_packages, setup

import myapp

setup(
    name='mygrep',
    version=myapp.__version__,
    author='Denis Zierpka',
    author_email='denis.spb02@mail.ru',
    packages=find_packages(),
    test_suite='tests',
    long_description=open(join(dirname(__file__), 'README.md')).read(),
    entry_points={
        'console_scripts': [
            'mygrep = myapp.app:main',
        ]
    },
)
