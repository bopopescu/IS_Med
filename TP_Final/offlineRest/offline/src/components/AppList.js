import React, { Component } from 'react';



class AppList extends Component {
    render() {
      var filter = localStorage.getItem('filter')
      var list = [];
      if(this.props.orcs.length!==0) {
        list = this.props.list
        .filter(art => {
          if (filter==='') return true;
          else return (art.orcid===filter);
        })
      }
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
            list.map(art => (
                <tr className='tableHover'>
                  <td>{art.orcid}</td>
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
  