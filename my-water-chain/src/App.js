import React from 'react';
import StarterScreen from './components/screens/StarterScreen.jsx';
import LoginScreen from './components/screens/LoginScreen.jsx';
import RegisterScreen from './components/screens/RegisterScreen.jsx';
import DisplayScreen from './components/screens/DisplayScreen.jsx';
import 'bootstrap/dist/css/bootstrap.min.css';
//import LineChart from './components/coreComponents/LineChart.js';
import ProtectedRoute from './components/security/PrivateRoute.jsx';
import './App.css';
import {BrowserRouter,Route,Switch} from 'react-router-dom';
  function App(){
    return (
    <div className="App">
    <BrowserRouter>
    <Switch>
    <Route component={StarterScreen} exact path="/"></Route>
    <Route component={RegisterScreen} exact path="/register"></Route>
    <Route component={LoginScreen} exact path="/login"></Route>
    <ProtectedRoute component={DisplayScreen} exact path="/login-props-test" />
    </Switch>
    </BrowserRouter>
    </div>
  );
    }

export default App;
