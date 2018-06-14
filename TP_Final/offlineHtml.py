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
                            <meta charset=UTF-8/>
                            <link rel="stylesheet" type="text/css" href="index.css">
                            <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
                            <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
                            <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
                            <title>Offline HTML</title>
                        </head>
                        <header class="header">
                            <div class="row">
                                <h2 class="title">IS - Sistema ORCID</h2>
                            </div>
                        </header>
                        <body>
                            <script>
                                $(document).ready(function(){
                                    $('[data-toggle="tooltip"]').tooltip();   
                                });
                            </script>
                            <div id="text-container">
                                <p id="texto"> O sistema <em>ORCID</em> <a href="http://orcid.org">(http://orcid.org)</a> fornece um identificador único a cada investigador, que o distingue de qualquer outro, e suporta
                                    ligações automáticas com outros repositórios científicos (tais como o <em>SCOPUS</em> ou o <em>RESEARCHID</em>), garantindo o reconhecimento do
                                    trabalho realizado.<br>
                                    Esta página Web permite listar as várias informações de cada <em>orcid</em> recolhido de forma totalmente <b><em>offline</em></b>, ou seja, diretamente da Base De Dados onde a informação se encontra
                                    guardada.
                                </p>
                            </div>""")


def renderTablePage(table):
    table.write(""" <!DOCTYPE html>
                    <html lang="en">
                        <head>
                            <meta charset=UTF-8/>
                            <link rel="stylesheet" type="text/css" href="index.css">
                            <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
                            <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
                            <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
                            <title>Offline HTML</title>
                        </head>
                        <header class="header">
                            <div class="row">
                                <h2 class="title">IS - Sistema ORCID</h2>
                            </div>
                        </header>
                        <body>
                            <script>
                                    $(document).ready(function(){
                                        $('[data-toggle="tooltip"]').tooltip();   
                                    });
                            </script>
                            <div id="text-container">
                                <p id="texto"> Na tabela seguinte encontra-se toda a informação recolhida na Base de Dados para a opção selecionada selecionada:
                                </p>
                            </div>
                                <table id="tabelas" border='1' width = "80%">
                                <tr>
                                    <th id ="tituloTabelas"><em>Orcid</em></th>
                                    <th id ="tituloTabelas"><em>putCode</em></th>
                                    <th id ="tituloTabelas"><em>lastModifiedDate</em></th>
                                    <th id ="tituloTabelas"><em>titulo</em></th>
                                    <th id ="tituloTabelas"><em>ano</em></th>
                                    <th id ="tituloTabelas"><em>localpub</em></th>
                                    <th id ="tituloTabelas"><em>scopus</em></th>
                                </tr>""")

def createTable(id_Orcid):
    orcid = getOrcidFromId(id_Orcid)
    table = open('table' + orcid + '.html', "w")
    renderTablePage(table)
    for tuples in has_artigos:
        if tuples[0] == id_Orcid:
            art = getArtigoFromId(tuples[1])

            table.write("<tr>")
            table.write("<td id ='elemTabelas'>{0}</td>".format(orcid))
            table.write("<td id ='elemTabelas'>{0}</td>".format(art[1]))
            table.write("<td id ='elemTabelas'>{0}</td>".format(art[2]))
            table.write("<td id ='elemTabelas'>{0}</td>".format(art[3]))
            table.write("<td id ='elemTabelas'>{0}</td>".format(art[4]))
            table.write("<td id ='elemTabelas'>{0}</td>".format(art[5]))
            table.write("<td id ='elemTabelas'>{0}</td>".format(art[6]))

    table.write("</tr>")
    table.write("</table>")
    table.write("""
                                <div id="footer">
                                    <p id="footer_text">Realizado
                                        <a href="#" data-toggle="tooltip" data-placement="top" data-html="true" title="Bruno Sousa A74330<br>Adriana Guedes A74545<br>Marco Barbosa A75278<br>Ricardo Certo A75315 ">por:</a>
                                    </p>
                                </div>
                            </body>
                        </html>""")


def createAllTables():
    tables = open("allTables.html", "w")
    renderTablePage(tables)


    for frst in has_artigos:
        orcid = getOrcidFromId(frst[0])
        art = getArtigoFromId(frst[1])
        tables.write("<tr>")
        tables.write("<td id ='elemTabelas'>{0}</td>".format(orcid))
        tables.write("<td id ='elemTabelas'>{0}</td>".format(art[1]))
        tables.write("<td id ='elemTabelas'>{0}</td>".format(art[2]))
        tables.write("<td id ='elemTabelas'>{0}</td>".format(art[3]))
        tables.write("<td id ='elemTabelas'>{0}</td>".format(art[4]))
        tables.write("<td id ='elemTabelas'>{0}</td>".format(art[5]))
        tables.write("<td id ='elemTabelas'>{0}</td>".format(art[6]))

    tables.write("</tr>")
    tables.write("</table>")
    tables.write("""
                                        <div id="footer">
                                            <p id="footer_text">Realizado 
                                                <a href="#" data-toggle="tooltip" data-placement="top" data-html="true" title="Bruno Sousa A74330<br>Adriana Guedes A74545<br>Marco Barbosa A75278<br>Ricardo Certo A75315 ">por:</a>
                                            </p>
                                        </div>
                                    </body>
                                </html>""")

def renderAllButton():
    index.write("""
                            <div id = "all_button_div">
                                 <a href ={0} class ="btn btn-default" id ="all_button" >Mostrar Todos os Orcid </a>
                            </div>""".format('allTables.html'))



def renderSelectButton():
    idOrcids = []
    index.write("""
                            <div class="dropdown">
                                <button class="btn dropdown-toggle" id ="botao" type="button" data-toggle="dropdown">Selecionar Orcid  <span class="caret"></span></button>
                                <ul class="dropdown-menu">""")
    for frst in has_artigos:
        idOrcids.append(frst)

    difOrcids = list(dict(idOrcids).items())
    for difs in difOrcids:
        createTable(difs[0])
        orcid = getOrcidFromId(difs[0])
        index.write("""
                                    <li id = "botao_elems"><a href={0}>{1}</a></li>""".format('table'+orcid+'.html', orcid))
    index.write("""
                                </ul>""")
    index.write("""
                            </div>""")
    index.write("""
                                <div id="footer">
                                    <p id="footer_text">Realizado
                                        <a href="#" data-toggle="tooltip" data-placement="top" data-html="true" title="Bruno Sousa A74330<br>Adriana Guedes A74545<br>Marco Barbosa A75278<br>Ricardo Certo A75315 ">por:</a>
                                    </p>
                                </div>
                            </body>
                        </html>""")



def selectHasArtigos(conn, cursor):
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



htmlTop()
conn, cursor = connectionDB()
has_artigos = selectHasArtigos(conn, cursor)
renderAllButton()
renderSelectButton()
createAllTables()
cursor.close()
index.close()
webbrowser.open_new_tab('index.html')

