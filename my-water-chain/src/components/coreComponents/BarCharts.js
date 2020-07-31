import React from 'react';
import { Bar } from 'react-chartjs-2';

function BarChart()
{
    const Colors = ['rgba(255,156,86,0.6)','rgba(255,156,86,0.6)',
    'rgba(255,156,86,0.6)','rgba(255,156,86,0.6)',
    'rgba(255,156,86,0.6)'];
    const SecondColors = ['rgba(85,236,86,0.2)','rgba(85,236,86,0.2)',
        'rgba(85,236,86,0.2)','rgba(85,236,86,0.2)',
        'rgba(85,236,86,0.2)'];
    const data ={
        labels: ['Jan','Feb','Mar','Apr','May'],
        datasets:[
            {
                label: 'Consumption for 2020 (M)',
                data: [3,2,2,1,3],
                borderColor: ['rgba(255,156,86,0.6)','rgba(255,156,86,0.6)',
                'rgba(255,156,86,0.6)','rgba(255,156,86,0.6)',
                'rgba(255,156,86,0.6)'],
                backgroundColor: ['rgba(255,156,86,0.6)','rgba(255,156,86,0.6)',
                'rgba(255,156,86,0.6)','rgba(255,156,86,0.6)',
                'rgba(255,156,86,0.6)'],
            },
            {
                label: 'BlockChain Credits Earned',
                data: [3,2,5,1,3],
                borderColor: ['rgba(85,236,86,0.2)','rgba(85,236,86,0.2)',
                'rgba(85,236,86,0.2)','rgba(85,236,86,0.2)',
                'rgba(85,236,86,0.2)'],
                backgroundColor: ['rgba(85,236,86,0.2)','rgba(85,236,86,0.2)',
                'rgba(85,236,86,0.2)','rgba(85,236,86,0.2)',
                'rgba(85,236,86,0.2)'],
            }
        ]

    }
    const options = {
        title: {
            display:true,
            text: 'Bar Chart',

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
    return <Bar className = "Chart-Line-Chart"
    data={data} options={options}/>;
}

export default BarChart;