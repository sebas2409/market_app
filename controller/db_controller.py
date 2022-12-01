from db.db_logic import Db_Logic as db  # from modulo.archivo import class


class Db_controller:
    database = db()

    def add_categoria(self, data):
        self.database.add_categoria(data)

    def add_cliente(self, data):
        self.database.add_cliente(data)

    # def delete_client(self, id):
    #     self.database.delete_cliente_by_id(id)

    def add_pedido(self, data):
        self.database.add_pedido(data)

    # def add_detalle(self, data):
    #     self.database.add_detalle(data)

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
