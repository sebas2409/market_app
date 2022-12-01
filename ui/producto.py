import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb
from controller.db_controller import Db_controller as Controller


class Producto:

    def __init__(self, cuaderno):
        self.Controller = Controller()
        self.cuaderno1 = cuaderno

    def tabla_productos(self):
        self.paginaProductos = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.paginaProductos, text="Añadir a productos")
        self.labelFrame1 = ttk.LabelFrame(self.paginaProductos, text="Producto")
        self.labelFrame1.grid(column=0, row=0, padx=5, pady=10)

        self.label1 = ttk.Label(self.labelFrame1, text="id Producto: ")
        self.label1.grid(column=0, row=0, padx=4, pady=4)
        self.id_producto = tk.StringVar()
        self.id_producto_input = ttk.Entry(self.labelFrame1, textvariable=self.id_producto)
        self.id_producto_input.grid(column=1, row=0, padx=4, pady=4)

        self.label1 = ttk.Label(self.labelFrame1, text="Nombre: ")
        self.label1.grid(column=0, row=1, padx=4, pady=4)
        self.nombre = tk.StringVar()
        self.nombreInput = ttk.Entry(self.labelFrame1, textvariable=self.nombre)
        self.nombreInput.grid(column=1, row=1, padx=4, pady=4)

        self.label1 = ttk.Label(self.labelFrame1, text="Id Categoria: ")
        self.label1.grid(column=0, row=2, padx=4, pady=4)
        self.id_categoria = tk.IntVar()
        self.nombreInput = ttk.Entry(self.labelFrame1, textvariable=self.id_categoria)
        self.nombreInput.grid(column=1, row=2, padx=4, pady=4)

        self.label1 = ttk.Label(self.labelFrame1, text="Medida: ")
        self.label1.grid(column=0, row=3, padx=4, pady=4)
        self.medida = tk.StringVar()
        self.nombreInput = ttk.Entry(self.labelFrame1, textvariable=self.medida)
        self.nombreInput.grid(column=1, row=3, padx=4, pady=4)

        self.label1 = ttk.Label(self.labelFrame1, text="Precio: ")
        self.label1.grid(column=0, row=4, padx=4, pady=4)
        self.precio = tk.IntVar()
        self.nombreInput = ttk.Entry(self.labelFrame1, textvariable=self.precio)
        self.nombreInput.grid(column=1, row=4, padx=4, pady=4)

        self.label1 = ttk.Label(self.labelFrame1, text="Stock: ")
        self.label1.grid(column=0, row=5, padx=5, pady=4)
        self.stock = tk.IntVar()
        self.nombreInput = ttk.Entry(self.labelFrame1, textvariable=self.stock)
        self.nombreInput.grid(column=1, row=5, padx=4, pady=4)

        self.boton3 = ttk.Button(self.labelFrame1, text="Añadir a Producto",
                                 command=self.agregar_producto)
        self.boton3.grid(column=0, row=6, padx=4, pady=4)

        self.boton1 = ttk.Button(self.labelFrame1, text="Obtener gráfica")  # todo:  falta agregar command a ejecutar!
        self.boton1.grid(column=0, row=7, padx=4, pady=4)

        self.boton2 = ttk.Button(self.labelFrame1, text="Obtener Excel")  # todo:  falta agregar command a ejecutar!
        self.boton2.grid(column=1, row=7, padx=4, pady=4)

    def agregar_producto(self):
        datos = (
            self.id_producto.get(),
            self.idproducto_tipo.get(),
            self.nombre.get(),
            self.id_categoria.get(),
            self.medida.get(),
            self.precio.get(),
            self.stock.get())

        self.Controller.add_producto(datos)
        mb.showinfo("Información", "Producto Añadido")
        self.idproducto_tipo.set("")
        self.nombre.set("")
        self.id_categoria.set("")
        self.medida.set("")
        self.precio.set("")
        self.stock.set("")
