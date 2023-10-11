import json
import os

from task_app.task import Task

from .storage import TaskStorage


class FileTaskStorage(TaskStorage):
    "File Task Storage class. Saving and loading files from JSON"

    def __init__(self, path: str) -> None:
        super().__init__(path)
        self._path = path

        # try to create file
        try:
            with open(path, "x"):
                pass
        except FileExistsError:
            pass

        if os.path.getsize(path) != 0:
            with open(path, "r+") as file:
                self.tasks = self._deserialize(json.load(file))
        else:
            self.tasks = []

    def save_task(self, task: Task) -> None:
        task.id = self.tasks[-1].id + 1 if self.tasks else 0
        self.tasks.append(task)

    def get_all(self) -> list[Task]:
        return self.tasks

    def get_task(self, id: int) -> Task:
        ...

    def close(self) -> None:
        with open(self._path, "w") as file:
            file.write(json.dumps(self._serialize(self.tasks)))

    def _deserialize(self, serialized_tasks: dict) -> list[Task]:
        tasks = []

        for id, serialized_task in serialized_tasks.items():
            tasks.append(
                Task(
                    id=int(id),
                    name=serialized_task["name"],
                    description=serialized_task["description"],
                    completed=serialized_task["completed"],
                )
            )

        return tasks

    def _serialize(self, tasks: list[Task]) -> dict:
        serialized_tasks = {}

        for task in tasks:
            serialized_task = {
                "name": task.name,
                "description": task.description,
                "completed": task.completed,
            }

            serialized_tasks[task.id] = serialized_task

        return serialized_tasks
