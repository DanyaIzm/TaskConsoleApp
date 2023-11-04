from abc import ABC, abstractmethod

from pynput.keyboard import Key


class Screen(ABC):
    def __init__(self, app) -> None:
        super().__init__()
        self.app = app

    @abstractmethod
    def render(self) -> None:
        ...

    @abstractmethod
    def handle_key_press(self, key: Key) -> None:
        ...
