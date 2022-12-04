import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb
from controller.db_controller import Db_controller as Controller


class Table_creator:
    def __init__(self, cuaderno):
        self.Controller = Controller()
        self.cuaderno1 = cuaderno

    def form_create_table(self):
        self.pagina1 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina1, text="CREAR NUEVA TABLA")
        self.labelframe1 = ttk.LabelFrame(self.pagina1, text="Nueva Tabla")
        self.labelframe1.grid(column=0, row=0, padx=5, pady=10)

        self.label1 = ttk.Label(self.labelframe1, text="Nombre Tabla:")
        self.label1.grid(column=0, row=0, padx=4, pady=4)
        self.nombre_tipo = tk.StringVar()
        self.input_nombre = ttk.Entry(self.labelframe1, textvariable=self.nombre_tipo)
        self.input_nombre.grid(column=1, row=0, padx=4, pady=4)

        self.label1 = ttk.Label(self.labelframe1, text="Nombre Columna 1:")
        self.label1.grid(column=0, row=1, padx=4, pady=4)
        self.nombrecol1_tipo = tk.StringVar()
        self.input_nombrecol1 = ttk.Entry(self.labelframe1, textvariable=self.nombrecol1_tipo)
        self.input_nombrecol1.grid(column=1, row=1, padx=4, pady=4)


        self.label1 = ttk.Label(self.labelframe1, text="Nombre Columna 2:")
        self.label1.grid(column=0, row=2, padx=4, pady=4)
        self.nombrecol2_tipo = tk.StringVar()
        self.input_nombrecol2 = ttk.Entry(self.labelframe1, textvariable=self.nombrecol2_tipo)
        self.input_nombrecol2.grid(column=1, row=2, padx=4, pady=4)

        self.boton1 = ttk.Button(self.labelframe1, text="Añadir Nueva Tabla", command=self.create_new_table)
        self.boton1.grid(column=0, row=3, padx=4, pady=4)

    def create_new_table(self):
        datos = (self.nombre_tipo.get(), self.nombrecol1_tipo.get(), self.nombrecol2_tipo.get(),)
        self.Controller.create_new_table(datos)
        mb.showinfo("Información", "Nueva Tabla Creada!")
