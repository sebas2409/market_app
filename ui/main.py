import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb

from controller.db_controller import Db_controller as Controller


class FormularioTablas:
    def __init__(self):
        self.Controller = Controller()
        self.ventana1 = tk.Tk()
        self.ventana1.title("Gestión de Supermercado")
        self.cuaderno1 = ttk.Notebook(self.ventana1)
        self.form_cat()
        self.form_cliente()
        self.tabla_productos()
        self.form_pedido()
        self.form_detalle()
        self.cuaderno1.grid(column=0, row=0, padx=10, pady=10)
        self.ventana1.mainloop()

    # Formulario tabla categoría
    def form_cat(self):
        self.pagina1 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina1, text="Añadir a Categoría")

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

    # Formulario tabla cliente
    def form_cliente(self):
        self.pagina1 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina1, text="Añadir a cliente")
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
        self.boton1.grid(column=1, row=12, padx=4, pady=4)
        self.boton2 = ttk.Button(self.labelframe1, text="Borrar Cliente por ID")

        self.boton3 = ttk.Button(self.labelframe1, text="Actualizar a Cliente", command=self.update_cli)
        self.boton3.grid(column=1, row=13, padx=4, pady=4)

    # Formulario tabla pedido
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

    # Formulario tabla detalle
    def form_detalle(self):
        self.pagina1 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina1, text="Añadir detalles")
        self.labelframe1 = ttk.LabelFrame(self.pagina1, text="Detalle")
        self.labelframe1.grid(column=0, row=0, padx=5, pady=10)

        self.label1 = ttk.Label(self.labelframe1, text="Id pedido:")
        self.label1.grid(column=0, row=0, padx=4, pady=4)
        self.iddetalle = tk.IntVar()
        self.iddetalle_entry = ttk.Entry(self.labelframe1, textvariable=self.iddetalle)
        self.iddetalle_entry.grid(column=1, row=0, padx=4, pady=4)

        self.label1 = ttk.Label(self.labelframe1, text="Id Producto:")
        self.label1.grid(column=0, row=1, padx=4, pady=4)
        self.idproducto_tipo = tk.IntVar()
        self.entry_idproducto = ttk.Entry(self.labelframe1, textvariable=self.idproducto_tipo)
        self.entry_idproducto.grid(column=1, row=1, padx=4, pady=4)

        self.label2 = ttk.Label(self.labelframe1, text="Precio")
        self.label2.grid(column=0, row=2, padx=4, pady=4)
        self.precioD_tipo = tk.DoubleVar()
        self.entry_precioD = ttk.Entry(self.labelframe1, textvariable=self.precioD_tipo)
        self.entry_precioD.grid(column=1, row=2, padx=4, pady=4)

        self.label2 = ttk.Label(self.labelframe1, text="Unidades")
        self.label2.grid(column=0, row=3, padx=4, pady=4)
        self.unidades_tipo = tk.IntVar()
        self.entry_unidades = ttk.Entry(self.labelframe1, textvariable=self.unidades_tipo)
        self.entry_unidades.grid(column=1, row=3, padx=4, pady=4)

        self.label2 = ttk.Label(self.labelframe1, text="Descuento")
        self.label2.grid(column=0, row=4, padx=4, pady=4)
        self.descuento_tipo = tk.IntVar()
        self.entry_descuento = ttk.Entry(self.labelframe1, textvariable=self.descuento_tipo)
        self.entry_descuento.grid(column=1, row=4, padx=4, pady=4)

        self.botonRegistro = ttk.Button(self.labelframe1, text="Añadir Registro a Detalle", command=self.agregar_detalle)
        self.botonRegistro.grid(column=1, row=5, padx=4, pady=4)
        self.botonBorrarDetalle = ttk.Button(self.labelframe1, text="Borrar Detalle por ID")
        self.botonBorrarDetalle.grid(column=1, row=6, padx=4, pady=4)

    # Formulario tabla productos
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

    # def delete_cli(self):
    #     datos = self.idcliente_tipo.get()
    #     self.Controller.delete_client(datos)
    #     mb.showinfo("Información", "Cliente eliminado")
    #     self.idcliente_tipo.set(0)

    def agregar_cat(self):
        datos = (self.idcat_tipo.get(), self.cat_tipo.get())
        self.Controller.add_categoria(datos)
        mb.showinfo("Información", "Categoría Añadida")
        self.idcat_tipo.set(0)
        self.cat_tipo.set("")

    def agregar_pedido(self):
        datos = (self.idpedido_tipo.get(), self.idcliente_tipo.get(), self.fechaP_tipo.get(), self.fechaE_tipo.get())
        self.Controller.add_pedido(datos)
        mb.showinfo("Información", "Pedido Añadido")
        self.idpedido_tipo.set(0)
        self.idcliente_tipo.set(0)
        self.fechaP_tipo.set("")
        self.fechaE_tipo.set("")

    def agregar_detalle(self):
        datos = (self.iddetalle.get(), self.idproducto_tipo.get(), self.precioD_tipo.get(), self.unidades_tipo,
                 self.descuento_tipo)
        self.Controller.add_detalle(datos)
        mb.showinfo("Información", "Detalle Añadido")
        self.iddetalle.set(0)
        self.idproducto_tipo.set(0)
        self.precioD_tipo.set(0)
        self.unidades_tipo.set(0)
        self.descuento_tipo.set(0)

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

    def update_cli(self):
        datos = (self.idcliente_tipo.get(), self.cia_tipo.get(), self.contacto_tipo.get(), self.cargo_tipo.get(),
                 self.direccion_tipo.get(), self.ciudad_tipo.get(), self.region_tipo.get(), self.cp_tipo.get(),
                 self.pais_tipo.get(), self.tlf_tipo.get(), self.fax_tipo.get())

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

    def update_categoria(self):
        datos = (self.idcat_tipo.get(), self.cat_tipo.get())
        self.Controller.update_categoria(datos)
        mb.showinfo("Información", "Categoría actualizada")
        self.idcat_tipo.set(0)
        self.cat_tipo.set("")

    def update_pedido(self):
        datos = (self.idpedido_tipo.get(), self.idcliente_tipo.get(), self.fechaP_tipo.get(), self.fechaE_tipo.get())
        self.Controller.add_pedido(datos)
        mb.showinfo("Información", "Pedido actualizado")
        self.idpedido_tipo.set(0)
        self.idcliente_tipo.set(0)
        self.fechaP_tipo.set("")
        self.fechaE_tipo.set("")


aplicacion1 = FormularioTablas()
