import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb
from controller.db_controller import Db_controller as Controller


# Clase


class Producto:

    def __init__(self, cuaderno):
        self.Controller = Controller()
        self.cuaderno1 = cuaderno

    def tabla_productos(self):
        # Tabla producto
        self.paginaProductos = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.paginaProductos, text="TABLA PRODUCTO")
        self.labelFrame1 = ttk.LabelFrame(self.paginaProductos, text="Producto")
        self.labelFrame1.grid(column=0, row=0, padx=5, pady=10)

        # ID producto
        self.label1 = ttk.Label(self.labelFrame1, text="id Producto: ")
        self.label1.grid(column=0, row=0, padx=4, pady=4)
        self.id_producto = tk.StringVar()
        self.id_producto_input = ttk.Entry(self.labelFrame1, textvariable=self.id_producto)
        self.id_producto_input.grid(column=1, row=0, padx=4, pady=4)

        # Nombre
        self.label1 = ttk.Label(self.labelFrame1, text="Nombre: ")
        self.label1.grid(column=0, row=1, padx=4, pady=4)
        self.nombre = tk.StringVar()
        self.nombreInput = ttk.Entry(self.labelFrame1, textvariable=self.nombre)
        self.nombreInput.grid(column=1, row=1, padx=4, pady=4)

        # ID categoria
        self.label1 = ttk.Label(self.labelFrame1, text="Id Categoria: ")
        self.label1.grid(column=0, row=2, padx=4, pady=4)
        self.id_categoria = tk.IntVar()
        self.nombreInput = ttk.Entry(self.labelFrame1, textvariable=self.id_categoria)
        self.nombreInput.grid(column=1, row=2, padx=4, pady=4)

        # Medida
        self.label1 = ttk.Label(self.labelFrame1, text="Medida: ")
        self.label1.grid(column=0, row=3, padx=4, pady=4)
        self.medida = tk.StringVar()
        self.nombreInput = ttk.Entry(self.labelFrame1, textvariable=self.medida)
        self.nombreInput.grid(column=1, row=3, padx=4, pady=4)

        # Precio
        self.label1 = ttk.Label(self.labelFrame1, text="Precio: ")
        self.label1.grid(column=0, row=4, padx=4, pady=4)
        self.precio = tk.IntVar()
        self.nombreInput = ttk.Entry(self.labelFrame1, textvariable=self.precio)
        self.nombreInput.grid(column=1, row=4, padx=4, pady=4)

        # Stock
        self.label1 = ttk.Label(self.labelFrame1, text="Stock: ")
        self.label1.grid(column=0, row=5, padx=5, pady=4)
        self.stock = tk.IntVar()
        self.stockInput = ttk.Entry(self.labelFrame1, textvariable=self.stock)
        self.stockInput.grid(column=1, row=5, padx=4, pady=4)

        # Productos de la categoria

        self.productByCategoria = tk.IntVar()
        self.productByCategoriaInput = ttk.Entry(self.labelFrame1, textvariable=self.productByCategoria)
        self.productByCategoriaInput.grid(column=0, row=6, padx=4, pady=4)
        self.boton5 = ttk.Button(self.labelFrame1, text="Buscar por categoría",
                                 command=self.search_products_by_category)
        self.boton5.grid(column=1, row=6, padx=5, pady=4)

        # Añadir a producto
        self.boton3 = ttk.Button(self.labelFrame1, text="Añadir a Producto",
                                 command=self.agregar_producto)
        self.boton3.grid(column=0, row=7, padx=4, pady=4)

        # Actualizar producto
        self.boton4 = ttk.Button(self.labelFrame1, text="Actualizar Producto",
                                 command=self.update_producto)
        self.boton4.grid(column=0, row=8, padx=4, pady=4)

        self.delete_product = tk.IntVar()
        self.delete_product_input = ttk.Entry(self.labelFrame1, textvariable=self.delete_product)
        self.delete_product_input.grid(column=1, row=9, padx=4, pady=4)
        self.boton5 = ttk.Button(self.labelFrame1, text="Borrar por IDProducto",
                                 command=self.delete_product_byId)  # todo:  falta agregar command a ejecutar!
        self.boton5.grid(column=2, row=9, padx=4, pady=4)

        # Obtener gráfica
        self.boton1 = ttk.Button(self.labelFrame1, text="Obtener gráfica")  # todo:  falta agregar command a ejecutar!
        self.boton1.grid(column=1, row=7, padx=4, pady=4)

        # Obtener excel
        self.boton2 = ttk.Button(self.labelFrame1, text="Obtener Excel")  # todo:  falta agregar command a ejecutar!
        self.boton2.grid(column=1, row=8, padx=4, pady=4)

        self.boton100 = ttk.Button(self.labelFrame1, text="Ordenar por id", command=self.order_by_id)
        self.boton100.grid(column=1, row=10, padx=4, pady=4)

    # Función agregar producto
    def agregar_producto(self):
        datos = (
            self.id_producto.get(),
            self.nombre.get(),
            self.id_categoria.get(),
            self.medida.get(),
            self.precio.get(),
            self.stock.get())

        self.Controller.add_producto(datos)
        mb.showinfo("Información", "Producto Añadido")

        self.nombre.set("")
        self.id_categoria.set(0)
        self.medida.set("")
        self.precio.set(0)
        self.stock.set(0)

    # Función actualizar producto
    def update_producto(self):
        datos = (
            self.nombre.get(),
            self.medida.get(),
            self.precio.get(),
            self.stock.get(),
            self.id_producto.get())

        self.Controller.update_producto(datos)
        mb.showinfo("Información", "Producto actualizado")
        self.id_producto.set("")
        self.nombre.set("")
        self.medida.set("")
        self.precio.set(0)
        self.stock.set(0)

    # Función buscar productos
    def search_products_by_category(self):
        datos = (self.productByCategoria.get(),)
        self.Controller.searchProductByCategory(datos)
        mb.showinfo("Información", "Productos obtenidos")
        self.productByCategoria.set(0)

    def delete_product_byId(self):
        datos = (self.delete_product_input.get(),)
        self.Controller.delete_product_byId(datos)
        mb.showinfo("Información", "Producto Eliminado")

    def order_by_id(self):
        self.Controller.order_product_by_id()
