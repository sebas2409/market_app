import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb
from controller.db_controller import Db_controller as Controller


class Cliente:
    def __init__(self, cuaderno):
        self.Controller = Controller()
        self.cuaderno1 = cuaderno

    def form_cliente(self):
        self.pagina1 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina1, text="TABLA CLIENTE")
        self.labelframe1 = ttk.LabelFrame(self.pagina1, text="Cliente")
        self.labelframe1.grid(column=0, row=0, padx=5, pady=10)

        self.label1 = ttk.Label(self.labelframe1, text="IdCliente:")
        self.label1.grid(column=0, row=0, padx=4, pady=4)
        self.idcliente_tipo = tk.StringVar()
        self.entry_idcliente = ttk.Entry(self.labelframe1, textvariable=self.idcliente_tipo)
        self.entry_idcliente.grid(column=1, row=0, padx=4, pady=4)

        self.label2 = ttk.Label(self.labelframe1, text="Cia:")
        self.label2.grid(column=0, row=1, padx=4, pady=4)
        self.cia_tipo = tk.StringVar()
        self.entry_cia = ttk.Entry(self.labelframe1, textvariable=self.cia_tipo)
        self.entry_cia.grid(column=1, row=1, padx=4, pady=4)

        self.label3 = ttk.Label(self.labelframe1, text="Contacto:")
        self.label3.grid(column=0, row=2, padx=4, pady=4)
        self.contacto_tipo = tk.StringVar()
        self.entry_contacto = ttk.Entry(self.labelframe1, textvariable=self.contacto_tipo)
        self.entry_contacto.grid(column=1, row=2, padx=4, pady=4)

        self.label4 = ttk.Label(self.labelframe1, text="Cargo:")
        self.label4.grid(column=0, row=3, padx=4, pady=4)
        self.cargo_tipo = tk.StringVar()
        self.entry_cargo = ttk.Entry(self.labelframe1, textvariable=self.cargo_tipo)
        self.entry_cargo.grid(column=1, row=3, padx=4, pady=4)

        self.label5 = ttk.Label(self.labelframe1, text="Dirección:")
        self.label5.grid(column=0, row=4, padx=4, pady=4)
        self.direccion_tipo = tk.StringVar()
        self.entry_direccion = ttk.Entry(self.labelframe1, textvariable=self.direccion_tipo)
        self.entry_direccion.grid(column=1, row=4, padx=4, pady=4)

        self.label6 = ttk.Label(self.labelframe1, text="Ciudad:")
        self.label6.grid(column=0, row=5, padx=4, pady=4)
        self.ciudad_tipo = tk.StringVar()
        self.entry_ciudad = ttk.Entry(self.labelframe1, textvariable=self.ciudad_tipo)
        self.entry_ciudad.grid(column=1, row=5, padx=4, pady=4)

        self.label6 = ttk.Label(self.labelframe1, text="Región:")
        self.label6.grid(column=0, row=6, padx=4, pady=4)
        self.region_tipo = tk.StringVar()
        self.entry_region = ttk.Entry(self.labelframe1, textvariable=self.region_tipo)
        self.entry_region.grid(column=1, row=6, padx=4, pady=4)

        self.label6 = ttk.Label(self.labelframe1, text="Cod Postal:")
        self.label6.grid(column=0, row=7, padx=4, pady=4)
        self.cp_tipo = tk.StringVar()
        self.entry_cp = ttk.Entry(self.labelframe1, textvariable=self.cp_tipo)
        self.entry_cp.grid(column=1, row=7, padx=4, pady=4)

        self.label6 = ttk.Label(self.labelframe1, text="País:")
        self.label6.grid(column=0, row=9, padx=4, pady=4)
        self.pais_tipo = tk.StringVar()
        self.entry_pais = ttk.Entry(self.labelframe1, textvariable=self.pais_tipo)
        self.entry_pais.grid(column=1, row=9, padx=4, pady=4)

        self.label6 = ttk.Label(self.labelframe1, text="Teléfono:")
        self.label6.grid(column=0, row=10, padx=4, pady=4)
        self.tlf_tipo = tk.StringVar()
        self.entry_tlf = ttk.Entry(self.labelframe1, textvariable=self.tlf_tipo)
        self.entry_tlf.grid(column=1, row=10, padx=4, pady=4)

        self.label6 = ttk.Label(self.labelframe1, text="Fax:")
        self.label6.grid(column=0, row=11, padx=4, pady=4)
        self.fax_tipo = tk.StringVar()
        self.entry_fax = ttk.Entry(self.labelframe1, textvariable=self.fax_tipo)
        self.entry_fax.grid(column=1, row=11, padx=4, pady=4)

        self.boton1 = ttk.Button(self.labelframe1, text="Añadir Registro a Cliente", command=self.agregar_cli)
        self.boton1.grid(column=0, row=12, padx=4, pady=4)

        self.boton3 = ttk.Button(self.labelframe1, text="Actualizar a Cliente", command=self.update_cli)
        self.boton3.grid(column=0, row=13, padx=4, pady=4)

        self.boton2 = ttk.Button(self.labelframe1, text="Borrar Cliente por ID", command=self.delete_cli)
        self.boton2.grid(column=0, row=14, padx=4, pady=4)
        self.idEntry = tk.StringVar()
        self.idEntryInput = ttk.Entry(self.labelframe1, textvariable=self.idEntry)
        self.idEntryInput.grid(column=1, row=14, padx=4, pady=4)

        self.boton100 = ttk.Button(self.labelframe1, text="Ordenar por id", command=self.order_by_id)
        self.boton100.grid(column=0, row=15, padx=4, pady=4)

        self.boton101 = ttk.Button(self.labelframe1, text="Obtener gráfica de clientes",
                                   command=self.obtener_grafica_por_id)
        self.boton101.grid(column=0, row=16, pady=4, padx=5)

    def agregar_cli(self):
        datos = (self.idcliente_tipo.get(), self.cia_tipo.get(), self.contacto_tipo.get(), self.cargo_tipo.get(),
                 self.direccion_tipo.get(), self.ciudad_tipo.get(), self.region_tipo.get(), self.cp_tipo.get(),
                 self.pais_tipo.get(), self.tlf_tipo.get(), self.fax_tipo.get())

        mb.showinfo("Información", "Cliente añadido")
        self.Controller.add_cliente(datos)
        self.idcliente_tipo.set("")
        self.cia_tipo.set("")
        self.contacto_tipo.set("")
        self.cargo_tipo.set("")
        self.direccion_tipo.set("")
        self.ciudad_tipo.set("")
        self.region_tipo.set("")
        self.cp_tipo.set("")
        self.pais_tipo.set("")
        self.tlf_tipo.set("")
        self.fax_tipo.set("")

    def update_cli(self):
        datos = (self.cia_tipo.get(), self.contacto_tipo.get(), self.cargo_tipo.get(),
                 self.direccion_tipo.get(), self.ciudad_tipo.get(), self.region_tipo.get(), self.cp_tipo.get(),
                 self.pais_tipo.get(), self.tlf_tipo.get(), self.fax_tipo.get(), self.idcliente_tipo.get())

        mb.showinfo("Información", "Cliente actualizado")
        self.Controller.update_cliente(datos)
        self.idcliente_tipo.set("")
        self.cia_tipo.set("")
        self.contacto_tipo.set("")
        self.cargo_tipo.set("")
        self.direccion_tipo.set("")
        self.ciudad_tipo.set("")
        self.region_tipo.set("")
        self.cp_tipo.set("")
        self.pais_tipo.set("")
        self.tlf_tipo.set("")
        self.fax_tipo.set("")

    def delete_cli(self):
        datos = (self.idEntry.get(),)
        self.Controller.delete_client(datos)
        mb.showinfo("Información", "Usuario Eliminado")
        self.idcliente_tipo.set("")

    def order_by_id(self):
        self.Controller.order_by_id()

    def obtener_grafica_por_id(self):
        self.Controller.obtener_grafica_cliente()
