import React, { Component } from 'react';
import { Switch, Route, BrowserRouter as Router } from 'react-router-dom'

import Home from '../Home'

class Main extends Component {
 render() {
   return (
     <Router>
         <Switch>
           <Route path="/home" component={Home} />
         </Switch>
     </Router>
   );
 }
}

export default Main;