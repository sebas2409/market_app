from matplotlib import pyplot as pp

from db.db_logic import Db_Logic as db


class Db_controller:
    database = db()

    def add_categoria(self, data):
        self.database.add_categoria(data)

    def add_cliente(self, data):
        self.database.add_cliente(data)

    def add_pedido(self, data):
        self.database.add_pedido(data)

    def add_producto(self, data):
        self.database.add_producto(data)

    def update_cliente(self, data):
        self.database.update_cliente(data)

    def update_categoria(self, data):
        self.database.update_categoria(data)

    def update_pedido(self, data):
        self.database.update_pedido(data)

    def update_producto(self, data):
        self.database.update_producto(data)

    def select_pedido_byIdCli(self, data_idcliente):
        self.database.select_pedido_byIdCli(data_idcliente)

    def select_pedido_ordenado(self):
        self.database.select_pedido_ordenado()

    def searchProductByCategory(self, categoria):
        self.database.search_products_by_category(categoria)

    def delete_categoria(self, categoria):
        self.database.delete_categoria_by_id(categoria)

    def delete_product_byId(self, datos):
        self.database.delete_product_byId(datos)

    def delete_client(self, value):
        self.database.delete_cliente_by_id(value)

    def delete_pedido_byId(self, data_delete):
        self.database.delete_pedido_byId(data_delete)

    def order_by_id(self):
        self.database.order_cliente_by_id()

    def order_categoria_byId(self):
        self.database.order_categoria_byId()

    def order_product_by_id(self):
        self.database.order_product_by_id()

    def obtener_grafica_cliente(self, tipo):
        clientes = []
        pedidos = []
        rs = self.database.get_client_id()
        for c in rs:
            clientes.append(c[0])
            p = self.database.get_count_of_pedidos_by_client(c)
            pedidos.append(p)

        if tipo == "Plot":
            pp.plot(clientes, pedidos, color="red")
        elif tipo == "Scatter":
            pp.scatter(clientes, pedidos, color="green")
        elif tipo == "Fill-between":
            pp.fill_between(clientes, pedidos, color="blue")

        pp.xlabel("ID Clientes")
        pp.ylabel("Total de Pedidos")
        pp.savefig("../graph/client-graph.png")

    def create_new_table(self, datos):
        self.database.create_new_table(datos)

    def drop_table(self, tabla):
        self.database.drop_table(tabla)

    def grafica_clientes_cargo(self, tipo):
        clientes = []
        cargos = []
        rs = self.database.get_client_cargos()
        rs2 = self.database.count_clientes_byCargo()
        for c in rs:
            if c[0] not in cargos:
                cargos.append(c[0])
        cargos.sort()
        for x in rs2:
            clientes.append(x[1])

        if tipo == "Plot":
            pp.plot(cargos, clientes, color="red")
        elif tipo == "Scatter":
            pp.scatter(cargos, clientes, color="green")
        elif tipo == "Fill-between":
            pp.fill_between(cargos, clientes, color="blue")

        pp.xlabel("Cargo")
        pp.ylabel("ID Cliente")
        pp.savefig("../graph/client-graph2.png")
