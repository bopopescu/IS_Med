from hl7apy.core import Message
import MySQLdb as db

connection = db.connect (host = "localhost",
                              user = "root",
                              passwd = "root",
                              db = "pedido")

cursor = connection.cursor()

cursor.execute("SELECT idPedido FROM worklist LIMIT 1")
idP = cursor.fetchone()

cursor.execute("SELECT data FROM Pedido WHERE idPedido =" + str(idP[0]))
data = cursor.fetchone()

cursor.execute("SELECT idDoente FROM Pedido WHERE idPedido = " + str(idP[0]))
idD = cursor.fetchone()

cursor.execute("SELECT nome FROM Utente WHERE idUtenteCC =" + str(idD[0]))
nome = cursor.fetchone()

cursor.execute("SELECT estado FROM Pedido WHERE idPedido = " + str(idP[0]))
estado = cursor.fetchone()

cursor.execute("SELECT sexo FROM Utente WHERE idUtenteCC = " + str(idD[0]))
sexo = cursor.fetchone()

cursor.execute("SELECT morada FROM Utente WHERE idUtenteCC = " + str(idD[0]))
morada = cursor.fetchone()

cursor.execute("SELECT telefone FROM Utente WHERE idUtenteCC = " + str(idD[0]))
telefone = cursor.fetchone()

cursor.execute("SELECT desc FROM Pedido WHERE idPedido = " + str(idP[0]))
desc = cursor.fetchone()

cursor.execute("SELECT dataNasc FROM Utente WHERE idUtenteCC = " + str(idD[0]))
dataNasc = cursor.fetchone()

msh = "MSH|^~\&|A|A|B|B|" + data + "||ORM^O01|" + idP + "|P|2.5||||AL\r"
evn = "EVN||" + data + "||AAA|AAA|" + data + "\r"
pid = "PID|1||" + idD + "||" + nome + "||" + dataNasc + "|" + sexo + "|||" + morada + "||" + telefone + "|||" + sexo + "\r"
pv1 = "PV1|1|I|CON|||||||||" + desc + "||||||||||||||||||||||||||||||||" + data + "\r"
orc = "ORC|" + estado + "|" + data + "\r"
orb = "OBR|1|" + data + "||" + desc + "|||" + data + "\r"



aux = msh + evn + pid + pv1 + orc + orb
text_file = open("Output.txt", "w")
text_file.write(aux)
text_file.close()