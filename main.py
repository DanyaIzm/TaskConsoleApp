from frontends.console_app import App
from task_app import TaskManager
from task_app.storage import DatabaseTaskStorage, FileTaskStorage


def main():
    # storage = FileTaskStorage("./tasks.json")
    storage = DatabaseTaskStorage("./tasks.db")
    task_manager = TaskManager(storage=storage)
    app = App(task_manager=task_manager)

    app.start()


if __name__ == "__main__":
    main()
