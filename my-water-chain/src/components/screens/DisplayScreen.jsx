import React,{ useState } from 'react';
import LineChart from '../coreComponents/LineChart.js';
import LineChaart from '../coreComponents/LineChaart.js';
import Header from '../coreComponents/Header.jsx';
import Button from 'react-bootstrap/Button';
import BarChart from '../coreComponents/BarCharts.js';
import DonutChart from '../coreComponents/DonutChart.js';
import PrettyTable from '../coreComponents/PrettyTable.js';
import HeadersConstant from '../constants/ResponseConstants.js';
import {ipaddress} from '../constants/dummyconstantfiles.js';

export default function DisplayScreen(props)
{
    function reduce_to_index(data,factor)
    {
        let LowedDown = [];
        for(let i=0;i<data.length;i++)
    {
        LowedDown.push(data[i]/factor);
    }
    return(LowedDown);
    }
    const jsonData = props.Block_Chain[props.Block_Chain.length-1].water_data;
    let LowedDown = reduce_to_index(jsonData.FlowRate,1000);
    let QuantityIndexed = reduce_to_index(jsonData.Water_Quantity_Index_Day,1500000);
    const [ChartState,changeChartState] = useState(false);
    const [ButtonText,changeButtonText] = useState("Switch to Purchase Screen");
    const streamSession = "Generate Stream Session";
    function switchPurchase()
    {
        changeChartState(prev=>{
            return(!prev);
        });
        changeButtonText(prev=>{
            if(prev==="Switch to Purchase Screen")
            return("Switch to Dashboard Screen");
            else
            return("Switch to Purchase Screen");

        });
        
    }
    const generatePurchase = async()=>
    {
        const res = await fetch(`${ipaddress}livepeer-streaming`,{
            method: 'POST',
            headers:{
              'Content-Type':'application/json'
            },
            body:JSON.stringify({"email":props.email})
          }).then(response=>response.json()).then(
              finalbody=>{alert(`Your stream generated url is ${finalbody.url}. Note that the url will automatically expire after 30 mins. You may renew it here. You can stream your session @ https://videojs.github.io/videojs-contrib-hls/`);}
          );



    }
    return(<div className="Display-Screen-Global-Div">
        <Header />
        <div className="UI-Aligner"><Button className="Switch-Button-In-Display UI-Button-Click"
        onClick = {generatePurchase}>{streamSession}</Button>
        <Button className="Switch-Button-In-Display UI-Button-Click"
        onClick = {switchPurchase}>{ButtonText}</Button>
        </div>
        {ChartState?<div>
        <PrettyTable Data={props.industry_response} selfData = {props.self_details} Email = {props.email}/>
        </div>:<div><div className="Chart">
        <div className="Chart-Candidate"><LineChart Plot1 = {LowedDown}
        Plot2 = {jsonData.Solid_Waste_Analysis_Index}/></div>

        <div className="Chart-Candidate"> <BarChart Plot1 = {jsonData.Water_Quality_Index_Day}
        Plot2={QuantityIndexed} HH1={HeadersConstant.Water_Quality_Heading}
        HH2 ={HeadersConstant.Water_Quantity_Heading}/></div>
        <div className="Chart-Candidate"><DonutChart ColorSchema={HeadersConstant.Color_For_Credits} Texts={"Quality Index"}
        Data={[jsonData.Quality_Analysis.SPI,jsonData.Quality_Analysis.CDI,jsonData.Quality_Analysis.SWI,
            jsonData.Quality_Analysis.HSI]} Label={HeadersConstant.QualityParamsHeading}
            Words={HeadersConstant.QualityWords} LabelTime = {HeadersConstant.Time_Labels}/></div>
        </div>
        <div className="Chart">
        <div className="Chart-Candidate"><LineChaart Plot1 = {jsonData.Previous_Comparision.Yesterday_Quality}
        Plot2 = {jsonData.Previous_Comparision.Last3Day_Quality}
        Plot3 = {jsonData.Previous_Comparision.Last7Day_Quality}
        Plot4 = {jsonData.Previous_Comparision.Monthly_Quality}/></div>

        <div className="Chart-Candidate"> <BarChart Plot1 = {jsonData.Stable_Comparision.Stable_Quality}
        Plot2={jsonData.Stable_Comparision.Self_Quality} HH1={HeadersConstant.StableHeading} HH2={HeadersConstant.SelfHeading}/></div>
        <div className="Chart-Candidate"><DonutChart
        Data={jsonData.Credit_Consumption_History} Label={HeadersConstant.CreditsParamHeading} Texts={"Credit Consumption"}
            Words={HeadersConstant.CreditWords}/></div>
        </div>
        </div>
        }
        </div>);
}