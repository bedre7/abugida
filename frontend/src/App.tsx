import React from 'react';
import './App.css';
import Editor from './components/Editor/Editor';
import SideBar from './components/SideBar/SideBar';
import Terminal from './components/Terminal/Terminal';

const App = () => {
  return (
    <div className="App">
      <SideBar/>
      <Editor/> 
      <Terminal/>
    </div>
  );
}

export default App;
