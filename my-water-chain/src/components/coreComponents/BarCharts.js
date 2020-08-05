import React from 'react';
import { Bar } from 'react-chartjs-2';
import HeadersConstant from '../constants/ResponseConstants.js';
function BarChart(props)
{
    const Colors = ['rgba(255,156,86,0.6)','rgba(255,156,86,0.6)',
    'rgba(255,156,86,0.6)','rgba(255,156,86,0.6)',
    'rgba(255,156,86,0.6)','rgba(255,156,86,0.6)','rgba(255,156,86,0.6)'];
    const SecondColors = ['rgba(85,236,86,0.2)','rgba(85,236,86,0.2)',
        'rgba(85,236,86,0.2)','rgba(85,236,86,0.2)','rgba(85,236,86,0.2)','rgba(85,236,86,0.2)',
        'rgba(85,236,86,0.2)'];
    const data ={
        labels: HeadersConstant.Day_Lables,
        datasets:[
            {
                label: props.HH1,
                data: props.Plot1,
                borderColor: Colors,
                backgroundColor: Colors,
            },
            {
                label: props.HH2,
                data: props.Plot2,
                borderColor: SecondColors,
                backgroundColor: SecondColors,
            }
        ]

    }
    const options = {
        title: {
            display:true,
            text: 'Day Wise Quality/Quantity Performance',

        },
        scales: {
            yAxes: [
                {
                    ticks:{
                        min:0,
                        max:10,
                        stepSize: 1,
                    }
                }
            ]
        }
    }
    return <Bar className = "Chart-Line-Chart"
    data={data} options={options}/>;
}

export default BarChart;