import pygame
from .ui_element import UIElement


class Text(UIElement):
    def __init__(self, rect: pygame.Rect, **properties) -> None:
        super().__init__(rect, **properties)
        self._font = pygame.font.Font(size=properties["font_size"])

    def update(self) -> None:
        pass

    def render(self, surface: pygame.Surface) -> None:
        rendered_text = self._font.render(
            self.properties["text"], 1, self.properties["color"]
        )

        surface.blit(rendered_text, self.rect.topleft)
