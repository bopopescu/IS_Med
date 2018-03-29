import socket
import sys
import sendRecAPI
import time
import select


def client():
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Connect the socket to the port where the server is listening
    server_address = ('localhost', 10000)
    print 'connecting to %s port %s' % server_address
    sock.connect(server_address)
    while True:
        data = sendRecAPI.recv_msg(sock)
        if data:
            acks = extractAcks(data)
            sendRecAPI.send_msg(sock,acks)
        else:
            break
    sock.close()

def extractAcks(data):
    requests = data.split('!')
    acks = ""
    for i in range(len(requests)-2):
        ack = requests[i].split('||')[1].split('|')[1]
        acks += ack +"|"
    acks += requests[len(requests)-2].split('||')[1].split('|')[1]
    return acks





client()