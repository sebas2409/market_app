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
        self.cuaderno1.add(self.pagina1, text="TABLA PEDIDO")
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
                                 command=self.agregar_pedido)
        self.boton1.grid(column=1, row=4, padx=4, pady=4)

        self.boton2 = ttk.Button(self.labelframe1, text="Actualizar Pedido",
                                 command=self.update_pedido)
        self.boton2.grid(column=1, row=5, padx=4, pady=4)

        self.boton5 = ttk.Button(self.labelframe1, text="Borrar Pedido por ID", command=self.delete_pedido_byId)
        self.boton5.grid(column=1, row=7, padx=4, pady=4)
        self.idpedido_delete = tk.IntVar()
        self.input_idpedido_delete = ttk.Entry(self.labelframe1, textvariable=self.idpedido_delete)
        self.input_idpedido_delete.grid(column=2, row=7, padx=4, pady=4)

        self.boton4 = ttk.Button(self.labelframe1, text="Productos de idCliente: ", command=self.select_pedido_byIdCli)
        self.boton4.grid(column=1, row=6, padx=4, pady=4)
        self.idcli_select = tk.StringVar()
        self.entry_idcli_update = ttk.Entry(self.labelframe1, textvariable=self.idcli_select)
        self.entry_idcli_update.grid(column=2, row=6, padx=4, pady=4)

        self.boton5 = ttk.Button(self.labelframe1, text="Productos ordenados", command=self.select_pedido_ordenado)
        self.boton5.grid(column=1, row=8, padx=4, pady=4)

    def agregar_pedido(self):
        datos = (self.idpedido_tipo.get(), self.idcliente_tipo.get(), self.fechaP_tipo.get(), self.fechaE_tipo.get())
        self.Controller.add_pedido(datos)
        mb.showinfo("Información", "Pedido Añadido")
        self.idpedido_tipo.set("")
        self.idcliente_tipo.set("")
        self.fechaP_tipo.set("")
        self.fechaE_tipo.set("")

    def update_pedido(self):
        datos = (self.fechaP_tipo.get(), self.fechaE_tipo.get(), self.idpedido_tipo.get())
        self.Controller.update_pedido(datos)
        mb.showinfo("Información", "Pedido actualizado")
        self.idpedido_tipo.set("")
        self.idcliente_tipo.set("")
        self.fechaP_tipo.set("")
        self.fechaE_tipo.set("")

    def select_pedido_byIdCli(self):
        data_idcliente = (self.idcli_select.get(),)
        self.Controller.select_pedido_byIdCli(data_idcliente)

    def select_pedido_ordenado(self):
        self.Controller.select_pedido_ordenado()

    def delete_pedido_byId(self):
        data_delete = (self.idpedido_delete.get(),)
        self.Controller.delete_pedido_byId(data_delete)
        mb.showinfo("Información", "Pedido eliminado")
