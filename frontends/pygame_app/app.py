import sys
import pygame

from frontends.app import App
from frontends.pygame_app.screens.main_screen import MainScreen
from task_app.task_manager import TaskManager


_APP_SCALE_FACTOR = 70


class PygameApp(App):
    def __init__(self, task_manager: TaskManager) -> None:
        super().__init__(task_manager)
        pygame.init()
        self.pygame_screen = pygame.display.set_mode(
            (16 * _APP_SCALE_FACTOR, 9 * _APP_SCALE_FACTOR)
        )
        self._running = False
        self.screen = MainScreen(self)

    def start(self) -> None:
        self._running = True

        self._loop()

    def stop(self) -> None:
        self._running = False
        self.task_manager.close()
        pygame.quit()
        sys.exit(0)

    def _loop(self) -> None:
        while self._running:
            self.pygame_screen.fill((0, 0, 0))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.stop()

                self.screen.handle_event(event)

            self.screen.update()
            self.screen.render(self.pygame_screen)
            pygame.display.update()
