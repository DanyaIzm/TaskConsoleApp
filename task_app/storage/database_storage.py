import sqlite3
from functools import wraps
from typing import Any

from task_app.task import Task

from .storage import TaskStorage


def _connection_provider(method):
    @wraps(method)
    def wrapped_method(*args, **kwargs) -> Any:
        self = args[0]

        self._connection = sqlite3.connect(self._path)

        result = method(*args, **kwargs)

        self._connection.close()
        self._connection = None

        return result

    return wrapped_method


class DatabaseTaskStorage(TaskStorage):
    def __init__(self, path: str) -> None:
        super().__init__(path)
        self._path = path
        self._connection: sqlite3.Connection = None

        self._create_table()

    @_connection_provider
    def save_task(self, task: Task) -> None:
        query = """
            INSERT INTO Tasks(name, description, completed)
            VALUES (?,?,?);
        """

        self._connection.execute(query, [task.name, task.description, task.completed])
        self._connection.commit()

    @_connection_provider
    def update_task(self, task: Task) -> None:
        query = """
            UPDATE Tasks
            SET name = ?, description = ?, completed = ?
            WHERE id = ?;
        """

        self._connection.execute(
            query, [task.name, task.description, task.completed, task.id]
        )
        self._connection.commit()

    @_connection_provider
    def get_all(self) -> list[Task]:
        query = """
            SELECT * FROM Tasks;
        """

        cursor = self._connection.execute(query)
        tasks = cursor.fetchall()

        return self._deserialize_tasks(tasks)

    @_connection_provider
    def get_task(self, id: int) -> Task:
        ...

    @_connection_provider
    def delete_task(self, task: Task) -> None:
        query = """
            DELETE FROM Tasks 
            WHERE id = ?;
        """

        self._connection.execute(query, [task.id])
        self._connection.commit()

    def close(self) -> None:
        pass

    @_connection_provider
    def _create_table(self) -> None:
        query = """
            CREATE TABLE IF NOT EXISTS Tasks(
                id integer primary key autoincrement,
                name varchar(255),
                description varchar(511),
                completed boolean
            );
        """
        self._connection.execute(query)
        self._connection.commit()

    def _deserialize_tasks(self, raw_tasks: list[tuple]) -> list[Task]:
        tasks = []

        for raw_task in raw_tasks:
            tasks.append(
                Task(
                    id=raw_task[0],
                    name=raw_task[1],
                    description=raw_task[2],
                    completed=raw_task[3],
                )
            )

        return tasks
