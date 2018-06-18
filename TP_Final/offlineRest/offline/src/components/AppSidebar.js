import React, { Component } from 'react';



class AppSidebar extends Component {
    state = {
        data: {
            orcidValue: '',   
        }
    }

    onChangeInput = e => this.setState({ data: { ...this.state.data, orcidValue: e.target.value } })

    render() {
        return (
            <div>
                <div className="row">
                    <input className="w3-input col-xs-12 col-md-9" onChange={this.onChangeInput} value={this.state.data.orcidValue} placeholder="orcid: 0000-0000-0000-0000" />
                    <button className="w3-button col-xs-12 col-md-3 myButton" 
                            onClick={() => {
                                this.props.addOrcid(this.state.data.orcidValue);
                                this.setState({ data: { ...this.state.data, orcidValue: '' } })
                                }} >Inserir</button>
                </div>
                <div className="row sidebarItem">
                            <button className="w3-button col-xs-12" onClick={() => {localStorage.setItem('filter','');this.props.render();}}>TODOS</button>
                    </div>
                {this.props.list.map(orc =>
                    <div className="row sidebarItem">
                            <button className="col-xs-11 w3-padding-small w3-left-align w3-button"
                                    onClick={() => {localStorage.setItem('filter',orc.orcid);this.props.render();}}>
                                    {orc.orcid}
                            </button>
                            <span className="col-xs-1 w3-padding-small w3-right" onClick={() => this.props.remOrcid(orc.orcid)}>✖</span>
                    </div>
                )}
            </div>
        );
    }
}

export default AppSidebar;
