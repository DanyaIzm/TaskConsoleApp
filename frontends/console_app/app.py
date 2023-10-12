from pynput.keyboard import Key, KeyCode, Listener

from task_app.task_manager import TaskManager
from .screens.main_screen import MainScreen


class App:
    def __init__(self, task_manager: TaskManager) -> None:
        self.task_manager = task_manager
        self.tasks = []
        self.selected_task = 0
        self.screen = MainScreen(self)
        self._keyboard_listener = Listener(on_press=self._handle_keyboard_event)

    def start(self) -> None:
        self.run()

    def run(self) -> None:
        self._fetch_tasks()
        self.screen.render()

        with self._keyboard_listener:
            self._keyboard_listener.join()

    def stop(self) -> None:
        self.task_manager.close()

    def _fetch_tasks(self) -> None:
        self.tasks = self.task_manager.get_tasks()

    def _handle_keyboard_event(self, key: Key | KeyCode) -> None:
        self._fetch_tasks()

        self.screen.handle_key_press(key)

        self.screen.render()
