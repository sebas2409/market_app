import tkinter as tk
from tkinter import ttk


# Clase
class FormularioTablas:
    def __init__(self):
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

        self.boton1 = ttk.Button(self.labelframe1, text="Añadir Registro a Categoría", command=self.add_categoria())
        self.boton1.grid(column=1, row=2, padx=4, pady=4)

    # Formulario tabla cliente
    def form_cliente(self):
        self.pagina1 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina1, text="Añadir a cliente")
        self.labelframe1 = ttk.LabelFrame(self.pagina1, text="Cliente")
        self.labelframe1.grid(column=0, row=0, padx=5, pady=10)

        self.label1 = ttk.Label(self.labelframe1, text="IdCliente:")
        self.label1.grid(column=0, row=0, padx=4, pady=4)
        self.idpedido_tipo = tk.IntVar()
        self.entry_idpedido = ttk.Entry(self.labelframe1, textvariable=self.idpedido_tipo)
        self.entry_idpedido.grid(column=1, row=0, padx=4, pady=4)

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

        self.boton1 = ttk.Button(self.labelframe1, text="Añadir Registro a Cliente", command=self.add_cliente())
        self.boton1.grid(column=1, row=12, padx=4, pady=4)
        self.boton2 = ttk.Button(self.labelframe1, text="Borrar Cliente por ID")

    # Formulario tabla pedido
    def form_pedido(self):
        self.pagina1 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina1, text="Añadir un pedido")
        self.labelframe1 = ttk.LabelFrame(self.pagina1, text="Pedido")
        self.labelframe1.grid(column=0, row=0, padx=5, pady=10)

        self.label1 = ttk.Label(self.labelframe1, text="Id pedido:")
        self.label1.grid(column=0, row=0, padx=4, pady=4)
        self.idpedido_tipo = tk.IntVar()
        self.entry_idpedido = ttk.Entry(self.labelframe1, textvariable=self.idpedido_tipo)
        self.entry_idpedido.grid(column=1, row=0, padx=4, pady=4)

        self.label2 = ttk.Label(self.labelframe1, text="Fecha pedido:")
        self.label2.grid(column=0, row=1, padx=4, pady=4)
        self.fechaP_tipo = tk.StringVar()
        self.entry_fechaP = ttk.Entry(self.labelframe1, textvariable=self.fechaP_tipo)
        self.entry_fechaP.grid(column=1, row=1, padx=4, pady=4)

        self.label2 = ttk.Label(self.labelframe1, text="Fecha entrega:")
        self.label2.grid(column=0, row=2, padx=4, pady=4)
        self.fechaE_tipo = tk.StringVar()
        self.entry_fechaE = ttk.Entry(self.labelframe1, textvariable=self.fechaE_tipo)
        self.entry_fechaE.grid(column=1, row=2, padx=4, pady=4)

        self.boton1 = ttk.Button(self.labelframe1, text="Añadir Registro a Pedido", command=self.add_pedido())
        self.boton1.grid(column=1, row=12, padx=4, pady=4)
        self.boton2 = ttk.Button(self.labelframe1, text="Borrar Pedido por ID")

    # Formulario tabla detalle
    def form_detalle(self):
        self.pagina1 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina1, text="Añadir detalles")
        self.labelframe1 = ttk.LabelFrame(self.pagina1, text="Detalle")
        self.labelframe1.grid(column=0, row=0, padx=5, pady=10)

        self.label1 = ttk.Label(self.labelframe1, text="Id pedido:")
        self.label1.grid(column=0, row=0, padx=4, pady=4)
        self.idpedido_tipo = tk.IntVar()
        self.entry_idpedido = ttk.Entry(self.labelframe1, textvariable=self.idpedido_tipo)
        self.entry_idpedido.grid(column=1, row=0, padx=4, pady=4)

        self.label1 = ttk.Label(self.labelframe1, text="Id cliente:")
        self.label1.grid(column=0, row=1, padx=4, pady=4)
        self.idcliente_tipo = tk.IntVar()
        self.entry_idcliente = ttk.Entry(self.labelframe1, textvariable=self.idcliente_tipo)
        self.entry_idcliente.grid(column=1, row=1, padx=4, pady=4)

        self.label1 = ttk.Label(self.labelframe1, text="Id pedido:")
        self.label1.grid(column=0, row=2, padx=4, pady=4)
        self.idpedido_tipo = tk.IntVar()
        self.entry_idpedido = ttk.Entry(self.labelframe1, textvariable=self.idpedido_tipo)
        self.entry_idpedido.grid(column=1, row=2, padx=4, pady=4)

        self.label2 = ttk.Label(self.labelframe1, text="Precio")
        self.label2.grid(column=0, row=3, padx=4, pady=4)
        self.precio_tipo = tk.StringVar()
        self.entry_precio = ttk.Entry(self.labelframe1, textvariable=self.precio_tipo)
        self.entry_precio.grid(column=1, row=3, padx=4, pady=4)

        self.label2 = ttk.Label(self.labelframe1, text="Unidades")
        self.label2.grid(column=0, row=4, padx=4, pady=4)
        self.unidades_tipo = tk.StringVar()
        self.entry_unidades = ttk.Entry(self.labelframe1, textvariable=self.unidades_tipo)
        self.entry_unidades.grid(column=1, row=4, padx=4, pady=4)

        self.label2 = ttk.Label(self.labelframe1, text="Descuento")
        self.label2.grid(column=0, row=5, padx=4, pady=4)
        self.descuento_tipo = tk.StringVar()
        self.entry_descuento= ttk.Entry(self.labelframe1, textvariable=self.descuento_tipo)
        self.entry_descuento.grid(column=1, row=5, padx=4, pady=4)

        self.botonRegistro = ttk.Button(self.labelframe1, text="Añadir Registro a Detalle", command=self.add_detalle())
        self.botonRegistro.grid(column=1, row=12, padx=4, pady=4)
        self.botonBorrarDetalle = ttk.Button(self.labelframe1, text="Borrar Detalle por ID")
        self.botonBorrarDetalle.grid(column=1, row=13, padx=4, pady=4)

    # Formulario tabla productos
    def tabla_productos(self):
        self.paginaProductos = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.paginaProductos, text="Añadir a productos")
        self.labelFrame1 = ttk.LabelFrame(self.paginaProductos, text="Producto")
        self.labelFrame1.grid(column=0, row=0, padx=5, pady=10)

        self.label1 = ttk.Label(self.labelFrame1, text="Nombre: ")
        self.label1.grid(column=0, row=0, padx=4, pady=4)
        self.nombre = tk.StringVar()
        self.nombreInput = ttk.Entry(self.labelFrame1, textvariable=self.nombre)
        self.nombreInput.grid(column=1, row=0, padx=4, pady=4)

        self.label1 = ttk.Label(self.labelFrame1, text="Id Categoria: ")
        self.label1.grid(column=0, row=1, padx=4, pady=4)
        self.id_categoria = tk.IntVar()
        self.nombreInput = ttk.Entry(self.labelFrame1, textvariable=self.id_categoria)
        self.nombreInput.grid(column=1, row=1, padx=4, pady=4)

        self.label1 = ttk.Label(self.labelFrame1, text="Medida: ")
        self.label1.grid(column=0, row=2, padx=4, pady=4)
        self.medida = tk.StringVar()
        self.nombreInput = ttk.Entry(self.labelFrame1, textvariable=self.medida)
        self.nombreInput.grid(column=1, row=2, padx=4, pady=4)

        self.label1 = ttk.Label(self.labelFrame1, text="Precio: ")
        self.label1.grid(column=0, row=3, padx=4, pady=4)
        self.precio = tk.IntVar()
        self.nombreInput = ttk.Entry(self.labelFrame1, textvariable=self.precio)
        self.nombreInput.grid(column=1, row=3, padx=4, pady=4)

        self.label1 = ttk.Label(self.labelFrame1, text="Stock: ")
        self.label1.grid(column=0, row=4, padx=4, pady=4)
        self.stock = tk.IntVar()
        self.nombreInput = ttk.Entry(self.labelFrame1, textvariable=self.stock)
        self.nombreInput.grid(column=1, row=4, padx=4, pady=4)

        self.boton1 = ttk.Button(self.labelFrame1, text="Obtener gráfica")  # todo:  falta agregar command a ejecutar!
        self.boton1.grid(column=0, row=5, padx=4, pady=4)

        self.boton2 = ttk.Button(self.labelFrame1, text="Obtener Excel")  # todo:  falta agregar command a ejecutar!
        self.boton2.grid(column=1, row=5, padx=4, pady=4)

        # todo: Falta hacer tabs de crear tabla y eliminar tabla!

    # TODO MÉTODOS AÑADIR REGISTROS:

    def add_categoria(self):
        pass

    def add_cliente(self):
        pass

    def add_pedido(self):
        pass

    def add_detalle(self):
        pass


aplicacion1 = FormularioTablas()
