from datetime import datetime
import mysql.connector


def criarMensagem (msg):

    msg_recebida = msg

    split_msg = msg_recebida.split('\n',4)
    #|AA|AA|BB|BB|
    #msh_recebido = split_msg[0].split('||',1)[0][8:-12]
    #AA
    #msh_from = msh_recebido.split('|',4)[1]
    #BB
    #msh_to = msh_recebido.split('|',4)[3]

    msh = "MSH|^~\&|B|B|A|A|" + split_msg[0][20:len(split_msg[0])]


    pid =split_msg[2]
    if (pid.split('||||||||||',1)[0][-1]=='F'):
        sexo='F'
    else:
        sexo='M'

    orc =split_msg[3]
    obr =split_msg[4]

    id_pedido = pid.split('|', 4)[3]

    #recolher input da observacao e inserir na worklist do pc2
    print("\n\n\nMensagem lida\n")

    conn = mysql.connector.connect(
        user='root',
        password='',
        host='127.0.0.1',
        database='mydb')

    obs = raw_input("Insira as observacoes do exame: ")

    data = datetime.now().strftime('%Y%m%d%H%M%S')
    obx = "OBX|1|TX|||" + str(obs) + "|||||" + str(sexo[0]) + "|||" + str(data) + "|||||""\n"
    msg = msh + "\n" + pid + "\n" + orc + "\n" + obr + "\n" + obx + "\n"

    cursor = conn.cursor()
    #alterar para os parâmetros da bd do pc2
    try:
        sql = "INSERT INTO mydb.worklist(id_pedido, msg, estado) VALUES (%(id_pedido)s, %(msg)s, %(estado)s) "
        cursor.execute(sql, {'id_pedido': id_pedido, 'msg': msg, 'estado': 0 })
        conn.commit()

    except:
        conn.rollback()

    cursor.close()
    conn.close()
    return msg