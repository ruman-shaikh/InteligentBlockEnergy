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
      <h2>Welcome to your dashboard</h2>
      <hr/>
      <br />
      <h3>Your Account Info</h3>
      <br/>
      <div className="AccountInfo">
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
      <Link to="/transaction-pool">Sell Energy</Link>
      <br />
      <Link to="/blockchain">Blockchain</Link>
      <br />
      
    </div>
  );
}

export default Dashboard;
