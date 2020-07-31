import React from 'react';
import { Line } from 'react-chartjs-2';

function LineChart()
{
    const data ={
        labels: ['Jan','Feb','Mar','Apr','May'],
        datasets:[
            {
                label: 'Consumption for 2020 (M)',
                data: [3,2,2,1,3],
                borderColor: ['rgba(255,206,86,0.2)'],
                backgroundColor: ['rgba(255,206,86,0.2)'],
                pointBackgroundColor:['rgba(255,206,86,0.2)'],
                pointBorderColor:['rgba(255,206,86,0.2)'],
            },
            {
                label: 'BlockChain Credits Earned',
                data: [3,2,5,1,3],
                borderColor: ['rgba(255,236,86,0.2)'],
                backgroundColor: ['rgba(255,236,86,0.2)'],
                pointBackgroundColor:['rgba(255,236,86,0.2)'],
                pointBorderColor:['rgba(255,236,86,0.2)'],
            }
        ]

    }
    const options = {
        title: {
            display:true,
            text: 'Line Chart',

        },
        scales: {
            yAxes: [
                {
                    ticks:{
                        min:0,
                        max:6,
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