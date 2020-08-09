import React from 'react';
import { Line } from 'react-chartjs-2';
import HeadersConstant from '../constants/ResponseConstants.js';
function LineChaart(props)
{
    const color_01 = ['rgba(164, 227, 94, 0.5)'];
    const color_02 = ['rgba(194, 137, 236, 0.5)'];
    const color_03 = ['rgba(103, 184, 112, 0.8)'];
    const color_04 = ['rgba(177, 219, 231, 0.8)'];
    const data ={
        labels: HeadersConstant.Time_Labels,
        datasets:[
            {
                label: HeadersConstant.Chart_02_Heading_01,
                data: props.Plot1,
                borderColor: color_01,
                backgroundColor: color_01,
                pointBackgroundColor:color_01,
                pointBorderColor:color_01,
            },
            {
                label: HeadersConstant.Chart_02_Heading_02,
                data: props.Plot2,
                borderColor: color_02,
                backgroundColor: color_02,
                pointBackgroundColor:color_02,
                pointBorderColor:color_02,
            },
            {
                label: HeadersConstant.Chart_02_Heading_03,
                data: props.Plot3,
                borderColor: color_03,
                backgroundColor: color_03,
                pointBackgroundColor:color_03,
                pointBorderColor:color_03,
            },
            {
                label: HeadersConstant.Chart_02_Heading_04,
                data: props.Plot4,
                borderColor: color_04,
                backgroundColor: color_04,
                pointBackgroundColor:color_04,
                pointBorderColor:color_04,
            }
        ]

    }
    const options = {
        title: {
            display:true,
            text: 'Quality Analysis Month to Date',

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

export default LineChaart;