import React,{ useState } from 'react';
import LineChart from '../coreComponents/LineChart.js';
import LineChaart from '../coreComponents/LineChaart.js';
import Header from '../coreComponents/Header.jsx';
import Button from 'react-bootstrap/Button';
import BarChart from '../coreComponents/BarCharts.js';
import DonutChart from '../coreComponents/DonutChart.js';
import PrettyTable from '../coreComponents/PrettyTable.js';
import HeadersConstant from '../constants/ResponseConstants.js';


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

    function CreateDataSetArray(numberOfElements,plotlabel,plotdata,color)
    {
        let DataSetArray = [];
        let temp = {};
        for(let i = 0;i<numberOfElements;i++)
        {
            temp = {
                label: plotlabel[i],
                data: plotdata[i],
                borderColor: [color[i]],
                backgroundColor: [color[i]],
                pointBackgroundColor:[color[i]],
                pointBorderColor:[color[i]],
            };
            DataSetArray.push(temp);
        }
        return(DataSetArray);

    }

    const jsonData = props.Block_Chain[props.Block_Chain.length-1].water_data;
    let LowedDown = reduce_to_index(jsonData.FlowRate,1000);
    let QuantityIndexed = reduce_to_index(jsonData.Water_Quantity_Index_Day,1500000);
    console.log(props.industry_response);
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
    return(<div className="Display-Screen-Global-Div">
        <Header />
        <Button className="Switch-Button-In-Display" onClick = {switchPurchase}>{ButtonText}</Button>
        {ChartState?<div>
        <PrettyTable Data={props.industry_response} selfData = {props.self_details} Email = {props.email}/>
        </div>:<div><div className="Chart">
        <div className="Chart-Candidate"><LineChart Plot1 = {LowedDown}
        Plot2 = {jsonData.Solid_Waste_Analysis_Index}/></div>

        <div className="Chart-Candidate"> <BarChart Plot1 = {jsonData.Water_Quality_Index_Day}
        Plot2={QuantityIndexed} HH1={HeadersConstant.Water_Quality_Heading}
        HH2 ={HeadersConstant.Water_Quantity_Heading}/></div>
        <div className="Chart-Candidate"><DonutChart ColorSchema={HeadersConstant.Color_For_Credits}
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
        Data={jsonData.Credit_Consumption_History} Label={HeadersConstant.CreditsParamHeading}
            Words={HeadersConstant.CreditWords}/></div>
        </div>
        </div>
        }
        </div>);
}