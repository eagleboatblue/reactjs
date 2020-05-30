import React, { PureComponent } from 'react';
import logo from './logo.svg';
import './App.css';
import Greet from './components/Greet'
import Welcome from './components/Welcome'
import Message from './components/Message'
import Counter from './components/Counter'
import FunctionClick from './components/FunctionClick'
import ClassClick from './components/ClassClick'
import EventBind from './components/EventBind'
import ParentComponent from './components/ParentComponent'
import UserGreeting from './components/UserGreeting'
import NameList from './components/NameList'
import Stylesheet from './components/Stylesheet'
import Inline from './components/Inline'
import './appStyles.css'
import stylesModule from './appStyles.module.css'
import LifecycleA from './components/LifecycleA'
import PureComp from './components/PureComp'
import ParentComp from './components/ParentComp'

function App() {
  return (
    <div className="App">
      <ClassClick />
      {/* <LifecycleA /> */}
      {/* <h1 className='error'>Error</h1>
      <h1 className={stylesModule.success}>Success</h1>
       <Inline />  */}
      {/* <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header> */}
    </div>
  );
}

export default App;
