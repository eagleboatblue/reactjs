import React, { Component } from 'react';
import { Switch, Route, BrowserRouter as Router } from 'react-router-dom'

import App from '../App';

class Main extends Component {
 render() {
   return (
     <Router>
         <Switch>
           <Route path="/" component={App} />
         </Switch>
     </Router>
   );
 }
}

export default Main;