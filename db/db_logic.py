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

    # def delete_cliente_by_id(self, id):
    #     con = self.abrir()
    #     cursor = con.cursor()
    #     sql = "delete from cliente where idcliente = (?)"
    #     cursor.execute(sql, id)
    #     con.commit()
    #     con.close()

    def add_pedido(self, datos):
        con = self.abrir()
        cursor = con.cursor()
        sql = "insert into pedido values (?,?,?,?)"
        cursor.execute(sql, datos)
        con.commit()
        con.close()

    def add_detalle(self, datos):
        con = self.abrir()
        cursor = con.cursor()
        sql = "insert into detalle values (?,?,?,?,?)"
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

    def abrir(self):
        # conexion = sqlite3.connect("../supermercado.db")
        conexion = sqlite3.connect("C:/Users/grand/PycharmProjects/hg_sge_gestion_supermercado/supermercado.db")
        return conexion
