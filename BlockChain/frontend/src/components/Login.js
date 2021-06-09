import React, { useState } from 'react';
import logo from '../assets/logo.png';
import { API_BASE_URL } from '../config';
import history from '../history';
import { FormGroup, FormControl, Button } from 'react-bootstrap';

function Login() {

  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');

  const updateUsername = event => {
    setUsername(event.target.value);
  }

  const updatePassword = event => {
    setPassword(event.target.value);
  }

  const submitCredentials = () => {
    fetch(`${API_BASE_URL}/account/login`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ username, password })
    }).then(response => response.json())
      .then(json => {
        if(json.status)
        { 
         alert('Success!');
         history.push('/dashboard');
        }
        else
          alert('Invalid Userid or password!');   
      });
  }

  return (
    <div className="Login">
      <img className="logo" src={logo} alt="application-logo" />
      <h3>Enter Login Details</h3>
      <hr />
      <br />
      <FormGroup>
        <FormControl
          input="text"
          placeholder="Enter Username"
          value={username}
          onChange={updateUsername}
        />
      </FormGroup>
      <FormGroup>
        <FormControl
        type = "password"
          input="text"
          placeholder="Enter Password"
          value={password}
          onChange={updatePassword}
        />
      </FormGroup>
      <div>
        <Button
          variant="danger"
          onClick={submitCredentials}
        >
          Submit
        </Button>
      </div>
      </div>
  )
}

export default Login;
