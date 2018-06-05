from setuptools import setup, find_packages

setup(
  name='celery-run',
  entry_points={
    'celery.commands': [
      'run = celery_run.command:CeleryRun',
    ],
  },
  install_requires=['celery>=3'],
  packages=find_packages()
)