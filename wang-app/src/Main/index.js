import React, { Component } from 'react';
import { Switch, Route, BrowserRouter as Router } from 'react-router-dom'

import BookComp from '../components/BookComp'

class Main extends Component {
 render() {
   return (
     <Router>
         <Switch>
           <Route path="/" component={BookComp} />
         </Switch>
     </Router>
   );
 }
}

export default Main;