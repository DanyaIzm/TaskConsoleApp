import pygame

from frontends.pygame_app.ui_elements.input_field import InputField
from task_app.task import Task
from .screen import PygameScreen
from frontends.app import App
from frontends.pygame_app.ui_elements import UIElement
from frontends.pygame_app.ui_elements.text import Text


class AddTaskScreen(PygameScreen):
    def __init__(self, app: App) -> None:
        super().__init__(app)

        self._previous_screen = self.app.screen

        self._header = Text(
            pygame.Rect(10, 10, self.app.pygame_screen.get_width(), 30),
            text="Добавить новую задачу",
            font_size=30,
            color=(255, 255, 255),
        )
        self._name_input = InputField(
            pygame.rect.Rect(10, 50, self.app.pygame_screen.get_width() // 5 * 4, 30),
            label_text="Название",
            label_color=(255, 255, 255),
            input_color=(0xF7, 0x7B, 0x4D),
            label_font_size=30,
            input_font_size=30,
            selected=True,
        )
        self._description_input = InputField(
            pygame.rect.Rect(10, 90, self.app.pygame_screen.get_width() // 5 * 4, 30),
            label_text="Описание",
            label_color=(255, 255, 255),
            input_color=(0xF7, 0x7B, 0x4D),
            label_font_size=30,
            input_font_size=30,
            selected=False,
        )
        self._footer = Text(
            pygame.Rect(
                10,
                self.app.pygame_screen.get_height() - 30,
                0,
                self.app.pygame_screen.get_width(),
            ),
            text="вниз-вверх - выбор поля ввода; enter - подтвердить; escape - выйти",
            font_size=20,
            color=(255, 255, 255),
        )

        self._elements: list[UIElement] = [
            self._header,
            self._footer,
            self._name_input,
            self._description_input,
        ]

        self._active_input = self._name_input

    def handle_event(self, event: pygame.event.Event) -> None:
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_position = event.pos

            for element in self._elements:
                if isinstance(element, InputField):
                    if element.rect.collidepoint(*mouse_position):
                        self._active_input = element

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.app.screen = self._previous_screen
            elif event.key == pygame.K_BACKSPACE:
                self._active_input.update_properties(
                    input_text=self._active_input.properties["input_text"][:-1]
                )
            elif event.key == pygame.K_RETURN:
                self.app.task_manager.add_task(
                    Task(
                        name=self._name_input.properties["input_text"],
                        description=self._description_input.properties["input_text"],
                    )
                )
                self.app.screen = self._previous_screen
            else:
                if event.unicode:
                    self._active_input.update_properties(
                        input_text=self._active_input.properties["input_text"]
                        + event.unicode
                    )

    def update(self) -> None:
        for element in self._elements:
            if isinstance(element, InputField):
                element.update_properties(selected=(element is self._active_input))

        for element in self._elements:
            element.update()

    def render(self, surface: pygame.Surface) -> None:
        for element in self._elements:
            element.render(surface)
