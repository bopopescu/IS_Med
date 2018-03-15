import socket
import threading
from interface import comecarMensagem
import time
import sys

reload(sys)
sys.setdefaultencoding('utf8')


global queueReceived
queueReceived = []


global queueToSend
queueToSend = []

def letsSendSomeMessages():
    time.sleep(10)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 10000)
    #print('connecting to %s port %s' % server_address)
    sock.connect(server_address)

    while True:
        if queueToSend:
            sendData(sock,queueToSend[0])
            receiveData(sock)
            del queueToSend[0]



def letsReceiveSomeMessages():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 10001)
    #print('starting up on %s port %s' % server_address)
    sock.bind(server_address)
    sock.listen(1)
    #print('waiting for a connection')
    connection, client_address = sock.accept()
    #print('connection from', client_address)
    while True:
        data = receiveData(connection)
        queueReceived.append(data)
        sendData(connection, "Confirmed Reception")



def sendData(sock,message):
    #print('sending "%s"' % message)
    sock.sendall(message.encode("utf-8"))


def receiveData(sock):
    data = sock.recv(10000).decode("utf-8")
    #print('received "%s"' % data)
    return data


def background():
    while True:
        queueToSend.append(comecarMensagem())
        print ("\n> Mensagem Enviada")

a_thread = threading.Thread(target=letsSendSomeMessages)
a_thread.start()
b_thread = threading.Thread(target=letsReceiveSomeMessages)
b_thread.start()
background()

