import json

from celery.bin.base import Command


class CeleryRun(Command):

    def add_arguments(self, parser):
        parser.add_argument(
          'task', help='Task to run',
        ),
        parser.add_argument(
          'task_kwargs', help='Kwargs to pass to task'
        )

    def run(self, task=None, task_kwargs=None, **kwargs):
        try:
            task_kwargs = json.loads(task_kwargs)
        except ValueError:
            print "%s was not parsed as json" % task_kwargs
            return
        print 'Running %s with kwargs %s' % (task, task_kwargs)
        self.app.tasks[task](**task_kwargs)
        print 'Task %s successfully ran' % task