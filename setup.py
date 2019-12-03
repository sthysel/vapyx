# -*- encoding: utf-8 -*-
from glob import glob
from os.path import basename, splitext

from setuptools import find_packages, setup

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name='vapyx',
    license='MIT',
    version='0.0.1',
    description='Manage AXIS video devices',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Robert Svensson, Thys Meintjes',
    author_email='Kane610@users.noreply.github.com, sthysel@gmail.com',
    entry_points={
        'console_scripts': [
            'vapyx=vapyx.cli:cli',
        ],
    },
    install_requires=[
        'click',
        'loguru',
        'requests',
    ],
    url='https://github.com/sthysel/vapyx',
    classifiers=[
        'License :: MIT',
        'Development Status :: 4 - Beta',
        'Operating System :: Unix',
        'Operating System :: POSIX',
        'Programming Language :: Python :: 3',
        'Topic :: Utilities',
    ],
    keywords=['axis', 'vapix', 'onvif', 'event stream'],
    extras_require={},
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    py_modules=[splitext(basename(path))[0] for path in glob('src/*.py')],
    include_package_data=True,
    zip_safe=False,
    package_data={
        '': ['config/*.yml'],
    },
)
