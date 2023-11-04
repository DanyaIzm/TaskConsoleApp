import pygame
from .ui_element import UIElement


class InputField(UIElement):
    def __init__(self, rect: pygame.Rect, **properties) -> None:
        super().__init__(rect, **properties)
        self._label_font = pygame.font.Font(size=properties["label_font_size"])
        self._input_font = pygame.font.Font(size=properties["input_font_size"])
        self._input_box = pygame.Rect(
            self.rect.left + self.rect.width // 3,
            self.rect.top,
            self.rect.width // 3 * 2,
            self.rect.height,
        )

        if not self.properties.get("input_text"):
            self.properties["input_text"] = ""

    def update(self) -> None:
        return super().update()

    def render(self, surface: pygame.Surface) -> None:
        rendered_label = self._label_font.render(
            self.properties["label_text"],
            1,
            self.properties["label_color"],
        )
        rendered_input_text = self._input_font.render(
            self.properties["input_text"],
            1,
            self.properties["input_color"],
        )

        rendered_box = pygame.draw.rect(
            surface,
            (200, 200, 200) if self.properties["selected"] else (100, 100, 100),
            self._input_box,
        )
        surface.blit(rendered_input_text, rendered_box.topleft)
        surface.blit(rendered_label, self.rect.topleft)
