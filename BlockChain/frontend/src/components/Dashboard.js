import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import logo from '../assets/logo.png';
import { API_BASE_URL } from '../config';

function Dashboard() {
  const [accountInfo, setAccountInfo] = useState({});

  useEffect(() => {
    fetch(`${API_BASE_URL}/account/info`)
      .then(response => response.json())
      .then(json => setAccountInfo(json));
  }, []);

  const { name, userid, address, meterid, storage } = accountInfo;

  return (
    <div className="Dashboard">
      <h2><b>Welcome To Your Dashboard</b></h2>
      <hr/>
      <br/>
      <div className="bbox">
      <h3><u><b>Your Account Info</b></u></h3>
        <div>Name: {name}</div>
        <div>UserID: {userid}</div>
        <div>Address: {address}</div>
        <div>Meterid: {meterid}</div>
        <div>Storage: {storage}</div>
      </div>
      <br />
      <br />
      <Link to="/request">Request Energy</Link>
      <br />
      <Link to="/sell-energy">Sell Energy</Link>
      <br />
      <Link to="/blockchain">Blockchain</Link>
      <br />
    </div>
  );
}

export default Dashboard;
