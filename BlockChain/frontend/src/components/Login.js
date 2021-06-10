import React, { useState } from 'react';
import final_logo from '../assets/final_logo.png';
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
    <br />
      <img className="final_logo" src={final_logo} alt="application-logo" />
      <div className= "bbox">
      <h3><b>Enter Login Details</b></h3>
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
         LOGIN
        </Button>
      </div>
      </div>
      </div>
  )
}

export default Login;
