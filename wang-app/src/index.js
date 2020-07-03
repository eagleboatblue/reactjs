import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
//import {Router} from 'react-router-dom';
import {createBrowserHistory} from 'history'
// import App from './App';
import * as serviceWorker from './serviceWorker';
// mport 'semantic-ui-css/semantic.min.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import App from './App';
import {Route, Router} from 'react-router-dom'

const history = createBrowserHistory();

ReactDOM.render((
  <Router history={history}>
   {/* <Main history={history}/> */}
    <Route path="/" component={App} />
  </Router>),
  document.getElementById('root')
);

// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: https://bit.ly/CRA-PWA
serviceWorker.unregister();
