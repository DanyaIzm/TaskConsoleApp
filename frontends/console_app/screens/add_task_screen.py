import os
from enum import Enum

from pynput.keyboard import Key, KeyCode

from task_app.task import Task
from .screen import Screen


class State(Enum):
    NAME_STATE: int = 1
    DESCRIPTION_STATE: int = 2


class AddTaskScreen(Screen):
    def __init__(self, app) -> None:
        super().__init__(app)
        self._last_screen = self.app.screen
        self._task_name = ""
        self._task_description = ""
        self._state = State.NAME_STATE

    def render(self) -> None:
        os.system("cls")
        print("Добавить новую задачу:\n\n")
        print(
            f"{'>' if self._state == State.NAME_STATE else ' '}Название: "
            f"{self._task_name}"
        )
        print(
            f"{'>' if self._state == State.DESCRIPTION_STATE else ' '}Описание: "
            f"{self._task_description}"
        )

    def handle_key_press(self, key: Key | KeyCode) -> None:
        # restore screen state
        if key == Key.esc:
            self.app.screen = self._last_screen

        if key == Key.enter:
            match self._state:
                case State.NAME_STATE:
                    self._state = State.DESCRIPTION_STATE
                case State.DESCRIPTION_STATE:
                    self._add_task()
                    self.app.screen = self._last_screen

        if key == Key.backspace:
            match self._state:
                case State.NAME_STATE:
                    self._task_name = self._task_name[:-1]
                case State.DESCRIPTION_STATE:
                    self._task_description = self._task_description[:-1]

        if key == Key.space:
            self._update_task_field(" ")

        if isinstance(key, KeyCode):
            self._update_task_field(key.char)

    def _update_task_field(self, char: str):
        match self._state:
            case State.NAME_STATE:
                self._task_name = self._task_name + char
            case State.DESCRIPTION_STATE:
                self._task_description = self._task_description + char

    def _add_task(self) -> None:
        self.app.task_manager.add_task(Task(self._task_name, self._task_description))
