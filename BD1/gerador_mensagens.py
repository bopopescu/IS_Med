from datetime import datetime
import mysql.connector

def gerarMensagens(num):

    bloco = []
    conn = mysql.connector.connect(
        user='root',
        password='',
        host='127.0.0.1',
        database='pedido')

    cursor = conn.cursor()


    for i in range(num):
        msg = "MSH|^~\&|A|A|B|B|201504051157||ORM^O01|"+str(i)+"|P|2.5|||AL|"+\
              "PID|||50626||CONCEICAO SERRANO SEQUEIRA^MARIA^^||19411012|F||||||||||28006303|"+\
              "PV1||I|INT||||||||||||||||15002727|"+\
              "ORC|CA|4727374|4727374||||||20150405111053|"+\
              "OBR|01|4727374|4727374|M10405^TORAX, UMA INCIDENCIA|||||||||||^^^|||CR|RXE||||||||^^^20150405115723^^0||||||"

        bloco.append(msg)

        data = datetime.now().strftime('%Y%m%d%H%M%S')

        try:
            sql = "INSERT INTO pedido.worklist(msg) VALUES (%(msg)s)"
            cursor.execute(sql, {'msg': msg, })
            conn.commit()
        except:
            conn.rollback()

    #print bloco[]

gerarMensagens(10)