from datetime import datetime
import mysql.connector

data = datetime.now().strftime('%Y%m%d%H%M%S')


n = 0

''' NAO VAI RECEBER UM FICHEIRO MAS SIM UMA STRING 
path = '/Users/adriana/Documents/uni/EC/is/IS_Med/Output1.txt'

file = open(path, 'r')

i = 0
arr = []

for line in file:
    arr.append(line)
    i += 1

msg = arr[2] + arr[4] + arr[5]

print (msg)

'''

#parse da string
msg_recebida = "MSH|^~\&|AA|AA|BB|BB|201504051157||ORM^O01|A2015040511	5751000002533|P|2.5|||AL|"+\
               "\nPID|||50626||CONCEICAO SERRANO SEQUEIRA^MARIA^^||19411012|F||||||||||28006303|"+\
               "\nPV1||I|INT||||||||||||||||15002727|"+\
               "\nORC|CA|4727374|4727374||||||20150405111053|"+\
               "\nOBR|01|4727374|4727374|M10405^TORAX, UMA INCIDENCIA|||||||||||^^^|||CR|RXE||||||||^^^20150405115723^^0||||||"+"\n"

split_msg = msg_recebida.split('\n',4)

#|AA|AA|BB|BB|
msh_recebido = split_msg[0].split('||',1)[0][8:-12]

#AA
msh_from = msh_recebido.split('|',4)[1]

#BB
msh_to = msh_recebido.split('|',4)[3]

msh = split_msg[0][:9] + msh_to + "|" + msh_to + "|" + msh_from + "|" + msh_from + split_msg[0][20:len(split_msg[0])]



pid =split_msg[1]
if (pid.split('||||||||||',1)[0][-1]=='F'):
    sexo='F'
else:
    sexo='M'

orc =split_msg[3]
obr =split_msg[4]


#recolher input da observacao e inserir na worklist do pc2
while(1):
    print("\n\n\nMensagem lida\n")

    conn = mysql.connector.connect(
        user='root',
        password='root',
        host='127.0.0.1',
        #!
        database='worklist')

    obs = raw_input("Insira as observacoes do exame: ")

    obx = "OBX|1|TX|||" + str(obs[0]) + "|||||" + str(sexo[0]) + "|||" + str(data) + "|||||""\n"
    msg = msh + "\n" + pid + "\n" + orc + "\n" + obr + "\n" + obx + "\n"

    cursor = conn.cursor()

    #alterar para os parâmetros da bd do pc2
    try:
        sql = "INSERT INTO worklist(data, idDoente, tipo, descricao) VALUES (%(data)s, %(idDoente)s, %(tipo)s, %(descricao)s) "
        cursor.execute(sql, {'data': data, 'idDoente': cc, 'tipo': tipo, 'descricao': descr, })
        conn.commit()

    except:
        conn.rollback()


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

    cursor.close()
    conn.close()


    text_file = open("Output_PC2" + str(n) + ".txt", "w")
    text_file.write(msg)
    text_file.close()
    n += 1

exit()