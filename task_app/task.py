class Task:
    def __init__(
        self,
        name: str,
        description: str,
        id: int = None,
        completed: bool = False,
    ) -> None:
        self.id = id
        self.name = name
        self.description = description
        self.completed = completed

    def mark_as_completed(self) -> None:
        self.completed = True

    def mark_as_uncompleted(self) -> None:
        self.completed = False

    def __repr__(self) -> str:
        return f"{self.id}: {self.name}, {self.description}, {self.completed}"
