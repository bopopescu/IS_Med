import mysql.connector
import webbrowser


def connectionDB():
    conn = mysql.connector.connect(
            user='root',
            password='',
            host='127.0.0.1',
            database='isfinal')
    cursor = conn.cursor()
    return conn, cursor


index = open("index.html", "w")

def htmlTop():
    index.write(""" <!DOCTYPE html>
                    <html lang="en">
                        <head>
                            <link rel="stylesheet" type="text/css" href="index.css">
                            <link rel="stylesheet" href="https://www.w3schools.com/lib/w3-colors-flat.css">
                            <link rel="stylesheet" type="text/css" href="w3.css">
                            <meta charset="utf-8"/>
                            <title>Offline HTML</title>
                        </head>
                        <header class="w3-container w3-flat-wet-asphalt">
                            <div class="row">
                                <div class="col-md-10 col-xs-12">
                                <h2 class="title w3-margin w3-jumbo">IS - Sistema ORCID</h2>
                                </div>
                            </div>
                        </header>
                        <body>""")

def htmlTail():
    index.write("""<footer class="w3-container w3-padding-64 w3-center w3-opacity">
                        <p>Powered by
                            <a >Grupo 5</a>
                        </p>
                    </footer>
                </body>
            </html>""")



def selectHasArtigos(conn,cursor):
   sql = "SELECT * FROM isfinal.orcid_has_artigos"
   cursor.execute(sql)
   has_artigos = cursor.fetchall()
   return has_artigos


def getArtigoFromId(id):
    sql = "SELECT * FROM isfinal.artigos WHERE idArtigos = %s" %id
    cursor.execute(sql)
    artigo = cursor.fetchone()
    return artigo

def getOrcidFromId(id):
    sql = "SELECT orcid FROM isfinal.orcid WHERE idOrcid = %s" %id
    cursor.execute(sql)
    orcid = cursor.fetchone()
    return orcid[0]


def createTable():
    index.write("<table border='1'>")
    index.write("<tr>")
    index.write("<th>Orcid</th>")
    index.write("<th>putCode</th>")
    index.write("<th>lastModifiedDate</th>")
    index.write("<th>titulo</th>")
    index.write("<th>ano</th>")
    index.write("<th>localpub</th>")
    index.write("<th>scopus</th>")
    index.write("</tr>")

    for frst in has_artigos:
        orcid = getOrcidFromId(frst[0])
        art = getArtigoFromId(frst[1])
        index.write("<tr>")
        index.write("<td>{0}</td>".format(orcid))
        index.write("<td>{0}</td>".format(art[1]))
        index.write("<td>{0}</td>".format(art[2]))
        index.write("<td>{0}</td>".format(art[3]))
        index.write("<td>{0}</td>".format(art[4]))
        index.write("<td>{0}</td>".format(art[5]))
        index.write("<td>{0}</td>".format(art[6]))
        index.write("</tr>")
    index.write("</table>")

htmlTop()

conn, cursor = connectionDB()
has_artigos = selectHasArtigos(conn, cursor)
createTable()
cursor.close()

htmlTail()
index.close()
webbrowser.open_new_tab('index.html')

