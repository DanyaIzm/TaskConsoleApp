from task_app.task import Task
from task_app.storage import TaskStorage


class TaskManager:
    def __init__(self, storage: TaskStorage) -> None:
        self.storage = storage
        self._tasks = storage.get_all()

    def add_task(self, task: Task) -> None:
        self.storage.save_task(task)
        self._tasks = self.storage.get_all()

    def get_tasks(self) -> list[Task]:
        return self._tasks

    def change_state(self, task: Task) -> None:
        if not task.completed:
            task.mark_as_completed()
        else:
            task.mark_as_uncompleted()

        self.storage.update_task(task)
        self._tasks = self.storage.get_all()

    def delete_task(self, task: Task) -> None:
        self.storage.delete_task(task)
        self._tasks = self.storage.get_all()

    def close(self) -> None:
        self.storage.close()
