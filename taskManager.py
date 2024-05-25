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
        
    # Metodo que pone el atributo estado como penndiente
    def notCompleteTask(self):
        self.complete = False
    
    #Este método coge el color de fondo dependiendo si la tarea es pendiente o completa
    def get_background_color(self):
        state = "Pendiente" if not self.complete else "Completada"
        return "yellow" if state == "Pendiente" else "green"

    # Es un método que devuelve un string con información sobre la Tarea
    def __str__(self):
        state = "Completada" if self.complete else "Pendiente"
        return f"{self.name:^10} {'|':^10} {self.desc:^10} {'|':^10} {state:^10}"
    
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
        
    # Este método pone la tarea en estado pendiente
    def notCompleteTask(self, i):
        try:
            self.tasks[i].notCompleteTask()
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

        # Creamos la ventana y ajustamos los márgenes. Aqui he dado colores al fondo para que se vea más estético
        root.configure(bg="lightblue")
        self.frame = tk.Frame(root, bg="lightblue")
        self.frame.pack(pady=20, expand=True, fill='both')

        # Ponemos el título y le aplicamos los estilos y margenes
        self.text = tk.Label(root, text="Gestor de tareas", font=("Helvetica", 28, "italic"), fg="green", bg="lightblue")
        self.text.pack(padx=5, pady=5)
        
        self.frame = tk.Frame(root, bg="lightblue")
        self.frame.pack(padx=10, pady=10, expand=True, fill='both')

        # Creamos la etiqueta Nombre de la tarea y le damos un tamaño, tambien creamos el input para que lo use el usuario
        self.labelName = tk.Label(self.frame, text="Nombre de la Tarea:", bg="lightblue")
        self.labelName.grid(row=0, column=0)
        self.entryName = tk.Entry(self.frame)
        self.entryName.grid(row=0, column=1)
        
        # Creamos la etiqueta Descripción y le damos un tamaño, tambien creamos el input para que lo use el usuario
        self.labelDesc = tk.Label(self.frame, text="Descripción:", bg="lightblue")
        self.labelDesc.grid(row=1, column=0)
        self.entryDesc = tk.Entry(self.frame)
        self.entryDesc.grid(row=1, column=1)
        
        # Botón de agregar tarea con estilos para ser más estético y unido a la función addTask que hace la funcionalidad del mismo
        self.addBtn = tk.Button(self.frame,text="AGREGAR TAREA", command=self.addTask, bg="navy", fg="white", font=("Helvetica", 10, "bold"), relief="raised", bd=5, padx=5, pady=3)
        self.addBtn.grid(row=2, columnspan=2, pady=10)
        
        # Recuadro blanco donde posteriormente se mostrarán todas nuestras tareas
        self.tasksListBox = tk.Listbox(self.frame, width=50, height=10)
        self.tasksListBox.grid(row=3, columnspan=3, pady=10)
        
        # Botón de completar tarea con estilos para ser más estético y unido a la función completeTask que hace la funcionalidad del mismo
        self.completeBtn = tk.Button(self.frame,text="COMPLETAR TAREA", command=self.completeTask, bg="navy", fg="white", font=("Helvetica", 10, "bold"), relief="raised", bd=5, padx=5, pady=3)
        self.completeBtn.grid(row=4, column=0, padx=(0, 5), pady=5)
        
        # Botón de completar tarea con estilos para ser más estético y unido a la función notCompleteTask que hace la funcionalidad del mismo
        self.completeBtn = tk.Button(self.frame,text="TAREA PENDIENTE", command=self.notCompleteTask, bg="navy", fg="white", font=("Helvetica", 10, "bold"), relief="raised", bd=5, padx=5, pady=3)
        self.completeBtn.grid(row=4, column=1, padx=(5, 0), pady=5)
       
        # Botón de eliminar tarea seleccionada con estilos para ser más estético y unido a la función deleteTask que hace la funcionalidad del mismo
        self.deleteBtn = tk.Button(self.frame,text="ELIMINAR TAREA", command=self.deleteTask, bg="navy", fg="white", font=("Helvetica", 10, "bold"), relief="raised", bd=5, padx=5, pady=3)
        self.deleteBtn.grid(row=5, columnspan=2, pady=5)
        
        # Llamamos al método para mostrar las tareas
        self.showTasks()
        
    # Función que permite añadir una tarea
    def addTask(self):
        # Cogemos el nombre y la descripción
        name = self.entryName.get()
        desc = self.entryDesc.get()
        
        if not name:
            # Mostrar mensaje de error en caso de que no se haya indicado nombre para la tarea
            messagebox.showerror("Aviso", "La tarea debe tener un nombre")
        else:
            #Lo añade a la lista y vacia el campo input
            self.taskList.addTask(name, desc)
            self.showTasks()
            self.entryName.delete(0, tk.END)
            self.entryDesc.delete(0, tk.END)
    
    # Función para completar la tarea        
    def completeTask(self):
        # Control de errores en caso de fallo
        try:
            # Cogemos el índice de la tarea seleccionada y conociendo el indice llamamos a completeTask
            i = self.tasksListBox.curselection()[0]
            self.taskList.completeTask(i)
            self.showTasks()
        except IndexError:
            # Salta el error en caso de que el usuario no haya seleccionado ninguna tarea
            messagebox.showerror("ERROR", "Primero selecciona una tarea")
        except ValueError as e:
            messagebox.showerror("ERROR", str(e))
    
    # Parecida a la funcion anterior pero cuando queremos poner la tarea como pendiente de nuevo
    def notCompleteTask(self):
        try:
            i = self.tasksListBox.curselection()[0]
            self.taskList.notCompleteTask(i)
            self.showTasks()
        except IndexError:
            messagebox.showerror("ERROR", "Primero selecciona una tarea")
        except ValueError as e:
            messagebox.showerror("ERROR", str(e))
    
    # Función que controla la eliminación de la tarea
    def deleteTask(self):
        try:
            # Cogemos el índice y se lo pasamos a la funcion del objeto
            i = self.tasksListBox.curselection()[0]
            self.taskList.deleteTask(i)
            self.showTasks()
        except IndexError:
            messagebox.showerror("ERROR", "Primero selecciona una tarea")
        except ValueError as e:
            messagebox.showerror("ERROR", str(e))
            
    # Función que muestra todas las tareas y por tanto es llamada cada vez que se agrega, elimina o modifica una tarea        
    def showTasks(self):
        self.tasksListBox.delete(0,tk.END)
        # Recorremos la lista de tareas y mostramos las tareas y le damos un color de fondo dependiendo de su state
        for task in self.taskList.showTasks():
            # self.tasksListBox.insert(tk.END, str(task).replace("|", " | "))  
            task_str, bg_color = str(task), task.get_background_color()
            self.tasksListBox.insert(tk.END, task_str.replace("|", " | "))
            self.tasksListBox.itemconfig(tk.END, {'bg': bg_color})   
        
# Ejecución de la página garantizando el uso de tkinter
if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
        
        
    