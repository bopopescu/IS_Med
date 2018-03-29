import socket
import sys
import time
import sendRecAPI
import select
import mysql.connector
import threading
import fileinput



def server():
    global nReq
    global nBlock
    global startTime
    global frequencyUpdate
    global keepGoin
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_address = ('localhost', 10000)
    print 'starting up on %s port %s' % server_address
    sock.bind(server_address)
    sock.listen(1)
    print 'waiting for a connection'
    connection, client_address = sock.accept()
    print 'connection from', client_address
    sure = 'n'
    while (sure!="y" and sure!="Y"):
        nReq = int(raw_input("\nWith how many request per message would you like to test? "))
        timeout = float(raw_input("\nWhat's the timeout(secs) between messages that you wold like to test? "))
        frequencyUpdate = float(raw_input("\nWith what frequency(secs) would you like to receive updates on measures? "))
        print ("\n"+str(nReq)+" requests per message and a timeout of "+str(timeout)+" seconds. Updates on measures each "+str(frequencyUpdate)+" seconds.")
        sure = raw_input("Is that right?(y/n) ")

    #get the last nMens from worklist
    reqList = getRequests(nReq)
    #generate block and list of acks
    (block,acksDict) = gerarBloco(reqList)
    #

    print "Starting to Send"
    acksRecList = []
    connection.setblocking(0)
    
    startTime = time.time()
    
    keepGoin = 1
    while keepGoin:
        #send block
        sendRecAPI.send_msg(connection,block)
        ready = select.select([connection], [], [], timeout)
        if (ready[0]):
            acksRec = sendRecAPI.recv_msg(connection)
            acksRec = acksRec.split('|')
            for ack in acksRec:
                del acksDict[ack]
            #check ack's
            if acksDict:
                #resend messages if needed
                listReqFail = []
                for r in acksDict:
                    listReqFail.append(acksDict[r])
                (block,acksDict) = gerarBloco(reqList)
            else:
                #if not restructure block and ackDict
                (block,acksDict) = gerarBloco(reqList) 
                nBlock += 1
            acksRecList = []
        else:
            print "timeout"
            (block,acksDict) = gerarBloco(reqList)
    connection.shutdown(socket.SHUT_RDWR)
    connection.close()
    sock.close()

def getRequests(x):
    print "Connecting to DB"
    conn = mysql.connector.connect(
        user='root',
        password='root',
        host='127.0.0.1',
        database='pedido')
    cursor = conn.cursor()
    print "Connected! Executing querys."
    cursor.execute("SELECT msg FROM pedido.worklist "+
                   "ORDER BY id DESC "+
                   "LIMIT "+str(x))
    resultSet = cursor.fetchall()
    ret = []
    for row in resultSet:
        ret.append(row[0].encode("utf-8"))
    return ret


def gerarBloco(bloco):
    bloco_ack = {}
    bloco = [x + "!" for x in bloco]
    blocoRet = ""
    for m in bloco:
        ack = m.split('||')[1].split('|')[1]
        bloco_ack[ack] = m
        blocoRet = blocoRet+m
    return (blocoRet, bloco_ack)


def background():
    global nReq
    global nBlock
    global startTime
    global frequencyUpdate
    global keepGoin
    while keepGoin:
        time.sleep(frequencyUpdate)
        minutes = (time.time()-startTime)/60
        blocks = (float(nBlock))/minutes
        req = nBlock*nReq
        print "\n\n"
        print str(nBlock) + " blocks sent. A total of " + str(req) + "requests."
        print str(minutes) + " minutes have passed."
        print "MEAN:\n"+str(blocks)+" blocks per minute." + str(float(req)/minutes) + " requests per minute."








global keepGoin
keepGoin = 0
nBlock = 0
a_thread = threading.Thread(target=server)
a_thread.start()
while not keepGoin:
    pass
b_thread = threading.Thread(target=background)
b_thread.start()
stop = raw_input("TO STOP THE SERVER JUST INPUT SOMETHING\n")
keepGoin=0
a_thread.join()
b_thread.join()
