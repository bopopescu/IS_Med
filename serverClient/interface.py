import mysql.connector

def comecarMensagem():
    print("\n\n\nCriar pedido\n")

    conn = mysql.connector.connect(
        user='root',
        password='',
        host='127.0.0.1',
        database='pedido')

    data = raw_input("Insira a data: ")
    cc = raw_input("Insira o CC do utente: ")
    tipo = raw_input("Insira o tipo pretendido para o pedido (CA,NW): ")
    descr = raw_input("Insira a descricao: ")

    cursor = conn.cursor()

    try:
        sql = "INSERT INTO pedido.Pedido(data, idDoente, tipo, descricao) VALUES (%(data)s, %(idDoente)s, %(tipo)s, %(descricao)s) "
        cursor.execute(sql, {'data': data, 'idDoente': cc, 'tipo': tipo, 'descricao': descr, })
        conn.commit()

    except:
        conn.rollback()


    cursor.execute("SELECT idPedido FROM worklist LIMIT 1")
    idP = cursor.fetchone()

    cursor.execute("SELECT data FROM Pedido WHERE idPedido =" + str(idP[0]))
    data = cursor.fetchone()


    cursor.execute("SELECT nome FROM Utente WHERE idUtenteCC = " + cc)
    nome = cursor.fetchone()
    #nome = nome[0].encode()


    cursor.execute("SELECT tipo FROM Pedido WHERE idPedido = " + str(idP[0]))
    tipo = cursor.fetchone()


    cursor.execute("SELECT descricao FROM Pedido WHERE idPedido = %s", (idP[0],))
    desc = cursor.fetchone()

    cursor.execute("SELECT sexo FROM Utente WHERE idUtenteCC = " + cc)
    sexo = cursor.fetchone()
    sexo = sexo[0].encode()

    cursor.execute("SELECT morada FROM Utente WHERE idUtenteCC = " + cc)
    morada = cursor.fetchone()
    morada = morada[0].encode('ascii', 'ignore')


    cursor.execute("SELECT telefone FROM Utente WHERE idUtenteCC = " + cc)
    telefone = cursor.fetchone()

    cursor.execute("SELECT dataNasc FROM Utente WHERE idUtenteCC = " + cc)
    dataNasc = cursor.fetchone()

    dataNasc = dataNasc[0].encode()

    cursor.close()
    conn.close()


    msh = "MSH|^~\&|A|A|B|B|" + str(data[0]) + "||ORM^O01|" + str(idP[0]) + "|P|2.5||||AL\n"
    evn = "EVN||" + str(data[0]) + "||AAA|AAA|" + str(data[0]) + "\n"
    pid = "PID|1||" + cc + "||" + nome[0] + "||" + str(dataNasc) + "|" + str(sexo) + "|||" + str(morada) + "||" + str(telefone[0]) + "|||" + str(sexo) + "\n"
    pv1 = "PV1|1|I|CON|||||||||" + str(desc[0]) + "||||||||||||||||||||||||||||||||" + str(data[0]) + "\n"
    orc = "ORC|" + str(tipo[0]) + "|" + str(data[0]) + "\n"
    orb = "OBR|1|" + str(data[0]) + "||" + str(desc[0]) + "|||" + str(data[0]) + "\n"

    aux = msh + evn + pid + pv1 + orc + orb


    return aux
