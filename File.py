import json

class File:
    @staticmethod
    def read():
        with open("task.json", "r") as archivo:
            tasks = json.load(archivo)
            print("Tareas Creadas")
            for task in tasks:
                print(f"id: {task['id']}, {task['name']} {task['state']}")

    def readNotDone():
        with open("task.json", "r") as archivo:
            tasks = json.load(archivo)
            print("Tareas Sin Empezar")
            for task in tasks:
                if task['state'] == 'Not Done':
                    print(f"id: {task['id']}, {task['name']} {task['state']}")

    def readProgress():
        with open("task.json", "r") as archivo:
            tasks = json.load(archivo)
            print("Tareas En Progreso")
            for task in tasks:
                if task['state'] == 'Progress':
                    print(f"id: {task['id']}, {task['name']} {task['state']}")

    def readDone():
        with open("task.json", "r") as archivo:
            tasks = json.load(archivo)
            print("Tareas Terminadas")
            for task in tasks:
                if task['state'] == 'Done':
                    print(f"id: {task['id']}, {task['name']} {task['state']}")

    @staticmethod
    def write(tasks):
        with open("task.json", "w") as archivo:
            json.dump(tasks, archivo, indent=4)