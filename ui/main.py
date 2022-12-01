import tkinter as tk
from tkinter import ttk
from controller.db_controller import Db_controller as Controller
from ui.categoria import Categoria
from ui.cliente import Cliente
from ui.pedido import Pedido
from ui.producto import Producto


class FormularioTablas:
    def __init__(self):
        self.Controller = Controller()
        self.ventana1 = tk.Tk()
        self.ventana1.title("Gestión de Supermercado")
        self.cuaderno1 = ttk.Notebook(self.ventana1)

        self.Categoria = Categoria(cuaderno=self.cuaderno1)
        self.Cliente = Cliente(cuaderno=self.cuaderno1)
        self.Pedido = Pedido(cuaderno=self.cuaderno1)
        self.Producto = Producto(cuaderno=self.cuaderno1)
        self.Categoria.form_cat()
        self.Cliente.form_cliente()
        self.Pedido.form_pedido()
        self.Producto.tabla_productos()

        self.cuaderno1.grid(column=0, row=0, padx=10, pady=10)
        self.ventana1.mainloop()


aplicacion1 = FormularioTablas()
