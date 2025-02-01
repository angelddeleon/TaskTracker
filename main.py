import sys
import os
import json
import click
from ListTask import List
from File import File


@click.group()
def cli():
    ruta = "task.json"

    if not os.path.exists(ruta):
        with open(ruta, "w") as archivo:
            json.dump([], archivo)  

    with open(ruta, "r") as archivo:
        try:
            tasks = json.load(archivo)
        except json.JSONDecodeError:
            print("El archivo está vacío o contiene datos no válidos. Inicializando con una lista vacía.")
            tasks = []
        except Exception as e:
            print(f"Error al cargar tareas: {e}")
            tasks = []

    # Crear una instancia de List y almacenar en una variable global
    global task_list
    task_list = List(tasks)

@cli.command()
@click.option('--name', required=True, help='Nombre de la tarea')
@click.option("--status", required=True, help="Estado de la tarea (1-no hecha, 2-en progreso, 3-hecha)")
def new(name, status):
    if not name or not status:
        click.echo('Es necesario el nombre de la tarea o su estatus')
        return
    
    task_list.addTask(name, status)

@cli.command()
@click.option('--id', required=True, help='Id de la tarea que desea cambiar')
@click.option("--status", required=True, help="Estado de la tarea (1-no hecha, 2-en progreso, 3-hecha)")
def update(id, status):
    if not id or not status:
        click.echo('Es necesario el id de la tarea o su estatus')
        return
    
    task_list.updateTask(id, status)

@cli.command()
@click.option('--id', required=True, help='Id de la tarea que desea eliminar')
def delete(id):
    if not id:
        click.echo('Es necesario el id de la tarea ')
        return
    
    task_list.eliminateTask(id)


@cli.command()
def Tasks():
    List.showList()

@cli.command()
def TasksNotDone():
    List.showListNotDone()

@cli.command()
def TasksProgress():
    List.showListProgress()

@cli.command()
def TasksDone():
    List.showListDone()

if __name__ == "__main__":
    cli()






def main():
    ruta = "task.json"

    if not os.path.exists(ruta):
        with open(ruta, "w") as archivo:
            json.dump([], archivo)  

    with open(ruta, "r") as archivo:
        try:
            tasks = json.load(archivo)
        except json.JSONDecodeError:
            print("El archivo está vacío o contiene datos no válidos. Inicializando con una lista vacía.")
            tasks = []
        except Exception as e:
            print(f"Error al cargar tareas: {e}")
            tasks = []


    # Guarda las tareas de nuevo en el archivo
    with open(ruta, "w") as archivo:
        json.dump(tasks, archivo, indent=4)


    File.read()
        
    list = List(tasks)

    while True:
        print("Opciones")
        print("1. Agregar una Tarea<>")
        print("2. Update Task<>")
        print("3. Eliminar Tareas")
        print("4. mostrar lista de tares<>")
        print("5. mostrar lista de tares Not Done<>")
        print("6. mostrar lista de tares Progress<>")
        print("7. mostrar lista de tares Done<>")
        print("8.Salir de la aplicacion")

        opcion = input('Ingrese su opcion: ')

        if opcion == '1':

            list.addTask()

        elif opcion == '2':
            print("Actualizando la tarea")

        elif opcion == '3':
            list.eliminateTask()

        elif opcion == '4':


            list.showList()

        elif opcion == '5':


            list.showList()
        
        elif opcion == '6':


            list.showListProgress()


        elif opcion == '8':
            print("Saliendo de la aplicacion")
            break


    print('Hello World')



main()




