import requests
import sys

def verify(array):
    print array
    return True

def listORCID():
    print "-l"

def addORCID(listaORCID):
    print "-a"

def remORCID(listaORCID):
    print "-r"

def instructions():
    print "HELP:"
    print "\tSart background syncing process:"
    print "\t\tpython background"
    print "\tList ORCID being analyzed:"
    print "\t\tpython background -l"
    print "\tAdd ORCID('s) to be analyzed:"
    print "\t\tpython background -a XXXX-XXXX-XXXX-XXXX"
    print "\t\tpython background -a XXXX-XXXX-XXXX-XXXX YYYY-YYYY-YYYY-YYYY ZZZZ-ZZZZ-ZZZZ-ZZZZ"
    print "\tSRemove ORCID('s) from being analyzed:"
    print "\t\tpython background -r XXXX-XXXX-XXXX-XXXX"
    print "\t\tpython background -r XXXX-XXXX-XXXX-XXXX YYYY-YYYY-YYYY-YYYY ZZZZ-ZZZZ-ZZZZ-ZZZZ"

def background():
    orcidList = ["0000-0003-4121-6169"]
    for orcid in orcidList:
        headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
        r = requests.get('https://pub.orcid.org/v2.1/'+orcid+'/works',headers=headers)
        reqJson = r.json()
        for art in reqJson["group"]:
            artTitle = art["work-summary"][0]["title"]["title"]["value"]
            print orcid + " | " + artTitle


array = sys.argv
del array[0]

if (len(array)==0):
    background()
elif (array[0]=="-l"):
    listORCID()
elif (array[0]=="-a" and verify(array)):
    addORCID(1)
elif (array[0]=="-r" and verify(array)):
    remORCID(1)
else:
    instructions()