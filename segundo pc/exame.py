from datetime import datetime

#i = datetime.now().strftime('%Y%m%d%H%M%S')

path = '/Users/adriana/Documents/uni/EC/is/IS_Med/Output1.txt'

file = open(path, 'r')

i = 0
arr = []

for line in file:
    arr.append(line)
    i += 1

msg = arr[2] + arr[4] + arr[5]

print (msg)


#cursor.execute("SELECT idPedido FROM worklist LIMIT 1")
#idP = cursor.fetchone()

#cursor.execute("SELECT data FROM Pedido WHERE idPedido =" + str(idP[0]))
#data = cursor.fetchone()

#cursor.execute("SELECT idDoente FROM Pedido WHERE idPedido = " + str(idP[0]))
#idD = cursor.fetchone()

#cursor.execute("SELECT nome FROM Utente WHERE idUtenteCC = " + str(idD[0]))
#nome = cursor.fetchone()

#cursor.execute("SELECT estado FROM Pedido WHERE idPedido = " + str(idP[0]))
#estado = cursor.fetchone()

#cursor.execute("SELECT descricao FROM Pedido WHERE idPedido = %s", (idP[0],))
#desc = cursor.fetchone()

#cursor.execute("SELECT sexo FROM Utente WHERE idUtenteCC = " + str(idD[0]))
#sexo = cursor.fetchone()

#cursor.execute("SELECT morada FROM Utente WHERE idUtenteCC = " + str(idD[0]))
#morada = cursor.fetchone()

#cursor.execute("SELECT telefone FROM Utente WHERE idUtenteCC = " + str(idD[0]))
#telefone = cursor.fetchone()

#cursor.execute("SELECT dataNasc FROM Utente WHERE idUtenteCC = " + str(idD[0]))
#dataNasc = cursor.fetchone()

msh = "MSH|^~\&|B|B|A|A|" + str(data[0]) + "||ORU^R01|" + str(idP[0]) + "|P|2.5\r"


msg = msh + arr[2] + arr[4] + arr[5]
#text_file = open("Output.txt", "w")
#text_file.write(aux)
#text_file.close()


