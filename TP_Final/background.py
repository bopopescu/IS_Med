import requests
import sys
import time
import mysql.connector

conn = mysql.connector.connect(
        user='root',
        password='root',
        host='127.0.0.1',
        database='ISfinal')
cursor = conn.cursor()


def getOrcidsDB():
    cursor.execute("Select orcid From Orcid;")
    resultSet = cursor.fetchall()
    orcidListDB = []
    for row in resultSet:
        orcidListDB.append(row[0].encode("utf-8"))
    return orcidListDB

def verify(array):
    del array[0]
    for orcid in array:
        if (len(orcid)!=19):
            print "Orcid with invalid format!"
            return False
        for i in range(len(orcid)):
            if (i==4 or i==9 or i==14):
                if (orcid[i]!="-"):
                    print "Orcid with invalid format!"
                    return False
            elif (not orcid[i].isdigit()):
                print "Orcid with invalid format!"
                return False
    return True

def listORCID():
    for orcid in orcidList:
        print orcid

def addORCID(listaORCID):
    for orcid in listaORCID:
        if (not orcidList.__contains__(orcid)):
            cursor.execute("Insert into ISfinal.Orcid(orcid) values (\""+orcid+"\");")
            conn.commit()
            print orcid+" inserted."
        else:
            print orcid+" already exists."

def remORCID(listaORCID):
    for orcid in listaORCID:
        if (orcidList.__contains__(orcid)):
            print "Delete from Orcid where orcid=\""+orcid+"\";"
            cursor.execute("Delete from ISfinal.Orcid where orcid=\""+orcid+"\";")
            conn.commit()
            print orcid+ " removed."
        else:
            print orcid+ " doesnt exist."

def instructions():
    print "HELP:"
    print "\tSart background syncing process:"
    print "\t\tpython background"
    print "\tList ORCID being analyzed:"
    print "\t\tpython background -l"
    print "\tAdd ORCID('s) to be analyzed:"
    print "\t\tpython background -a XXXX-XXXX-XXXX-XXXX"
    print "\t\tpython background -a XXXX-XXXX-XXXX-XXXX YYYY-YYYY-YYYY-YYYY ZZZZ-ZZZZ-ZZZZ-ZZZZ"
    print "\tRemove ORCID('s) from being analyzed:"
    print "\t\tpython background -r XXXX-XXXX-XXXX-XXXX"
    print "\t\tpython background -r XXXX-XXXX-XXXX-XXXX YYYY-YYYY-YYYY-YYYY ZZZZ-ZZZZ-ZZZZ-ZZZZ"


def background():
    global orcidList
    while(True):
        for orcid in orcidList:
            headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
            r = requests.get('https://pub.orcid.org/v2.1/'+orcid+'/works',headers=headers)
            reqJson = r.json()
            for art in reqJson["group"]:
                artTitle = art["work-summary"][0]["title"]["title"]["value"]
                print orcid + " | " + artTitle
        orcidList = getOrcidsDB()
        time.sleep(5)





orcidList = getOrcidsDB()

array = sys.argv
del array[0]

if (len(array)==0):
    background()
elif (array[0]=="-l"):
    listORCID()
elif (array[0]=="-a" and verify(array)):
    addORCID(array)
elif (array[0]=="-r" and verify(array)):
    remORCID(array)
else:
    instructions()