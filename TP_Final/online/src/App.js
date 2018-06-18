import React, { Component } from 'react';
import './App.css';
import AppList from './components/AppList'
import AppSidebar from './components/AppSidebar'

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      listAll: [],
      listOrc: []
    }
  }

  componentDidMount() {
    if (localStorage.getItem('listOrc') !== null && localStorage.getItem('listOrc') !== undefined) {
      this.setState({ listOrc: JSON.parse(localStorage.getItem('listOrc')) });
    }
    localStorage.setItem("filter", '');
    setInterval(() => { this.background() }, 10000);

  }

  newOrcid(orcidValue) {
    const regex = new RegExp(/^[0-9]{4}-[0-9]{4}-[0-9]{4}-[0-9]{4}$/);
    if (regex.test(orcidValue) === false) return;
    var orcList = [];
    var orcid = {
      value: orcidValue
    };
    if (localStorage.getItem('listOrc') !== null && localStorage.getItem('listOrc') !== undefined) {
      orcList = JSON.parse(localStorage.getItem('listOrc'))
    }
    var x;
    for (x in orcList) {
      if (orcList[x].value === orcidValue) return;
    }
    orcList = orcList.concat(orcid)
    localStorage.setItem('listOrc', JSON.stringify(orcList));
    this.setState({ listOrc: orcList });
    this.background()
  }
  remOrcid(orcidValue) {
    var orcList = JSON.parse(localStorage.getItem('listOrc')).filter(orc => orc.value !== orcidValue)
    localStorage.setItem('listOrc', JSON.stringify(orcList));
    this.setState({
      listOrc: orcList
    });
    this.background()
  }


  async background() {
    var x;
    var orcList = this.state.listOrc;
    localStorage.setItem('provList', JSON.stringify([]));
    var t0 = performance.now();
    for (x in orcList) {
      var request = require('request-promise');
      await request({
        "method": "GET",
        "uri": "https://pub.orcid.org/v2.1/" + orcList[x].value + "/works",
        "json": true,
        "headers": {
          "content-type": "application/json",
          "Accept-Charset": "UTF-8"
        }
      }).then(reqJson => {
        var list = []

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
          var artTitle, year;
          if (workFL.length === 0) {
            //Caso nenhuma das referencias esteja ligada ao scopus apenas guarda o titulo
            artTitle = art["work-summary"][0]["title"]["title"]["value"]
            year = (art["work-summary"][0]["publication-date"] != null) ? art["work-summary"][0]["publication-date"]["year"]["value"] : '';
            list.push(newArt(artTitle, year, art["last-modified-date"]["value"], ''));
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
            list.push(newArt(artTitle, year, art["last-modified-date"]["value"], scopusID));
          }
        }

        list = JSON.parse(localStorage.getItem('provList')).concat(list);
        localStorage.setItem('provList', JSON.stringify(list));


        function newArt(title, year, lastModDate, scopusA) {
          const item = {
            orcid: orcList[x],
            titulo: title,
            ano: year,
            dataModificacao: lastModDate,
            scopus: scopusA.substr(7)
          }
          return item;
        }
      });
    }

    function arrayUnique(array) {
      var a = array.concat();
      for (var i = 0; i < a.length; ++i) {
        for (var j = i + 1; j < a.length; ++j) {
          if (a[i].orcid["value"] === a[j].orcid["value"] &&
            a[i].titulo === a[j].titulo &&
            a[i].ano === a[j].ano &&
            a[i].dataModificacao === a[j].dataModificacao &&
            a[i].scopus === a[j].scopus) {
            a.splice(j--, 1);
          }
        }
      }

      return a;
    }

    const lista = JSON.parse(localStorage.getItem('provList'));
    localStorage.removeItem('provList');
    this.setState((previousState) => ({
      listAll: arrayUnique(previousState.listAll.concat(lista)).filter(art => {
        return previousState.listOrc.filter(orc => art.orcid["value"] === orc.value).length !== 0;
      })
    }));
    var t1 = performance.now();
    console.log(t1 - t0)
  }

  rerender() {
    this.forceUpdate()
  }

  render() {
    if (this.state.listAll.length === 0 && this.state.listOrc.length !== 0) {
      this.background();
    }
    console.log(this.state);
    return (
      <div className="App">
        <header className="App-header">
          <h1 className="App-title">IS - Sistema ORCID</h1>
        </header>
        <div>
          <div className="mySidebarScopus col-xs-3">
            <AppSidebar
              list={this.state.listOrc}
              addOrcid={(orcid) => this.newOrcid(orcid)}
              remOrcid={(orcid) => this.remOrcid(orcid)}
              render={() => this.rerender()} />
          </div>
          <div className="listDiv col-xs-9 no-padding">
            <AppList
              list={this.state.listAll}
              orcs={this.state.listOrc} />
          </div>
        </div>
      </div>
    );
  }
}

export default App;
