import tkinter as tk
from tkinter import messagebox

class Tarea:
    def __init__(self, num, name, desc):
        self.num = num
        self.name = name
        self.desc = desc
        self.completada = False
    
    def completarTarea(self):
        self.completada = True
    
    def __str__(self):
        estado = "Completada" if self.completada else "Pendiente"
        return f"Tarea {self.num}: {self.name} - {estado}"
    