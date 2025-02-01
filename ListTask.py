
from File import File
from Task import Task



def lineBreak():
    print("\n")



class List:

    def __init__(self, tasks):
       self.tareas = tasks
       self.cont = 1

    def showList():
        File.read()

    def showListNotDone():
        File.readNotDone()
    
    def showListProgress():
        File.readProgress()

    def showListDone():
        File.readDone()


    def addTask(self, name, optionStatus):
        status = ''
        
        if optionStatus == '1':
            status = "Not Done"  
        elif optionStatus == '2':
            status = "Progress"  
        elif optionStatus == '3':
            status = "Done"
        else:
            print("Esta opción no es válida. El estado no se ha cambiado.")
            return  
        
        count = len(self.tareas) + 1

        task = Task(count, name, status)
        taskDict = task.to_dict()
        self.tareas.append(taskDict)

        File.write(self.tareas)

        

        print("Su tarea ha sido agregada.")

    def updateTask(self, idTask, optionStatus):

        taskFound = False
        idTaskInt = int(idTask)

        for task in self.tareas:
            if task['id'] == idTaskInt:  
                taskFound = True

                if optionStatus == '1':
                    task['status'] = "not Done"
                elif optionStatus == '2':
                    task['status'] = "Progress"
                elif optionStatus == '3':
                    task['status'] = "Done"
                else:
                    print("Esta opción no es válida. El estado no se ha cambiado.")
                    return 

                break  

                

        if not taskFound:
            print("No existe ninguna tarea con este ID.")
            return

        File.write(self.tareas)

        print("Tarea actualizada con éxito.")


    def eliminateTask(self, idTask):

        newList = []
        taskFound = False

        idTaskInt = int(idTask)

        for task in self.tareas:

            if task["id"] == idTaskInt:
                taskFound = True
                continue
            else:
                newList.append(task)

        self.tareas = newList

        File.write(self.tareas)

        if taskFound == False:
            print("No existe ninguna con este id")
            return

        print("Tarea Eliminada")







