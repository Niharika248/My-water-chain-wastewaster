import React from "react";

export default function Footer()
{
    const Element1 = "GZB Automation";
    const today = new Date();
    const DayFormat = today.toString().split(" ").slice(0,4);
    const Element3 = DayFormat.filter(Boolean).join(" ");
    const Element2 = "Copyright © "+today.getFullYear().toString()+". All rights reserved.";
    return(
        <div className="FooterAligner">
        <div className="FooterElement Footer01">{Element1}</div>
        <div className="FooterElement">{Element2}</div>
        <div className="FooterElement Footer03">{Element3}</div>
        </div>
    );
}