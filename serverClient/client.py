import socket
import sys

# Create a TCP/IP socket
from pip._vendor.distlib.compat import raw_input

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 10000)
print('connecting to %s port %s' % server_address)
sock.connect(server_address)

try:

    # Send data
    message = raw_input("Message: ")
    print('sending "%s"' % message)
    sock.sendall(message.encode("utf-8"))

    # Look for the response
    amount_received = 0
    amount_expected = len(message)

    while amount_received < amount_expected:
        data = sock.recv(16)
        amount_received += len(data)
        print('received "%s"' % data)

finally:
    print('closing socket')
    sock.close()

