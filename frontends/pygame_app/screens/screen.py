from abc import ABC, abstractmethod
import pygame

from frontends.app import App


class PygameScreen(ABC):
    def __init__(self, app: App) -> None:
        super().__init__()
        self.app = app

    @abstractmethod
    def handle_event(self, event: pygame.event.Event) -> None:
        ...

    @abstractmethod
    def update(self) -> None:
        ...

    @abstractmethod
    def render(self, surface: pygame.Surface) -> None:
        ...
