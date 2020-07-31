import React from "react";
export default function Header(props)
{
    return(
        <div>
        <h1 className = "HeadingForm">{props.header}</h1>
        </div>
    );
}