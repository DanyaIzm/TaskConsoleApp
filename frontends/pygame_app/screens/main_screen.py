import pygame

from frontends.pygame_app.screens.add_task_screen import AddTaskScreen
from .screen import PygameScreen
from frontends.app import App
from frontends.pygame_app.ui_elements import UIElement
from frontends.pygame_app.ui_elements.task_items_container import TaskItemsContainer
from frontends.pygame_app.ui_elements.text import Text


class MainScreen(PygameScreen):
    def __init__(self, app: App) -> None:
        super().__init__(app)
        self._header = Text(
            pygame.Rect(10, 10, 0, 30),
            text="Ваши задачи",
            font_size=30,
            color=(255, 255, 255),
        )
        self._items_container = TaskItemsContainer(
            pygame.Rect(self._header.rect.left, self._header.rect.bottom + 10, 0, 20),
            selected_task=0,
            font_size=20,
            color=(255, 255, 255),
        )
        self._footer = Text(
            pygame.Rect(
                10,
                self.app.pygame_screen.get_height() - 30,
                0,
                self.app.pygame_screen.get_width(),
            ),
            text="Управление: вверх, вниз - выбрать задачу; "
            "tab - создать задачу; "
            "space - отметить, как выполненную; delete - удалить задачу; "
            "escape - выйти из программы.",
            font_size=20,
            color=(255, 255, 255),
        )

        self._elements: list[UIElement] = [
            self._header,
            self._items_container,
            self._footer,
        ]

        self._tasks = self.app.task_manager.get_tasks()

    def handle_event(self, event: pygame.event.Event) -> None:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                last_selected_task = self._items_container.properties["selected_task"]
                self._items_container.update_properties(
                    selected_task=last_selected_task - 1
                    if last_selected_task > 0
                    else 0
                )
            elif event.key == pygame.K_DOWN:
                last_selected_task = self._items_container.properties["selected_task"]
                self._items_container.update_properties(
                    selected_task=last_selected_task + 1
                    if last_selected_task < len(self._tasks) - 1
                    else len(self._tasks) - 1
                )
            elif event.key == pygame.K_SPACE:
                selected_task = self._items_container.properties["selected_task"]
                self.app.task_manager.change_state(self._tasks[selected_task])
                self._items_container.update_properties(tasks=self._tasks)
            elif event.key == pygame.K_DELETE:
                selected_task = self._items_container.properties["selected_task"]
                self.app.task_manager.delete_task(self._tasks[selected_task])
            elif event.key == pygame.K_TAB:
                self.app.screen = AddTaskScreen(self.app)
            elif event.key == pygame.K_ESCAPE:
                self.app.stop()

    def update(self) -> None:
        self._tasks = self.app.task_manager.get_tasks()

        self._items_container.update_properties(tasks=self._tasks)

        for element in self._elements:
            element.update()

    def render(self, surface: pygame.Surface) -> None:
        for element in self._elements:
            element.render(surface)
