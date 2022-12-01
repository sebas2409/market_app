import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb
from controller.db_controller import Db_controller as Controller


class Pedido:

    def __init__(self, cuaderno):
        self.Controller = Controller()
        self.cuaderno1 = cuaderno

    def form_pedido(self):
        self.pagina1 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina1, text="Añadir un pedido")
        self.labelframe1 = ttk.LabelFrame(self.pagina1, text="Pedido")
        self.labelframe1.grid(column=0, row=0, padx=5, pady=10)

        self.label1 = ttk.Label(self.labelframe1, text="Id pedido:")
        self.label1.grid(column=0, row=0, padx=4, pady=4)
        self.idpedido_tipo = tk.StringVar()
        self.entry_idpedido = ttk.Entry(self.labelframe1, textvariable=self.idpedido_tipo)
        self.entry_idpedido.grid(column=1, row=0, padx=4, pady=4)

        self.label1 = ttk.Label(self.labelframe1, text="Id cliente:")
        self.label1.grid(column=0, row=1, padx=4, pady=4)
        self.idcliente_tipo = tk.StringVar()
        self.entry_idcliente = ttk.Entry(self.labelframe1, textvariable=self.idcliente_tipo)
        self.entry_idcliente.grid(column=1, row=1, padx=4, pady=4)

        self.label2 = ttk.Label(self.labelframe1, text="Fecha pedido:")
        self.label2.grid(column=0, row=2, padx=4, pady=4)
        self.fechaP_tipo = tk.StringVar()
        self.entry_fechaP = ttk.Entry(self.labelframe1, textvariable=self.fechaP_tipo)
        self.entry_fechaP.grid(column=1, row=2, padx=4, pady=4)

        self.label2 = ttk.Label(self.labelframe1, text="Fecha entrega:")
        self.label2.grid(column=0, row=3, padx=4, pady=4)
        self.fechaE_tipo = tk.StringVar()
        self.entry_fechaE = ttk.Entry(self.labelframe1, textvariable=self.fechaE_tipo)
        self.entry_fechaE.grid(column=1, row=3, padx=4, pady=4)

        self.boton1 = ttk.Button(self.labelframe1, text="Añadir Registro a Pedido",
                                 command=self.agregar_pedido)  # ! importante llamar a las funcineos
        self.boton1.grid(column=1, row=4, padx=4, pady=4)
        self.boton2 = ttk.Button(self.labelframe1, text="Borrar Pedido por ID")

    def agregar_pedido(self):
        datos = (self.idpedido_tipo.get(), self.idcliente_tipo.get(), self.fechaP_tipo.get(), self.fechaE_tipo.get())
        self.Controller.add_pedido(datos)
        mb.showinfo("Información", "Pedido Añadido")
        self.idpedido_tipo.set(0)
        self.idcliente_tipo.set(0)
        self.fechaP_tipo.set("")
        self.fechaE_tipo.set("")

    def update_pedido(self):
        datos = (self.idpedido_tipo.get(), self.idcliente_tipo.get(), self.fechaP_tipo.get(), self.fechaE_tipo.get())
        self.Controller.add_pedido(datos)
        mb.showinfo("Información", "Pedido actualizado")
        self.idpedido_tipo.set(0)
        self.idcliente_tipo.set(0)
        self.fechaP_tipo.set("")
        self.fechaE_tipo.set("")
