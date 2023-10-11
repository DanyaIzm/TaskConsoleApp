from abc import ABC, abstractclassmethod

from task_app.task import Task


class TaskStorage(ABC):
    "Abstract class for task storage"

    def __init__(self, path: str) -> None:
        super().__init__()

    @abstractclassmethod
    def save_task(self, task: Task) -> None:
        ...

    @abstractclassmethod
    def get_all(self) -> list[Task]:
        ...

    @abstractclassmethod
    def get_task(self, id: int) -> Task:
        ...

    @abstractclassmethod
    def close(self) -> None:
        ...
