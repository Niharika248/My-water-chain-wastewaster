import React from "react";
import DashboardDetails from '../constants/WelcomeScreen.js';
export default function TabularComponent(props)
{
    return(
        <div>
        <div className="Display-Chart-Blockchain-Coins">{DashboardDetails.WaterCoins+ ": "}</div>
        <div className="Display-Chart-Complex-Block">
        <div className="Display-Chart-Allowance-Coins-01">{DashboardDetails.Allowance+ ": 250 l/day"}</div>
        <div className="Display-Chart-Allowance-Coins-02">{" + "}</div>
        </div>
        
        <div className="Display-Chart-Expires-On">{DashboardDetails.ExpireText+"14th April 2021"}</div>
        </div>
    );
}