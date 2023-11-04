from abc import ABC, abstractmethod
from task_app.task_manager import TaskManager


class App(ABC):
    def __init__(self, task_manager: TaskManager) -> None:
        super().__init__()
        self.task_manager = task_manager

    @abstractmethod
    def start(self) -> None:
        ...

    @abstractmethod
    def stop(self) -> None:
        ...
