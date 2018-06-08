from setuptools import setup, find_packages

setup(
  name='celery-run',
  entry_points={
    'celery.commands': [
      'run = celery_run.command:CeleryRun',
      'ls = celery_run.command:CeleryLs'
    ],
  },
  install_requires=['celery>=3'],
  packages=find_packages()
)