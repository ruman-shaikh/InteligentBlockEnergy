import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import { Button } from 'react-bootstrap';
import Etran from './Etran';
import { API_BASE_URL, SECONDS_JS } from '../config';
import history from '../history';
import { FormGroup, FormControl } from 'react-bootstrap';

const POLL_INTERVAL = 10 * SECONDS_JS;
function SellEnergy() {
  const [etrandata, setEtrandata] = useState([]);
  const [etuid, setEtuid] = useState('');

  const fetchEtrandata = () => {
    fetch(`${API_BASE_URL}/account/etran`)
      .then(response => response.json())
      .then(json => {
        console.log('Etran json', json);

        setEtrandata(json);
      });
  }


  const updateEtuid = event => {
    setEtuid(event.target.value);
  }

  const submitEtuid = () => {
    fetch(`${API_BASE_URL}/account/esell`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ etuid })
    }).then(response => response.json())
      .then(json => {
        console.log('submitEtuid json', json);
        if(json.status)
        {
        alert('Energy Transaction Completed!!');
        history.push('/dashboard');
        }
        else
        alert('Transaction Failed, ETUID not found');
      });
    }
   useEffect(() => {
    fetchEtrandata();

    const intervalId = setInterval(fetchEtrandata, POLL_INTERVAL);

    return () => clearInterval(intervalId);
  }, []);

  return (
    <div className="SellEnergy">
      <hr />
      <h3>Please copy paste an etuid from the available list below</h3>
      <br/>
      <FormGroup>
        <FormControl
          input="text"
          placeholder="Enter Etuid"
          value={etuid}
          onChange={updateEtuid}
        />
      </FormGroup>
      <div>
        <Button
          variant="danger"
          onClick={submitEtuid}
        >Sell
        </Button>
      </div>
      <br />
      <h3>Available Etuids</h3>
      <div>
        {
          etrandata.map(etran => (
            <div key={etran.etuid}>
              <hr />
              <Etran etran={etran} />
            </div>
          ))
        }
      </div>
      <hr />
      <br/>
      <br/>
            <Link to="/dashboard">Back To Dashboard</Link>
    </div>
  )
}

export default SellEnergy;