import mysql.connector

print("Criar pedido\n")

conn = mysql.connector.connect(
    user='root',
    password='root',
    host='127.0.0.1',
    database='pedido')

data = raw_input("Insira a data: ")
estado = raw_input("Insira o estado pretendido para o pedido (CA,NW): ")
cc = raw_input("Insira o CC do utente: ")
descr = raw_input("Insira a descricao: ")

mycursor = conn.cursor()

try:
    sql = "INSERT INTO pedido.Pedido(data, idDoente, estado, descricao) VALUES (%(data)s, %(idDoente)s, %(estado)s, %(descricao)s) "
    mycursor.execute(sql, {'data': data, 'idDoente': cc, 'estado': str(estado), 'descricao': str(descr), })
    conn.commit()

except:
    conn.rollback()

mycursor.close()
conn.close()

exit()
