import React from 'react';
import DummyDetails from '../constants/dummyconstantfiles.js';
function PrettyTable(props)
{
    return(
        <div className = "Purchase-View">
        <div className = "Purchase-View-Heading">Purchase Water Drops</div>
        <div className = "Purchase-Table">
        <div className = "Purchase-Table-Header">Industry Name</div>
        <div className = "Purchase-Table-Header">Allowance</div>
        <div className = "Purchase-Table-Header">Credits</div>
        <div className = "Purchase-Table-Header">Quantity Converted</div>
        <div className = "Purchase-Table-Header">Purchase Options</div>
        </div>
        {
            DummyDetails.map(props=>{
                return(
                    <div className = "Purchase-Table">
                    <div className = "Purchase-Table-Body">{props.IndustryName}</div>
                    <div className = "Purchase-Table-Body">{props.IndustryID}</div>
                    <div className = "Purchase-Table-Body">{props.Allowance}</div>
                    <div className = "Purchase-Table-Body">{props.Credits}</div>
                    <div className = "Purchase-Table-Body">{props.Converted}</div>
                    </div>
                );
            })
        }
        </div>
    );
}

export default PrettyTable;