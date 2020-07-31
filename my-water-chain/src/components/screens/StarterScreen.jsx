import React from 'react';
import Header from '../junk/Header.jsx';
import Authentication from '../AuthenticateCard.jsx';
import { withRouter } from 'react-router-dom';

function StarterScreen(props) {
  function loginClick()
    {
      props.history.push('/login');
    }
    function registerClick()
    {
      props.history.push('/register');
    }
  return (
    <div>
      <Header header="My Water Chain"/>
      <div className="WhiteCard">
      <div className="whiteSpace">
      </div>
      <Authentication text="Login" onClickaction={loginClick} />
      <Authentication text="Register" onClickaction={registerClick}/>
      </div>
    </div>
  );
}

export default withRouter(StarterScreen);
