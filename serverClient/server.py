import socket
import sys


def createServer():
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to the port
    server_address = ('172.20.10.3', 10000)
    print('starting up on %s port %s' % server_address)
    sock.bind(server_address)
    # Listen for incoming connections
    sock.listen(1)

    while True:
        # Wait for a connection
        print('waiting for a connection')
        connection, client_address = sock.accept()
        try:
            print('connection from', client_address)
            # Receive the data in small chunks and retransmit it
            data = receiveData(connection)
            print(data)
        finally:
            # Clean up the connection
            connection.close()


def sendData(sock,message):
    print('sending "%s"' % message)
    sock.sendall(message.encode("utf-8"))


def receiveData(sock):
    data = ""
    while True:
        data += sock.recv(512)
        print('received "%s"' % data)
        if not(data):
            print("Finished!")
            return data


createServer()
