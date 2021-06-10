import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import { FormGroup, FormControl, Button } from 'react-bootstrap';
import { API_BASE_URL } from '../config';
import history from '../history';

function Request() {
  const [quantity, setQuantity] = useState(0);

  const updateQuantity = event => {
    setQuantity(event.target.value);
  }

  const submitQuantity = () => {
    fetch(`${API_BASE_URL}/account/request`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ quantity })
    }).then(response => response.json())
      .then(json => {
        console.log('submitQuantity json', json);
        if(json.status)
        {
        alert('Energy Transaction Completed!!');
        history.push('/dashboard');
        }
        else
        alert('Insufficient Balance, Request lower energy!!');
      });
  }

  return (
    <div className="Request">
      <h2><b>Request Energy</b></h2>
      <br/>  
      <hr />
      <br />
      <FormGroup>
        <FormControl
          input="text"
          placeholder="Enter amount of energy"
          value={quantity}
          onChange={updateQuantity}
        />
      </FormGroup>
      <div>
        <Button
          variant="danger"
          onClick={submitQuantity}
        >
        Request
        </Button>
      </div>
      <br/>
      <hr/>
      <Link to="/dashboard">Go Back To Dashboard</Link>
      <br />
    </div>
  )
}

export default Request;
