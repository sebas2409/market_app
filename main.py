import tkinter as tk

ventana = tk.Tk()
ventana.title("Gestión de Supermercado")
ventana.config(width=400, height=300)
barra_menus = tk.Menu()
menu_supermercado = tk.Menu(barra_menus, tearoff=False)
menu_supermercado.add_command(label="Tabla Cliente")
menu_supermercado.add_command(label="Tabla Producto")
menu_supermercado.add_command(label="Tabla Detalle")

menu_supermercado.add_separator()
menu_supermercado.add_command(label="Salir", command=ventana.destroy)
menu_add = tk.Menu(barra_menus, tearoff=False)
menu_delete = tk.Menu(barra_menus, tearoff=False)
barra_menus.add_cascade(menu=menu_supermercado, label="Supermercado")
barra_menus.add_cascade(menu=menu_add, label="Añadir Tabla")
barra_menus.add_cascade(menu=menu_delete, label="Eliminar Tabla")
ventana.config(menu=barra_menus)
ventana.mainloop()

