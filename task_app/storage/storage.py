from abc import ABC, abstractmethod

from task_app.task import Task


class TaskStorage(ABC):
    "Abstract class for task storage"

    def __init__(self, path: str) -> None:
        super().__init__()

    @abstractmethod
    def save_task(self, task: Task) -> None:
        ...

    @abstractmethod
    def update_task(self, task: Task) -> None:
        ...

    @abstractmethod
    def get_all(self) -> list[Task]:
        ...

    @abstractmethod
    def get_task(self, id: int) -> Task:
        ...

    @abstractmethod
    def delete_task(self, task: Task) -> None:
        ...

    @abstractmethod
    def close(self) -> None:
        ...
