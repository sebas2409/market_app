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
