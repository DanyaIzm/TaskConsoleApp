from task_app.task import Task
from task_app.storage import TaskStorage


class TaskManager:
    def __init__(self, storage: TaskStorage) -> None:
        self.storage = storage

    def add_task(self, task: Task) -> None:
        self.storage.save_task(task)

    def get_tasks(self) -> list[Task]:
        return self.storage.get_all()

    def change_state(self, task: Task) -> None:
        if not task.completed:
            task.mark_as_completed()
        else:
            task.mark_as_uncompleted()

    def close(self) -> None:
        self.storage.close()
