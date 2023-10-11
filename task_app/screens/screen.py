from abc import ABC, abstractclassmethod

from pynput.keyboard import Key


class Screen(ABC):
    def __init__(self, app) -> None:
        super().__init__()
        self.app = app

    @abstractclassmethod
    def render(self) -> None:
        ...

    @abstractclassmethod
    def handle_key_press(self, key: Key) -> None:
        ...
