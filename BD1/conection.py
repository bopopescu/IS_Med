import mysql.connector


config = {
    'user': 'root',
    'password': '',
    'host': '127.0.0.1',
    'database': 'pedido',
    'raise_on_warnings': True,
    }

pedido_ref = {
    'idPedido': '',
    'data': '',
    'idDoente': '',
    'nomeDoente':'',
    'nprocesso':'',
    'morada': '',
    'telefone': '',
    'estado': '',
    'descricao': '',
}

cnx = mysql.connector.connect(**config)


print("Siga meu")










cnx.close()