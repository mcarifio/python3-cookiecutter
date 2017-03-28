#!/usr/bin/env python3
# Mike Carifio <mike@carif.io>

from setuptools import setup


# TODO mike@ecirca.com: pip3 install git+https://www.encirca.com/check.vali.center@master # test in venv
# {{project}}
setup(name='project',
      version='0.1',
      description='http://www.github.com/mcarifio/{{project}}/README.md',
      url='http://www.github.com/mcarifio/{{project}}',
      author='Mike Carifio',
      author_email='mike@carif.io',
      license='{{license}}',
      # packages=['{{project}}'],
      packages=['project'],
      # add scripts
      install_requires=[
          'fire',
          'nose',
          'AttrDict',
'wheel' # for pip3 install --upgrade -r requirements.txt in a virtual environment
      ])
