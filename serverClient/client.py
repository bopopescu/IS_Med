import socket
import sys
from pip._vendor.distlib.compat import raw_input



def client():
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Connect the socket to the port where the server is listening
    server_address = ('172.20.10.3', 10000)
    print('connecting to %s port %s' % server_address)
    sock.connect(server_address)

    while True:
        try:
            message = raw_input("Message: ")
            # Send data
            sendData(sock,message)
            # Look for the response
            receiveData(sock)

        finally:
            print('closing socket')
            sock.close()

def sendData(sock,message):
    print('sending "%s"' % message)
    sock.sendall(message.encode("utf-8"))


def receiveData(sock):
    while True:
        data = sock.recv(512)
        print('received "%s"' % data)
        if not(data):
            print("Finished!")
            break


client()