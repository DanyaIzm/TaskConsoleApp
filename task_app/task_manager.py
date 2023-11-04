from functools import wraps
from typing import Callable
from task_app.task import Task
from task_app.storage import TaskStorage


def _task_update_required(method: Callable):
    @wraps(method)
    def wrapped_method(self, *args, **kwargs):
        result = method(self, *args, **kwargs)
        self._tasks = self.storage.get_all()

        return result

    return wrapped_method


class TaskManager:
    def __init__(self, storage: TaskStorage) -> None:
        self.storage = storage
        self._tasks = storage.get_all()

    def get_tasks(self) -> list[Task]:
        return self._tasks

    @_task_update_required
    def add_task(self, task: Task) -> None:
        self.storage.save_task(task)

    @_task_update_required
    def change_state(self, task: Task) -> None:
        if not task.completed:
            task.mark_as_completed()
        else:
            task.mark_as_uncompleted()

        self.storage.update_task(task)

    @_task_update_required
    def delete_task(self, task: Task) -> None:
        self.storage.delete_task(task)

    def close(self) -> None:
        self.storage.close()
