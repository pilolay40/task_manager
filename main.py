from task_manager import TaskManager


def main():
    manager = TaskManager()
    while True:
        print("\n---- Gestor de Tareas Intelifente -----")
        print("1. Añadir tarea")
        print("2. Listar tareas")
        print("3. Completar tarea")
        print("4. Eliminar tarea")
        print("5. Salir")
        choice = input("Elige una opcion: ")

        match (choice):
            case "1":
                description = input("Introduce la description de la tarea: \n")
                manager.add_task(description)
            case "2":
                manager.list_task()
            case "3":
                id_task = input("Intorduce el id de la tarea a completar \n ")
                manager.complete_task(id_task)
            case "4":
                id_task = input("Intorduce el id de la tarea a eliminar \n ")
                manager.delete_task(id_task)
            case "5":
                print("Saliendo del programa")
                break
            case _:
                print("Opcion no valida, Selecciona Otra opcion")


if __name__ == "__main__":
    main()
