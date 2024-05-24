import tkinter as tk
from tkinter import messagebox

class Tarea:
    def __init__(self, name, desc):
        self.name = name
        self.desc = desc
        self.complete = False
    
    def completeTask(self):
        self.complete = True
    
    def __str__(self):
        state = "Completada" if self.complete else "Pendiente"
        return f"Tarea {self.name}: {self.desc} - {state}"
    
class ListaTareas:
    def __init__(self):
        self.tasks = []

    def addTask(self, name, desc):
        task = Tarea(name, desc)
        self.tasks.append(task)

    def completeTask(self, i):
        try:
            self.tasks[i].completeTask()
        except IndexError:
            raise ValueError("No existe ninguna tarea con ese índice")
    
    def deleteTask(self, i):
        try:
            self.tasks.pop(i)
        except IndexError:
            raise ValueError("No existe ninguna tarea con ese índice") 
    