# Hace la importación de la libreria tkinter que sirve para dar un aspecto más visual a nuestro programa
import tkinter as tk
from tkinter import messagebox

# Creación de un objeto llamado Tarea cuyos atributos serán nombre, descripción y estado
class Tarea:
    # Constructor donde iniciamos los atributos, por defecto se iniciara como tarea pendiente
    def __init__(self, name, desc):
        self.name = name
        self.desc = desc
        self.complete = False
    
    # Metodo que pone el atributo estado como completo
    def completeTask(self):
        self.complete = True
    
    # Es un método que devuelve un string con información sobre la Tarea
    def __str__(self):
        state = "Completada" if self.complete else "Pendiente"
        return f"Tarea {self.name}: {self.desc} - {state}"
    
# Esta clase contiene como atributo la lista de tareas y tiene los métodos solicitados (Agregar, eliminar, completar y mostrar tareas)
class ListaTareas:
    # Iniciamos la lista vacia
    def __init__(self):
        self.tasks = []

    # Método que añade una tarea a la lista
    def addTask(self, name, desc):
        task = Tarea(name, desc)
        self.tasks.append(task)

    # Método que pone el estado de una tarea como completado, para ello cogemos el índice de la tarea
    def completeTask(self, i):
        try:
            self.tasks[i].completeTask()
        except IndexError:
            # Maneja la excepción en caso de que no existan tareas con ese índice
            raise ValueError("No existe ninguna tarea con ese índice")
    
    # Método que borra una tarea de nuestra lista, para ello se le indica el índice
    def deleteTask(self, i):
        try:
            self.tasks.pop(i)
        except IndexError:
            # Maneja la excepción en caso de que no existan tareas con ese índice
            raise ValueError("No existe ninguna tarea con ese índice") 
    
    # Método que muestra todas las tareas
    def showTasks(self):
        return self.tasks
    
class App:
    def __init__(self, root):
        # Esto se encarga, mediante el uso de tkinter, de poner el título a la ventana emergente cuando ejecutemos el programa
        self.root = root
        self.root.title("Gestor de Tareas")
        # Creamos un objeto ListaTareas
        self.taskList = ListaTareas()

        self.frame = tk.Frame(root)
        self.frame.pack(pady=20)

        # Creamos la etiqueta Nombre de la tarea y le damos un tamaño, tambien creamos el input para que lo use el usuario
        self.labelName = tk.Label(self.frame, text="Nombre de la Tarea:")
        self.labelName.grid(row=0, column=0)
        self.entryName = tk.Entry(self.frame)
        self.entryName.grid(row=0, column=1)
        
        # Creamos la etiqueta Descripción y le damos un tamaño, tambien creamos el input para que lo use el usuario
        self.labelDesc = tk.Label(self.frame, text="Descripción:")
        self.labelDesc.grid(row=1, column=0)
        self.entryDesc = tk.Entry(self.frame)
        self.entryDesc.grid(row=1, column=1)
        
        self.addBtn = tk.Button(self.frame,text="AGREGAR TAREA", command=self.addTask)
        self.addBtn.grid(row=2, columnspan=2, pady=10)
        
        self.tasksListBox = tk.Listbox(self.frame, width=50, height=10)
        self.tasksListBox.grid(row=3, columnspan=2, pady=10)
        
        self.completeBtn = tk.Button(self.frame,text="COMPLETAR TAREA", command=self.completeTask)
        self.completeBtn.grid(row=4, columnspan=2, pady=5)
       
        self.deleteBtn = tk.Button(self.frame,text="ELIMINAR TAREA", command=self.deleteTask)
        self.deleteBtn.grid(row=5, columnspan=2, pady=5)
        
        self.showTasks()
        
    def addTask(self):
        name = self.entryName.get()
        desc = self.entryDesc.get()
        self.tasksList.addTask(name, desc)
        self.showTasks()
        self.entryName.delete(0, tk.END)
        self.entryDesc.delete(0, tk.END)
            
    def completeTask(self):
        try:
            i = self.tasksListBox.curselection()[0]
            self.tasksList.completeTask(i)
            self.showTasks()
        except IndexError:
            messagebox.showerror("ERROR", "Primero selecciona una tarea")
        except ValueError as e:
            messagebox.showerror("ERROR", str(e))
    
    def deleteTask(self):
        try:
            i = self.tasksListBox.curselection()[0]
            self.tasksList.deleteTask(i)
            self.showTasks()
        except IndexError:
            messagebox.showerror("ERROR", "Primero selecciona una tarea")
        except ValueError as e:
            messagebox.showerror("ERROR", str(e))
            
    def showTasks(self):
        self.taskListBox.delete(0,tk.END)
        for task in self.taskList.showTask():
            self.taskListBox.insert(tk.END, str(task))
        
if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
        
        
    