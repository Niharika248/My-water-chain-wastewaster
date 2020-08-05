import React from 'react';
import { Line } from 'react-chartjs-2';
import HeadersConstant from '../constants/ResponseConstants.js';
function LineChart(props)
{
    const Color_01 = ['rgba(0,0,255,0.5)'];
    const Color_02 = ['rgba(240,160,255,0.4)'];
    const data ={
        labels: HeadersConstant.Time_Labels,
        datasets:[
            {
                label: HeadersConstant.Chart_01_Heading_01,
                data: props.Plot1,
                borderColor: Color_01,
                backgroundColor: Color_01,
                pointBackgroundColor:Color_01,
                pointBorderColor:Color_01,
            },
            {
                label: HeadersConstant.Chart_01_Heading_02,
                data: props.Plot2,
                borderColor: Color_02,
                backgroundColor: Color_02,
                pointBackgroundColor:Color_02,
                pointBorderColor:Color_02,
            }
        ]

    }
    const options = {
        title: {
            display:true,
            text: 'SWA and Flow Rate Index',

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
    return <Line className = "Chart-Line-Chart"
    data={data} options={options}/>;
}

export default LineChart;