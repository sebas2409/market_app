import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb
from controller.db_controller import Db_controller as Controller


class Table_droper:
    def __init__(self, cuaderno):
        self.Controller = Controller()
        self.cuaderno1 = cuaderno

    def form_drop_table(self):
        self.pagina1 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina1, text="BORRAR NUEVA TABLA")
        self.labelframe1 = ttk.LabelFrame(self.pagina1, text="Borrar Tabla")
        self.labelframe1.grid(column=0, row=0, padx=5, pady=10)

        self.label1 = ttk.Label(self.labelframe1, text="Borrar tabla:")
        self.label1.grid(column=0, row=2, padx=4, pady=4)

        self.nombreborrar_tipo = tk.StringVar()
        self.input_nombreborrar = ttk.Entry(self.labelframe1, textvariable=self.nombreborrar_tipo)
        self.input_nombreborrar.grid(column=1, row=2, padx=4, pady=4)

        self.boton1 = ttk.Button(self.labelframe1, text="Borrar Tabla", command=self.drop_table)
        self.boton1.grid(column=0, row=3, padx=4, pady=4)

    def drop_table(self):
        tabla = (self.nombreborrar_tipo.get(),)
        self.Controller.drop_table(tabla)
        mb.showinfo("Información", "Tabla Borrada!")
