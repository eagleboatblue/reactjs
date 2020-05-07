import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import {Router} from 'react-router-dom';
import Main from './Main';
import {createBrowserHistory} from 'history'
// import App from './App';
import * as serviceWorker from './serviceWorker';
import 'semantic-ui-css/semantic.min.css';
import 'bootstrap/dist/css/bootstrap.min.css';

const history = createBrowserHistory();

ReactDOM.render((
  <Router history={history}>
    <Main history={history}/>
  </Router>),
  document.getElementById('root')
);

// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: https://bit.ly/CRA-PWA
serviceWorker.unregister();
