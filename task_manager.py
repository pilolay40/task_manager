class Task:
    def __init__(self, id, description, completed=False):
        self.id = id
        self.description = description
        self.completed = completed

    def __str__(self):
        status = "✓" if self.completed else " "
        return f"[{status}] #{self.id}: {self.description}"


class TaskManager:
    def __init__(self):
        self._tasks = []
        self._next_id = 1

    def add_task(self, description: str):
        task = Task(self._next_id, description)
        self._tasks.append(task)
        self._next_id += 1
        print(f"Tarea {task} añadida")

    def list_task(self):
        if not self._tasks:
            print("No hay tareas pendientes")
        else:
            for task in self._tasks:
                print(task)

    def complete_task(self, id):
        task = self.find_task(id=id)
        if not task:
            print(f"Tarea con id {id} no encontrada")
        else:
            task.completed = True
            print(f"Tarea completada {task}")

    def delete_task(self, id):
        task = self.find_task(id)
        if not task:
            print(f"Tarea con id {id} no encontrada")

        self._tasks.remove(task)
        print(f"Tarea con id {id} no eliminada")

    def find_task(self, id):
        for task in self._tasks:
            if task.id == int(id):
                return task
