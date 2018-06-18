
const express = require('express');
var bodyParser = require('body-parser');
var JsonParser = bodyParser.json();
var urlencodedParser = bodyParser.urlencoded({ extended: false })

const app = express();
app.use(bodyParser());
const port = process.env.PORT || 5000;
var mysql = require('mysql')
var array;
var connection = mysql.createConnection({
  host: 'localhost',
  user: 'root',
  password: '',
  database: 'ISfinal'
});


connection.connect(function (err) {
  if (err) throw err
  console.log('You are now connected...')
})

app.get('/IS/orcids', function (req, res) {
  sql = 'Select orcid From Orcid'
  connection.query(sql, function (err, results) {
    if (err) throw err
    res.header("Access-Control-Allow-Origin", "*");
    res.header("Access-Control-Allow-Headers");
    res.send(JSON.stringify(results));
  })
});

app.post('/IS/addOrcid', function (req, res) {
  sql = 'Select orcid From Orcid where orcid=\'' + req.query.orcid + '\''
  connection.query(sql, function (err, results) {
    if (err) throw err
    if (results.length === 0) {
      sql = "Insert into ISfinal.Orcid(orcid) values (\"" + req.query.orcid + "\");";
      connection.query(sql, function (err, results) {
        if (err) throw err
        background();
        res.header("Access-Control-Allow-Origin", "*");
        res.header("Access-Control-Allow-Headers");
        res.send(JSON.stringify(results));
      });
    }
    else {
      res.header("Access-Control-Allow-Origin", "*");
      res.header("Access-Control-Allow-Headers");
      res.send(JSON.stringify(results));
    }
  })
});

app.post('/IS/delOrcid', function (req, res) {
  sql = "delete from Artigos where idArtigos in (Select idArtigos from  Orcid_has_Artigos where Orcid_has_Artigos.idOrcid = ( Select idOrcid from Orcid where Orcid.orcid=\'" + req.query.orcid + "\'));"
  connection.query(sql, function (err, results) {
    if (err) throw err
    sql = "Delete from Orcid where orcid=\"" + req.query.orcid + "\";"
    connection.query(sql, function (err, results) {
      if (err) throw err
      res.header("Access-Control-Allow-Origin", "*");
      res.header("Access-Control-Allow-Headers");
      res.send(JSON.stringify(results));
    })
  })
});

app.get('/IS/arts', function (req, res) {
  sql = 'SELECT Orcid.orcid, Artigos.titulo, Artigos.ano, Artigos.scopus FROM Artigos, Orcid_has_Artigos, Orcid WHERE Artigos.idArtigos = Orcid_has_Artigos.idArtigos and Orcid_has_Artigos.idOrcid = Orcid.idOrcid ORDER BY Artigos.lastModifiedDate DESC;'
  connection.query(sql, function (err, results) {
    if (err) throw err
    res.header("Access-Control-Allow-Origin", "*");
    res.header("Access-Control-Allow-Headers");
    res.send(JSON.stringify(results));
  })
});





app.listen(port, () => console.log(`Listening on port ${port}`));




async function background() {
  var x;
  sql = 'Select * From Orcid'
  connection.query(sql, async function (err, results) {
    if (err) throw err
    var orcList = results;
    var provList = []
    var idArt = 0;
    for (x in orcList) {
      var request = require('request-promise');
      await request({
        "method": "GET",
        "uri": "https://pub.orcid.org/v2.1/" + orcList[x].orcid + "/works",
        "json": true,
        "headers": {
          "content-type": "application/json",
          "Accept-Charset": "UTF-8"
        }
      }).then(reqJson => {
        var i;
        for (i in reqJson["group"]) {
          var art = reqJson["group"][i];
          var workFL = [];
          //Verifica se alguma das referencias de um artigo tem ligacao ao scopus se tiver adiciona a lista WorkFL
          var z;
          var eid;
          for (z in art["work-summary"]) {
            var work = art["work-summary"][z];
            var y;
            for (y in work["external-ids"]["external-id"]) {
              eid = work["external-ids"]["external-id"][y];
              if (eid["external-id-type"] === "eid") {
                workFL.push([work])
              }
            }
          }
          var artTitle = '';
          var year = 0;
          if (workFL.length === 0) {
            //Caso nenhuma das referencias esteja ligada ao scopus apenas guarda o titulo
            artTitle = art["work-summary"][0]["title"]["title"]["value"]
            year = (art["work-summary"][0]["publication-date"] != null) ? art["work-summary"][0]["publication-date"]["year"]["value"] : '';
            idArt = idArt + 1;
            provList.push(newArt(idArt, artTitle, year, art["last-modified-date"]["value"], ''));
          }
          else {
            //Caso hajam varias referencias com ligacao ao scopus analisa a que tem display-index menor
            var workF = workFL[0]
            var k;
            for (k in workFL) {
              work = workFL[k];
              if (parseInt(work["display-index"], 10) < parseInt(workF["display-index"], 10)) {
                workF = work
              }
            }
            artTitle = workF[0]["title"]["title"]["value"]
            year = workF[0]["publication-date"]["year"]["value"]
            var scopusID = ""
            var it;
            for (it in workF[0]["external-ids"]["external-id"]) {
              eid = workF[0]["external-ids"]["external-id"][it];
              if (eid["external-id-type"] === "eid") {
                scopusID = eid["external-id-value"]
              }
            }
            idArt = idArt + 1;
            provList.push(newArt(idArt, artTitle, year, art["last-modified-date"]["value"], scopusID));
          }
        }


        function newArt(idArt, title, year, lastModDate, scopusA) {
          const item = {
            idArt: idArt,
            idOrcid: orcList[x].idOrcid,
            orcid: orcList[x].orcid,
            titulo: title,
            ano: year,
            dataModificacao: lastModDate,
            scopus: scopusA.substr(7)
          }
          return item;
        }
      });
    }


    var sqlOA = '';
    var sqlA = '';
    var i;
    for (i in provList) {
      sqlA = sqlA + ', (' + provList[i].idArt + ',\"' + provList[i].titulo + '\",' + ((provList[i].ano === "") ? null : provList[i].ano) + ',' + provList[i].dataModificacao + ',\"' + provList[i].scopus + '\")';
      sqlOA = sqlOA + ', (' + provList[i].idArt + ',' + provList[i].idOrcid + ')';
    }
    connection.query("Delete from Orcid_has_Artigos", async function (err, results) {
      if (err) throw err
    })
    connection.query("Delete from Artigos", async function (err, results) {
      if (err) throw err
    })
    sqlA = 'INSERT INTO Artigos (idArtigos, titulo, ano, lastModifiedDate, scopus) VALUES' + sqlA.substr(1) + ';';
    connection.query(sqlA, async function (err, results) {
      if (err) throw err
    })
    sqlOA = 'INSERT INTO Orcid_has_Artigos (idArtigos, idOrcid) VALUES' + sqlOA.substr(1) + ';';
    connection.query(sqlOA, async function (err, results) {
      if (err) throw err
    })
  })
}


background()

setInterval(() => { background() }, 10000);