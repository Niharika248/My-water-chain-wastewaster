import React from "react";

export default function Authentication(props)
{
    return <button className = "UI-Button" onClick={props.onClickaction}>{props.text}</button>;
}