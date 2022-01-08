import React, { Component } from 'react'

export class Nav extends Component {
    render() {
        return (
            <div>
<nav className="navbar navbar-light bg-light">
  <div className="container-fluid">
    <a className="navbar-brand d-flex align-items-center " href="#">
      <img src="logo.png" alt="" width="50" height="44" className="d-inline-block align-text-top mx-4"/>
      Animal Intrusion Detection System
    </a>
  </div>
</nav>
            </div>
        )
    }
}

export default Nav
