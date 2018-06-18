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
    this.fetchInfo();
    setInterval(() => { this.fetchInfo() }, 10000);
  }

  fetchInfo() {
    fetch('http://localhost:5000/IS/orcids')
      .then(res => res.json())
      .then(orcs => {
        fetch('http://localhost:5000/IS/arts')
          .then(res => res.json())
          .then(arts => {
            this.setState({
              listAll: arts,
              listOrc: orcs
            })
          });
      });
  }

  newOrcid(orcidValue) {
    const regex = new RegExp(/^[0-9]{4}-[0-9]{4}-[0-9]{4}-[0-9]{4}$/);
    if (regex.test(orcidValue) === false) return;
    fetch('http://localhost:5000/IS/addOrcid?orcid=' + orcidValue, {method: 'POST'})
      .then(() => this.fetchInfo());
  }

  
  remOrcid(orcidValue) {
    this.setState((prevState) => ({
      listOrc: prevState.listOrc.filter(orc => orc.orcid!==orcidValue)
    }));
    fetch('http://localhost:5000/IS/delOrcid?orcid=' + orcidValue, {method: 'POST'})
      .then(() => this.fetchInfo());
  }



  rerender() {
    this.forceUpdate()
  }

  render() {
    console.log(this.state)
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
