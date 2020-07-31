import React,{ useState } from 'react';
import LineChart from '../coreComponents/LineChart.js';
import Header from '../coreComponents/Header.jsx';
import Button from 'react-bootstrap/Button';
import BarChart from '../coreComponents/BarCharts.js';
import DonutChart from '../coreComponents/DonutChart.js';
import PrettyTable from '../coreComponents/PrettyTable.js';
export default function DisplayScreen(props)
{
    const [ChartState,changeChartState] = useState(false);
    const [ButtonText,changeButtonText] = useState("Switch to Purchase Screen");
    function switchPurchase()
    {
        changeChartState(prev=>!prev);
        changeButtonText(prev=>{
            if(prev==="Switch to Purchase Screen")
            return("Switch to Chart Screen");
            else if(prev==="Switch to Chart Screen")
            return("Switch to Purchase Screen");
        });
    }
    return(<div class="Display-Screen-Global-Div">
        <Header />
        <Button className="Switch-Button-In-Display" onClick = {switchPurchase}>{ButtonText}</Button>
        {ChartState?<div>
        <PrettyTable />
        </div>:<div><div className="Chart">
        <div className="Chart-Candidate"><LineChart /></div>
        <div className="Chart-Candidate"> <BarChart /></div>
        <div className="Chart-Candidate"><DonutChart /></div>
        </div>
        <div className="Chart">
        <div className="Chart-Candidate"><LineChart /></div>
        <div className="Chart-Candidate"> <BarChart /></div>
        <div className="Chart-Candidate"><DonutChart /></div>
        </div>
        </div>
        }
        </div>);
}