import os
import sys

from pynput.keyboard import Key, KeyCode

from task_app.task import Task

from .add_task_screen import AddTaskScreen
from .screen import Screen


class MainScreen(Screen):
    def __init__(self, app) -> None:
        super().__init__(app)

    def render(self) -> None:
        os.system("cls")
        self._draw_header()
        self._draw_tasks()
        self._draw_footer()

    def handle_key_press(self, key: Key | KeyCode) -> None:
        if key == Key.esc:
            self.app.stop()
            sys.exit(0)

        if key == Key.up:
            self.app.selected_task = (
                self.app.selected_task - 1 if self.app.selected_task > 0 else 0
            )

        if key == Key.down:
            self.app.selected_task = (
                self.app.selected_task + 1
                if self.app.selected_task < len(self.app.tasks) - 1
                else len(self.app.tasks) - 1
            )

        if key == Key.space:
            if self.app.tasks:
                self.app.task_manager.change_state(
                    self.app.tasks[self.app.selected_task]
                )

        if key == Key.tab:
            self.app.screen = AddTaskScreen(self.app)

    def _draw_header(self) -> None:
        print("Ваши задачи:\n")

    def _draw_tasks(self) -> None:
        if not self.app.tasks:
            print("На данный момент задач нет!")

            return

        for index, task in enumerate(self.app.tasks):
            self._print_task(task, index == self.app.selected_task)

    def _print_task(self, task: Task, selected: bool) -> None:
        print(
            f"{'>' if selected else ' '}[{'v' if task.completed else 'x'}] "
            f"{task.name}: {task.description}"
        )

    def _draw_footer(self) -> None:
        print(
            "\n\n"
            "Управление: вверх, вниз - выбрать задачу; "
            "tab - создать задачу;\n"
            "space - отметить, как выполненную; delete - удалить задачу; \n"
            "escape - выйти из программы."
        )
