import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb
from controller.db_controller import Db_controller as Controller


class Categoria:

    def __init__(self, cuaderno):
        self.Controller = Controller()
        self.cuaderno1 = cuaderno

    def form_cat(self):
        # Tabla
        self.pagina1 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina1, text="TABLA CATEGORÍA")

        self.labelframe1 = ttk.LabelFrame(self.pagina1, text="Categoría")
        self.labelframe1.grid(column=0, row=0, padx=5, pady=10)
        self.label1 = ttk.Label(self.labelframe1, text="IdCategoría:")
        self.label1.grid(column=0, row=0, padx=4, pady=4)
        self.idcat_tipo = tk.IntVar()
        self.entry_id = ttk.Entry(self.labelframe1, textvariable=self.idcat_tipo)
        self.entry_id.grid(column=1, row=0, padx=4, pady=4)

        self.label2 = ttk.Label(self.labelframe1, text="Categoría:")
        self.label2.grid(column=0, row=1, padx=4, pady=4)
        self.cat_tipo = tk.StringVar()
        self.entry_cat = ttk.Entry(self.labelframe1, textvariable=self.cat_tipo)
        self.entry_cat.grid(column=1, row=1, padx=4, pady=4)

        self.boton1 = ttk.Button(self.labelframe1, text="Añadir Registro a Categoría",
                                 command=self.agregar_cat)
        self.boton1.grid(column=1, row=2, padx=4, pady=4)

        self.boton2 = ttk.Button(self.labelframe1, text="Actualizar Categoría",
                                 command=self.update_categoria)
        self.boton2.grid(column=1, row=3, padx=4, pady=4)

        self.delcategoria = tk.IntVar()
        self.delete_categoria_input = ttk.Entry(self.labelframe1, textvariable=self.delcategoria)
        self.delete_categoria_input.grid(column=0, row=4, padx=4, pady=4)
        self.boton3 = ttk.Button(self.labelframe1, text="Borrar Categoría",
                                 command=self.delete_categoria)
        self.boton3.grid(column=1, row=4, padx=4, pady=4)

        self.boton4 = ttk.Button(self.labelframe1, text="Ordenar por idCategoría",
                                 command=self.order_byId)
        self.boton4.grid(column=1, row=5, padx=4, pady=4)

    def agregar_cat(self):
        datos = (self.idcat_tipo.get(), self.cat_tipo.get())
        self.Controller.add_categoria(datos)
        mb.showinfo("Información", "Categoría Añadida")
        self.idcat_tipo.set(0)
        self.cat_tipo.set("")

    def update_categoria(self):
        datos = (self.cat_tipo.get(), self.idcat_tipo.get())
        self.Controller.update_categoria(datos)
        mb.showinfo("Información", "Categoría actualizada")
        self.idcat_tipo.set(0)
        self.cat_tipo.set("")

    def delete_categoria(self):
        datos = (self.delcategoria.get(),)
        self.Controller.delete_categoria(datos)
        mb.showinfo("Información", "Categoría eliminada")
        self.delcategoria.set(0)

    def order_byId(self):
        self.Controller.order_categoria_byId()

