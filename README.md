# celery-run

Celery extension to run tasks from command line.

Examples:

celery run task_name '{"key1": 2, "key2": "test"}' --app=yourapp --no-result
celery run task_name '{"key1": 2, "key2": "test"}' --app=yourapp

# celery-ls

Celery extension to list available tasks.

Example:

celery run ls --app=yourapp
