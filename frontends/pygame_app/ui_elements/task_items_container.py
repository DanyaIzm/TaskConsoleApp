import pygame

from frontends.pygame_app.ui_elements.task_item import TaskItem

from .ui_element import UIElement


class TaskItemsContainer(UIElement):
    def __init__(self, rect: pygame.Rect, **properties) -> None:
        super().__init__(rect, **properties)
        self._task_items: list[TaskItem] = []
        self._first_item_rect = pygame.Rect(
            *self.rect.topleft, self.rect.width, self.rect.height
        )

    def update_properties(self, **new_properties):
        super().update_properties(**new_properties)

        tasks = self.properties["tasks"]
        selected_task = self.properties["selected_task"]
        font_size = self.properties["font_size"]
        color = self.properties["color"]

        self._task_items.clear()

        for index, task in enumerate(tasks):
            self._task_items.append(
                TaskItem(
                    pygame.Rect(
                        self._first_item_rect.left,
                        self._first_item_rect.top + (self.rect.height + 5) * index,
                        self._first_item_rect.width,
                        self._first_item_rect.height,
                    ),
                    task=task,
                    selected=index == selected_task,
                    font_size=font_size,
                    color=color,
                )
            )

    def update(self) -> None:
        pass

    def render(self, surface: pygame.Surface) -> None:
        for task_item in self._task_items:
            task_item.render(surface)
