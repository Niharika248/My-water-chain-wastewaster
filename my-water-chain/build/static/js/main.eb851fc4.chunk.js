(this["webpackJsonpmy-water-chain"]=this["webpackJsonpmy-water-chain"]||[]).push([[0],{176:function(e,a,t){},177:function(e,a,t){"use strict";t.r(a);var r=t(0),n=t.n(r),l=t(65),o=t.n(l);t(76);function i(e){return n.a.createElement("div",null,n.a.createElement("h1",{className:"HeadingForm"},e.header))}function s(e){return n.a.createElement("button",{className:"UI-Button",onClick:e.onClickaction},e.text)}function c(){var e=new Date,a=e.toString().split(" ").slice(0,4).filter(Boolean).join(" "),t="Copyright \xa9 "+e.getFullYear().toString()+". All rights reserved.";return n.a.createElement("div",{className:"FooterAligner"},n.a.createElement("div",{className:"FooterElement Footer01"},"GZB Automation"),n.a.createElement("div",{className:"FooterElement"},t),n.a.createElement("div",{className:"FooterElement Footer03"},a))}var d=t(6);var u=Object(d.h)((function(e){return n.a.createElement("div",null,n.a.createElement(i,{header:"My Water Chain"}),n.a.createElement("div",{className:"WhiteCard"},n.a.createElement("div",{className:"whiteSpace"}),n.a.createElement(s,{text:"Login",onClickaction:function(){e.history.push("/login")}}),n.a.createElement(s,{text:"Register",onClickaction:function(){e.history.push("/register")}})),n.a.createElement(c,null))})),m=t(9),b=t.n(m),p=t(18),g=t(14),y=t(8),h=t(10),f=t(7),E=t(11),C=["","Field Cannot be Empty.","Maximum Character Exceed!","Spaces are not allowed.","Wrong Email Syntax!","Invalid ID","Passwords Don't Match!"],v=[{id:0,controlId:"formBasicEmail",Label:"Email",type:"email",placeholder:"Enter Registered Email"},{id:1,controlId:"formBasicPassword",Label:"Password",type:"password",placeholder:"Enter Password"}],_=t(21),P=t(67),N=t(68),w=new(function(){function e(){Object(P.a)(this,e),this.authenticated=!1}return Object(N.a)(e,[{key:"login",value:function(e){this.authenticated=!0,this.jsonData=e}},{key:"logout",value:function(){this.authenticated=!1}},{key:"isAuthenticated",value:function(){return this}}]),e}()),O=["Industry Name","Industry-ID","Allowance","Credits"],S=["Water Drops","Current Allowance","Expiry Date"],I="http://18.207.1.144/";function j(e){var a=Object(r.useState)({email:"",password:""}),t=Object(h.a)(a,2),l=t[0],o=t[1],i=Object(r.useState)(!1),s=Object(h.a)(i,2),d=s[0],u=s[1],m=Object(r.useState)({email:"",password:""}),P=Object(h.a)(m,2),N=P[0],O=P[1];return n.a.createElement("div",null,n.a.createElement(f.a,{className:"FormAligner"},v.map((function(e){return n.a.createElement(f.a.Group,{key:e.id,autoComplete:"off",controlId:e.controlId},n.a.createElement(f.a.Label,null,e.Label),n.a.createElement(f.a.Control,{type:e.type,placeholder:e.placeholder,value:l[e.type],onChange:function(a){o(Object(y.a)(Object(y.a)({},l),{},Object(g.a)({},e.type,a.target.value))),/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/.test(l.email)?O(Object(y.a)(Object(y.a)({},N),{},Object(g.a)({},"email",C[0]))):O(Object(y.a)(Object(y.a)({},N),{},Object(g.a)({},"email",C[4])))}}),n.a.createElement(f.a.Text,{className:"text-muted"},N[e.type]))})),d?n.a.createElement("div",{className:"UI-Aligner"},n.a.createElement(E.a,{className:"UI-Button-Click",variant:"primary",disabled:!0},n.a.createElement(_.a,{as:"span",animation:"border",size:"sm",role:"status","aria-hidden":"true"}),n.a.createElement("span",{className:"sr-only"},"Loading..."))):n.a.createElement("div",{className:"UI-Aligner"},n.a.createElement(E.a,{className:"UI-Button-Click",onClick:function(){var a=Object(p.a)(b.a.mark((function a(t){var r;return b.a.wrap((function(a){for(;;)switch(a.prev=a.next){case 0:return t.preventDefault(),u(!0),r=l,a.next=5,fetch("".concat(I,"login"),{method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify(r)}).then((function(e){return e.json()})).then(function(){var a=Object(p.a)(b.a.mark((function a(t){return b.a.wrap((function(a){for(;;)switch(a.prev=a.next){case 0:if(!t.Is_Valid){a.next=6;break}return a.next=3,fetch("".concat(I,"fetching"),{method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify(r)}).then((function(e){return e.json()})).then((function(a){u(!1),w.login(a),e.history.push("/login-props-test")}));case 3:a.sent,a.next=8;break;case 6:u(!1),alert("Invalid Credentials! Error Message: "+t.Error_Message);case 8:case"end":return a.stop()}}),a)})));return function(e){return a.apply(this,arguments)}}());case 5:a.sent;case 6:case"end":return a.stop()}}),a)})));return function(e){return a.apply(this,arguments)}}()},"Login"))),n.a.createElement(c,null))}var x=[{id:0,formcontrolIdType:"formBasicText-0",fieldLabel:"Registration-ID",fieldType:"text",fieldPlaceHolder:"Enter the 12 digit Registration ID",fieldDetails:"Device_ID"},{id:1,formcontrolIdType:"formBasicText-1",fieldLabel:"Registerar Username",fieldType:"text",fieldPlaceHolder:"Enter your Username.",fieldDetails:"Registerar_UserName"},{id:2,formcontrolIdType:"formBasicEmail-0",fieldLabel:"Registerar Email ID",fieldType:"email",fieldPlaceHolder:"Enter your Email-ID.",fieldDetails:"Registerar_Email"},{id:3,formcontrolIdType:"formBasicText-2",fieldLabel:"Organisation Name",fieldType:"text",fieldPlaceHolder:"Enter your Water Provider.",fieldDetails:"Organisation_Name"},{id:4,formcontrolIdType:"formBasicEmail-1",fieldLabel:"Organisation Email",fieldType:"email",fieldPlaceHolder:"Enter Water Provider ID.",fieldDetails:"Organisation_Email"},{id:5,formcontrolIdType:"formBasicPassword-0",fieldLabel:"Password",fieldType:"password",fieldPlaceHolder:"Enter Password.",fieldDetails:"Password"},{id:6,formcontrolIdType:"formBasicPassword-1",fieldLabel:"Re-enter Password",fieldType:"password",fieldPlaceHolder:"Re-enter Password.",fieldDetails:"Reenter_Password"}];function D(){var e=Object(r.useState)({Device_ID:"",Registerar_UserName:"",Registerar_Email:"",Organisation_Name:"",Organisation_Email:"",Password:"",Reenter_Password:""}),a=Object(h.a)(e,2),t=a[0],l=a[1],o=Object(r.useState)(!1),i=Object(h.a)(o,2),s=i[0],d=i[1];return n.a.createElement("div",null,n.a.createElement(f.a,{className:"FormAligner"},x.map((function(e){return n.a.createElement(f.a.Group,{key:e.id,autocomplete:"off",controlId:e.formcontrolIdType},n.a.createElement(f.a.Label,null,e.fieldLabel),n.a.createElement(f.a.Control,{type:e.fieldType,placeholder:e.fieldPlaceHolder,value:t[e.fieldDetails],onChange:function(a){l(Object(y.a)(Object(y.a)({},t),{},Object(g.a)({},e.fieldDetails,a.target.value)))}}))})),s?n.a.createElement("div",{className:"UI-Aligner"},n.a.createElement(E.a,{className:"UI-Button-Click",variant:"primary",disabled:!0},n.a.createElement(_.a,{as:"span",animation:"border",size:"sm",role:"status","aria-hidden":"true"}),n.a.createElement("span",{className:"sr-only"},"Loading..."))):n.a.createElement("div",{className:"UI-Aligner"},n.a.createElement(E.a,{className:"UI-Button-Click",onClick:function(){var e=Object(p.a)(b.a.mark((function e(a){var r;return b.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return a.preventDefault(),d(!0),r=t,e.next=5,fetch("".concat(I,"register"),{method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify(r)}).then((function(e){return e.json()})).then((function(e){d(!1),alert(e.Error_Message)}));case 5:e.sent;case 6:case"end":return e.stop()}}),e)})));return function(a){return e.apply(this,arguments)}}()},"Submit"))),n.a.createElement(c,null))}var k=t(19),H={Chart_01_Heading_01:"Flow Rate (milli-sq/pixels)",Chart_01_Heading_02:"Solid Waste Index",ColorHeading01:"rgba(234,156,234,0.6)",ColorHeading02:"rgba(255,0,0,0.6)",Heading01Text:"SWA and Flow Rate Index",Time_Labels:[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,19,20,21,22,23,24],Day_Lables:["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"],Water_Quality_Heading:"Water Quality Index",Water_Quantity_Heading:"Water Quantity Index",Color_For_Credits:["rgba(255,156,86,0.6)","rgba(250,100,100,0.6)","rgba(100,250,200,0.6)","rgba(120,120,120,0.5)","rgba(120,240,120,0.5)","rgba(60,120,240,0.6)","rgba(200,120,120,0.5)","rgba(120,120,250,0.5)"],Color_For_Quality:["rgba(255,156,146,0.6)","rgba(250,100,100,0.6)","rgba(150,156,200,0.6)","rgba(180,250,200,0.6)"],QualityParamsHeading:"Quality Distribution of Different Parameters",CreditsParamHeading:"Monthly Credit Consumption",QualityWords:["Spectral","Conductivity","Solid-Waste","Histogram"],CreditWords:["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug"],LineChart01OptionText:"SWA and Flow Rate Index",Chart_02_Heading_01:"Quality Yesterday",Chart_02_Heading_02:"Quality in Last 3 Days",Chart_02_Heading_03:"Quality in Last 7 Days",Chart_02_Heading_04:"Quality in Last 30 Days",StableHeading:"Stable Quality",SelfHeading:"Self Quality"};var T=function(e){var a=["rgba(0,0,255,0.5)"],t=["rgba(240,160,255,0.4)"],r={labels:H.Time_Labels,datasets:[{label:H.Chart_01_Heading_01,data:e.Plot1,borderColor:a,backgroundColor:a,pointBackgroundColor:a,pointBorderColor:a},{label:H.Chart_01_Heading_02,data:e.Plot2,borderColor:t,backgroundColor:t,pointBackgroundColor:t,pointBorderColor:t}]};return n.a.createElement(k.c,{className:"Chart-Line-Chart",data:r,options:{title:{display:!0,text:"SWA and Flow Rate Index"},scales:{yAxes:[{ticks:{min:0,max:10,stepSize:1}}]}}})};var L=function(e){var a=["rgba(0, 182, 255, 0.8)"],t=["rgba(1, 255, 255, 0.8)"],r=["rgba(0, 206, 255, 0.8)"],l=["rgba(200, 227, 248, 0.8)"],o={labels:H.Time_Labels,datasets:[{label:H.Chart_02_Heading_01,data:e.Plot1,borderColor:a,backgroundColor:a,pointBackgroundColor:a,pointBorderColor:a},{label:H.Chart_02_Heading_02,data:e.Plot2,borderColor:t,backgroundColor:t,pointBackgroundColor:t,pointBorderColor:t},{label:H.Chart_02_Heading_03,data:e.Plot3,borderColor:r,backgroundColor:r,pointBackgroundColor:r,pointBorderColor:r},{label:H.Chart_02_Heading_04,data:e.Plot4,borderColor:l,backgroundColor:l,pointBackgroundColor:l,pointBorderColor:l}]};return n.a.createElement(k.c,{className:"Chart-Line-Chart",data:o,options:{title:{display:!0,text:"Quality Analysis Month to Date"},scales:{yAxes:[{ticks:{min:0,max:10,stepSize:1}}]}}})},B={Heading:"Welcome to Your Dashboard",WaterCoins:"WaterDrops",Allowance:"Allowance",ExpireText:"Expires on ",LogoName:"logo.png"};function W(){return n.a.createElement("div",{className:"FullSizeContainer"},n.a.createElement("div",{className:"Section-02-Header"},B.Heading),n.a.createElement("div",{className:"Section-03-Header"},n.a.createElement("img",{src:"/my-water-chain"+B.LogoName,className:"Customize-Logo",alt:"Loading..."})))}var A=function(e){var a=["rgba(255,156,86,0.6)","rgba(255,156,86,0.6)","rgba(255,156,86,0.6)","rgba(255,156,86,0.6)","rgba(255,156,86,0.6)","rgba(255,156,86,0.6)","rgba(255,156,86,0.6)"],t=["rgba(85,236,86,0.2)","rgba(85,236,86,0.2)","rgba(85,236,86,0.2)","rgba(85,236,86,0.2)","rgba(85,236,86,0.2)","rgba(85,236,86,0.2)","rgba(85,236,86,0.2)"],r={labels:H.Day_Lables,datasets:[{label:e.HH1,data:e.Plot1,borderColor:a,backgroundColor:a},{label:e.HH2,data:e.Plot2,borderColor:t,backgroundColor:t}]};return n.a.createElement(k.a,{className:"Chart-Line-Chart",data:r,options:{title:{display:!0,text:"Day Wise Quality/Quantity Performance"},scales:{yAxes:[{ticks:{min:0,max:10,stepSize:1}}]}}})};var Q=function(e){var a=["rgba(255,156,86,0.6)","rgba(250,100,100,0.6)","rgba(100,250,200,0.6)","rgba(120,120,120,0.5)","rgba(120,240,120,0.5)","rgba(60,120,240,0.6)","rgba(200,120,120,0.5)","rgba(120,120,250,0.5)"],t={labels:e.Words,datasets:[{label:e.Label,data:e.Data,borderColor:a,backgroundColor:a}]},r={title:{display:!0,text:e.Texts}};return n.a.createElement(k.b,{className:"Chart-Line-Chart",data:t,options:r})};var R=function(e){var a=Object(d.g)(),t=e.Data,l=e.selfData,o=Object(r.useState)(!1),i=Object(h.a)(o,2),s=i[0],c=i[1],u=Object(r.useState)(!1),m=Object(h.a)(u,2),C=m[0],v=m[1],P=Object(r.useState)({_id:null,Credits:null,Password:null}),N=Object(h.a)(P,2),j=N[0],x=N[1];return n.a.createElement("div",null,n.a.createElement("h3",{className:"My-Table-Details-01"},"Industrial Performance"),n.a.createElement("table",{className:"Pretty-Table"},O.map((function(e){return n.a.createElement("th",{className:"Pretty-Table-Header"},e)})),t.map((function(e){return n.a.createElement("tr",{className:"Pretty-Table-Row"},n.a.createElement("td",{className:"Pretty-Table-Body"},e.Registerar_UserName),n.a.createElement("td",{className:"Pretty-Table-Body"},e._id),n.a.createElement("td",{className:"Pretty-Table-Body"},e.Allowance),n.a.createElement("td",{className:"Pretty-Table-Body"},e.Credits))}))),n.a.createElement("h3",{className:"My-Table-Details"},"My Details"),n.a.createElement("table",{className:"Pretty-Table"},S.map((function(e){return n.a.createElement("th",{className:"My-Pretty-Table-Header"},e)})),n.a.createElement("tr",{className:"Pretty-Table-Row"},l.map((function(e){return n.a.createElement("td",{className:"Pretty-Table-Body"},e)})))),n.a.createElement("div",{className:"Purchase-Reuqester"},n.a.createElement("div",null,n.a.createElement(f.a.Group,{className:"Purchase-Reuester-Column",key:1,autoComplete:"off",controlId:"PurchaseEntry"},n.a.createElement(f.a.Label,null,"Industry-ID"),n.a.createElement(f.a.Control,{type:"text",placeholder:"Enter Industry-ID",value:j._id,onChange:function(e){x(Object(y.a)(Object(y.a)({},j),{},Object(g.a)({},"_id",e.target.value)))}})),n.a.createElement(f.a.Group,{className:"Purchase-Reuester-Column",key:2,autoComplete:"off",controlId:"PurchaseCredit"},n.a.createElement(f.a.Label,null,"Water Drops"),n.a.createElement(f.a.Control,{type:"text",placeholder:"Enter Water Drops",value:j.Credits,onChange:function(e){x(Object(y.a)(Object(y.a)({},j),{},Object(g.a)({},"Credits",e.target.value)))}})),s?n.a.createElement("div",null,n.a.createElement("div",{className:"Purchase-Reuqester"},n.a.createElement(f.a.Group,{className:"Purchase-Reuester-Column",key:3,autoComplete:"off",controlId:"Password"},n.a.createElement(f.a.Label,null,"Password"),n.a.createElement(f.a.Control,{type:"password",placeholder:"Confirm Password",value:j.Password,onChange:function(e){x(Object(y.a)(Object(y.a)({},j),{},Object(g.a)({},"Password",e.target.value)))}}))),C?n.a.createElement("div",null,n.a.createElement(E.a,{className:"Purchase-Reuqester",variant:"primary",disabled:!0},n.a.createElement(_.a,{as:"span",animation:"border",size:"sm",role:"status","aria-hidden":"true"}),n.a.createElement("span",{className:"sr-only"},"Loading..."))):n.a.createElement("div",{className:"UI-Aligner"},n.a.createElement(E.a,{className:"Purchase-Reuqester UI-Button-Click",onClick:function(){var t=Object(p.a)(b.a.mark((function t(r){var n,l,o;return b.a.wrap((function(t){for(;;)switch(t.prev=t.next){case 0:return r.preventDefault(),v(!0),n={email:e.Email,_id:j._id,Credits:j.Credits,password:j.Password},t.next=5,fetch("".concat(I,"make-a-transaction"),{method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify(n)});case 5:return l=t.sent,t.next=8,l.json();case 8:o=t.sent,v(!1),console.log(e),w.login(o),a.push("/login-props-test");case 13:case"end":return t.stop()}}),t)})));return function(e){return t.apply(this,arguments)}}()},"Purchase"))):n.a.createElement("div",{className:"Purchase-Reuqester UI-Aligner"},n.a.createElement(E.a,{className:"Purchase-Requester-Column UI-Button-Click",onClick:function(e){e.preventDefault(),c(!0)}},"Procceed")))))};function F(e){function a(e,a){for(var t=[],r=0;r<e.length;r++)t.push(e[r]/a);return t}var t=e.Block_Chain[e.Block_Chain.length-1].water_data,l=a(t.FlowRate,1e3),o=a(t.Water_Quantity_Index_Day,15e5),i=Object(r.useState)(!1),s=Object(h.a)(i,2),c=s[0],d=s[1],u=Object(r.useState)("Switch to Purchase Screen"),m=Object(h.a)(u,2),g=m[0],y=m[1];var f=function(){var a=Object(p.a)(b.a.mark((function a(){return b.a.wrap((function(a){for(;;)switch(a.prev=a.next){case 0:return a.next=2,fetch("".concat(I,"livepeer-streaming"),{method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify({email:e.email})}).then((function(e){return e.json()})).then((function(e){alert("Your stream generated url is ".concat(e.url,". Note that the url will automatically expire after 30 mins. You may renew it here. You can stream your session @ https://videojs.github.io/videojs-contrib-hls/"))}));case 2:a.sent;case 3:case"end":return a.stop()}}),a)})));return function(){return a.apply(this,arguments)}}();return n.a.createElement("div",{className:"Display-Screen-Global-Div"},n.a.createElement(W,null),n.a.createElement("div",{className:"UI-Aligner"},n.a.createElement(E.a,{className:"Switch-Button-In-Display UI-Button-Click",onClick:f},"Generate Stream Session"),n.a.createElement(E.a,{className:"Switch-Button-In-Display UI-Button-Click",onClick:function(){d((function(e){return!e})),y((function(e){return"Switch to Purchase Screen"===e?"Switch to Dashboard Screen":"Switch to Purchase Screen"}))}},g)),c?n.a.createElement("div",null,n.a.createElement(R,{Data:e.industry_response,selfData:e.self_details,Email:e.email})):n.a.createElement("div",null,n.a.createElement("div",{className:"Chart"},n.a.createElement("div",{className:"Chart-Candidate"},n.a.createElement(T,{Plot1:l,Plot2:t.Solid_Waste_Analysis_Index})),n.a.createElement("div",{className:"Chart-Candidate"}," ",n.a.createElement(A,{Plot1:t.Water_Quality_Index_Day,Plot2:o,HH1:H.Water_Quality_Heading,HH2:H.Water_Quantity_Heading})),n.a.createElement("div",{className:"Chart-Candidate"},n.a.createElement(Q,{ColorSchema:H.Color_For_Credits,Texts:"Quality Index",Data:[t.Quality_Analysis.SPI,t.Quality_Analysis.CDI,t.Quality_Analysis.SWI,t.Quality_Analysis.HSI],Label:H.QualityParamsHeading,Words:H.QualityWords,LabelTime:H.Time_Labels}))),n.a.createElement("div",{className:"Chart"},n.a.createElement("div",{className:"Chart-Candidate"},n.a.createElement(L,{Plot1:t.Previous_Comparision.Yesterday_Quality,Plot2:t.Previous_Comparision.Last3Day_Quality,Plot3:t.Previous_Comparision.Last7Day_Quality,Plot4:t.Previous_Comparision.Monthly_Quality})),n.a.createElement("div",{className:"Chart-Candidate"}," ",n.a.createElement(A,{Plot1:t.Stable_Comparision.Stable_Quality,Plot2:t.Stable_Comparision.Self_Quality,HH1:H.StableHeading,HH2:H.SelfHeading})),n.a.createElement("div",{className:"Chart-Candidate"},n.a.createElement(Q,{Data:t.Credit_Consumption_History,Label:H.CreditsParamHeading,Texts:"Credit Consumption",Words:H.CreditWords})))))}t(175);var U=t(70),M=function(e){var a=e.component,t=Object(U.a)(e,["component"]);return n.a.createElement(d.b,Object.assign({},t,{render:function(e){return w.isAuthenticated().authenticated?n.a.createElement(a,w.isAuthenticated().jsonData):n.a.createElement(d.a,{to:{pathname:"/login",state:{from:e.location}}})}}))},J=(t(176),t(26));var z=function(){return n.a.createElement("div",{className:"App"},n.a.createElement(J.a,null,n.a.createElement(d.d,null,n.a.createElement(d.b,{component:u,exact:!0,path:"/"}),n.a.createElement(d.b,{component:D,exact:!0,path:"/register"}),n.a.createElement(d.b,{component:j,exact:!0,path:"/login"}),n.a.createElement(M,{component:F,exact:!0,path:"/login-props-test"}))))};Boolean("localhost"===window.location.hostname||"[::1]"===window.location.hostname||window.location.hostname.match(/^127(?:\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){3}$/));o.a.render(n.a.createElement(n.a.StrictMode,null,n.a.createElement(z,null)),document.getElementById("root")),"serviceWorker"in navigator&&navigator.serviceWorker.ready.then((function(e){e.unregister()})).catch((function(e){console.error(e.message)}))},71:function(e,a,t){e.exports=t(177)},76:function(e,a,t){}},[[71,1,2]]]);
//# sourceMappingURL=main.eb851fc4.chunk.js.map