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
        parser.add_argument('--no-result', dest='print_result', action='store_false', default=True)

    def run(self, task=None, task_kwargs=None, print_result=None, **kwargs):
        try:
            task_kwargs = json.loads(task_kwargs)
        except ValueError:
            print("%s was not parsed as json" % task_kwargs)
            return
        print('Running %s with kwargs %s' % (task, task_kwargs))
        result = self.app.tasks[task](**task_kwargs)
        print('Task %s successfully ran' % task)
        if print_result:
            print('Tsk %s returned %s' % (task, result))


class CeleryLs(Command):

    def run(self, **kwargs):
        task_names = self.app.tasks.keys()
        print('Available tasks are:')
        for task_name in task_names:
            print(task_name)
