import React from 'react';
import ReactDOM from 'react-dom';
import { Router, Switch, Route } from 'react-router-dom';
import './index.css';
import history from './history';
import App from './components/App';
import Blockchain from './components/Blockchain';
import ConductTransaction from './components/ConductTransaction';
import TransactionPool from './components/TransactionPool';
import Login from './components/Login';
import Dashboard from './components/Dashboard';
import Request from './components/Request';
ReactDOM.render(
  <Router history={history}>
    <Switch>
      <Route path='/' exact component={Login}/>
      <Route path='/app' component={App} />
      <Route path='/blockchain' component={Blockchain} />
      <Route path='/conduct-transaction' component={ConductTransaction} />
      <Route path='/transaction-pool' component={TransactionPool} />
      <Route path='/dashboard' component={Dashboard} />
      <Route path='/request' component={Request} />
    </Switch>
  </Router>,
  document.getElementById('root')
);
