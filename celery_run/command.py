import json

from celery.bin.base import Command


class CeleryRun(Command):

    def add_arguments(self, parser):
        parser.add_argument(
          'task', help='Task to run',
        ),
        parser.add_argument(
          'task_kwargs', help='Kwargs to pass to task', type=json.loads
        )

    def run(self, task=None, task_kwargs=None, **kwargs):
        print 'Running %s with kwargs %s' % (task, task_kwargs)
        self.app.tasks[task](**task_kwargs)