import pygame
from .ui_element import UIElement


class TaskItem(UIElement):
    def __init__(self, rect: pygame.Rect, **properties) -> None:
        super().__init__(rect, **properties)
        self._font = pygame.font.Font(size=properties["font_size"])
        self._selected_box = pygame.Rect(*self.rect.topleft, 16, 16)
        self._checked_box = pygame.Rect(
            self.rect.left + self._selected_box.width + 5, self.rect.top, 20, 20
        )

    def update(self) -> None:
        pass

    def render(self, surface: pygame.Surface) -> None:
        task = self.properties["task"]

        if self.properties["selected"]:
            pygame.draw.circle(
                surface,
                (0, 0, 255),
                self._selected_box.center,
                self._selected_box.width // 2,
            )

        pygame.draw.rect(
            surface, (0, 255, 0) if task.completed else (255, 0, 0), self._checked_box
        )

        rendered_text = self._font.render(
            f"{task.name}: {task.description}", 1, self.properties["color"]
        )
        surface.blit(
            rendered_text,
            (
                self._checked_box.right + 5,
                self._checked_box.centery - rendered_text.get_height() // 2,
            ),
        )
