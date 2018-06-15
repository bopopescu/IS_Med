import React, { Component } from 'react';



class AppList extends Component {
    render() {
      var filter = localStorage.getItem('filter')
      console.log(filter)
      return (
        <table className="w3-table-all">
        <thead>
          <tr>
            <th>Orcid</th>
            <th>Titulo</th>
            <th>Ano</th>
            <th>Scopus</th>
          </tr>
        </thead>
        <tbody>
          {
            this.props.list
            .filter(art => {
              if (filter==='') return true;
              else return (art.orcid["value"]===filter);
            })
            .sort((a,b) => {return b.dataModificacao-a.dataModificacao})
            .map(art => (
              <tr className='tableHover'>
                <td>{art.orcid["value"]}</td>
                <td>{art.titulo}</td>
                <td>{art.ano}</td>
                <td>{art.scopus}</td>
              </tr>
            ))
          }
        </tbody>
      </table>
      );
    }
  }
  
  export default AppList;
  