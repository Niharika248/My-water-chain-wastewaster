import React from 'react';
import DashboardDetails from '../constants/WelcomeScreen.js';
import TabularComponent from '../coreComponents/DisplayChart.jsx';
export default function Header()
{
    return(
        <div className="FullSizeContainer">
        <div className="Section-01-Header">
        <TabularComponent />
        </div>
        <div className="Section-02-Header">{DashboardDetails.Heading}</div>
        <div className="Section-03-Header">
        <img src={process.env.PUBLIC_URL +DashboardDetails.LogoName} className="Customize-Logo" alt="Loading..."></img>
        </div>
        </div>
    );
}