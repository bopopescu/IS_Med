import mysql.connector

print("Criar pedido")

conn = mysql.connector.connect(
    user ='root',
    password='root',
    host='127.0.0.1',
    database='pedido')

mycursor = conn.cursor()

data = raw_input("Insira a data: ")
estado = raw_input("Insira o estado pretendido para o pedido (CA,NW): ")
cc = raw_input("Insira o CC do utente: ")
descr = raw_input("Insira a descricao: ")


mycursor.execute("SELECT MAX(idPedido) from pedido.Pedido")
id_pedido = mycursor.fetchone()
print(id_pedido[0])
id_pedido = id_pedido[0] + 1


try:
    sql = "INSERT INTO pedido.Pedido VALUES (%d, %d, %d, %s, %s)"
    data = (int(id_pedido), int(data), int(cc), str(estado), str(descr))
    mycursor.execute(sql,data)
    conn.commit()
except:
    conn.rollback()

conn.close()

exit()

