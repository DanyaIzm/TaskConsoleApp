from task_app import App, TaskManager
from task_app.storage import FileTaskStorage
from task_app.storage import DatabaseTaskStorage


def main():
    # storage = FileTaskStorage("./tasks.json")
    storage = DatabaseTaskStorage("./tasks.db")
    task_manager = TaskManager(storage=storage)
    app = App(task_manager=task_manager)

    app.start()


if __name__ == "__main__":
    main()
