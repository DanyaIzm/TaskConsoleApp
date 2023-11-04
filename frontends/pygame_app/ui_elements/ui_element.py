from abc import ABC, abstractmethod
import pygame


class UIElement(ABC):
    def __init__(self, rect: pygame.Rect, **properties) -> None:
        super().__init__()
        self.rect = rect
        self.properties = properties

    def update_properties(self, **new_properties):
        for k, v in new_properties.items():
            self.properties[k] = v

    @abstractmethod
    def update(self) -> None:
        ...

    @abstractmethod
    def render(self, surface: pygame.Surface) -> None:
        ...
