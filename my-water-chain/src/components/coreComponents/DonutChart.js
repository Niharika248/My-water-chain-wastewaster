import React from 'react';
import { Doughnut } from 'react-chartjs-2';

function DonutChart(props)
{
    const Color = ['rgba(255,156,86,0.6)','rgba(250,100,100,0.6)','rgba(100,250,200,0.6)',
    'rgba(120,120,120,0.5)','rgba(120,240,120,0.5)','rgba(60,120,240,0.6)','rgba(200,120,120,0.5)','rgba(120,120,250,0.5)'];
    const data ={
        labels: props.Words,
        datasets:[
            {
                label: props.Label,
                data: props.Data,
                borderColor: Color,
                backgroundColor: Color,
            }
        ]

    }
    const options = {
        title: {
            display:true,
            text: props.Texts,

        }
    }
    return <Doughnut className = "Chart-Line-Chart"
    data={data} options={options}/>;
}

export default DonutChart;