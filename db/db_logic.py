import sqlite3


class Db_Logic:

    def add_categoria(self, datos):
        con = self.abrir()
        cursor = con.cursor()
        sql = "insert into categoria values (?,?)"
        cursor.execute(sql, datos)
        con.commit()
        con.close()

    def add_producto(self, datos):
        con = self.abrir()
        cursor = con.cursor()
        sql = "insert into producto values (?,?,?,?,?,?)"
        cursor.execute(sql, datos)
        con.commit()
        con.close()

    def add_cliente(self, datos):
        con = self.abrir()
        cursor = con.cursor()
        sql = "insert into cliente values (?,?,?,?,?,?,?,?,?,?,?)"
        cursor.execute(sql, datos)
        con.commit()
        con.close()

    def add_pedido(self, datos):
        con = self.abrir()
        cursor = con.cursor()
        sql = "insert into pedido values (?,?,?,?)"
        cursor.execute(sql, datos)
        con.commit()
        con.close()

    def update_pedido(self, datos):
        con = self.abrir()
        cursor = con.cursor()
        sql = "update pedido set fechapedido = ?, fechaentrega = ? where idpedido = ?"
        cursor.execute(sql, datos)
        con.commit()
        con.close()

    def update_categoria(self, datos):
        con = self.abrir()
        cursor = con.cursor()
        sql = "UPDATE categoria set categoria = ? where idcategoria = ?"
        cursor.execute(sql, datos)
        con.commit()
        con.close()

    def update_producto(self, datos):
        con = self.abrir()
        cursor = con.cursor()
        sql = "UPDATE producto set nombre = ?, medida = ?, precio = ?, stock = ? where idproducto = ?"
        cursor.execute(sql, datos)
        con.commit()
        con.close()

    def update_cliente(self, datos):
        con = self.abrir()
        cursor = con.cursor()
        sql = '''UPDATE cliente set cia = ?, contacto = ?, 
            cargo = ?, direccion = ?, ciudad = ?, region=?, cp=?, 
            pais=?, tlf=?, fax=? where idcliente = ?'''

        cursor.execute(sql, datos)
        con.commit()
        con.close()

    def select_pedido_byIdCli(self, data_idcliente):

        con = self.abrir()
        cursor = con.cursor()
        sql = "SELECT * FROM pedido where idcliente = ?"
        res = cursor.execute(sql, data_idcliente)
        for row in res.fetchall():
            print(row)

        con.close()

    def search_products_by_category(self, datos):
        con = self.abrir()
        cursor = con.cursor()
        sql = "SELECT * FROM producto WHERE idcategoria = ?"
        res = cursor.execute(sql, datos)
        x = res.fetchall()

        for row in x:
            print(row)

        con.close()

    def delete_cliente_by_id(self, value):
        print(value)
        con = self.abrir()
        cursor = con.cursor()
        sql = "delete from cliente where idcliente = ?"
        cursor.execute(sql, value)
        con.commit()
        con.close()

    def delete_product_byId(self, datos):
        con = self.abrir()
        cursor = con.cursor()
        sql = "delete from producto where idproducto = ?"
        cursor.execute(sql, datos)
        con.commit()
        con.close()

    def delete_pedido_byId(self, data_delete):
        con = self.abrir()
        cursor = con.cursor()
        sql = "delete from pedido where idpedido = ?"
        cursor.execute(sql, data_delete)
        con.commit()
        con.close()

    def delete_categoria_by_id(self, categoria):
        print(categoria)
        con = self.abrir()
        cursor = con.cursor()
        sql = "delete FROM categoria WHERE idcategoria = ?"
        cursor.execute(sql, categoria)
        con.commit()
        con.close()

    def order_cliente_by_id(self):
        con = self.abrir()
        cursor = con.cursor()
        sql = "select * from cliente order by idcliente"
        res = cursor.execute(sql)
        x = res.fetchall()
        for row in x:
            print(row)
        con.close()

    def order_categoria_byId(self):
        con = self.abrir()
        cursor = con.cursor()
        sql = "select * from categoria order by idcategoria"
        res = cursor.execute(sql)
        for row in res.fetchall():
            print(row)
        con.close()

    def order_product_by_id(self):
        con = self.abrir()
        cursor = con.cursor()
        sql = "select * from producto order by idproducto"
        res = cursor.execute(sql)
        for row in res.fetchall():
            print(row)
        con.close()

    def abrir(self):
        # conexion = sqlite3.connect("../supermercado.db")
        conexion = sqlite3.connect("C:/Users/grand/PycharmProjects/market_app_sge/supermercado.db")
        return conexion

    def select_pedido_ordenado(self):
        con = self.abrir()
        cursor = con.cursor()
        sql = "select * from pedido order by idpedido"
        res = cursor.execute(sql)
        x = res.fetchall()
        for row in x:
            print(row)
        con.close()

    def get_client_id(self):
        con = self.abrir()
        cursor = con.cursor()
        sql = "select idcliente from cliente "
        rs = cursor.execute(sql)
        return rs.fetchall()

    def get_count_of_pedidos_by_client(self, value):
        con = self.abrir()
        cursor = con.cursor()
        sql = "select * from pedido where idcliente = ?"
        rs = cursor.execute(sql, value)
        x = rs.fetchall()
        return len(x)

    def create_new_table(self, datos):
        con = self.abrir()
        cursor = con.cursor()
        sql = "CREATE TABLE IF NOT EXISTS {} ({} varchar(20),{} varchar(20))".format(datos[0], datos[1], datos[2])
        cursor.execute(sql)
        con.close()

    def drop_table(self, datos):
        con = self.abrir()
        cursor = con.cursor()
        sql = "drop table {}".format(datos[0])
        cursor.execute(sql)
        con.close()

    def get_client_cargos(self):
        con = self.abrir()
        cursor = con.cursor()
        sql = "select cargo from cliente "
        rs = cursor.execute(sql)
        return rs.fetchall()
