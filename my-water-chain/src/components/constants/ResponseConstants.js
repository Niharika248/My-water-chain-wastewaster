const HeadersConstant = {
  Chart_01_Heading_01:"Flow Rate (milli-sq/pixels)",
  Chart_01_Heading_02:"Solid Waste Index",
  ColorHeading01:'rgba(234,156,234,0.6)',
  ColorHeading02:'rgba(255,0,0,0.6)',
  Heading01Text:'SWA and Flow Rate Index',


  Time_Labels:[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,19,20,21,22,23,24],
  Day_Lables:["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"],
  Water_Quality_Heading:"Water Quality Index",
  Water_Quantity_Heading:"Water Quantity Index",
  Color_For_Credits:['rgba(255,156,86,0.6)','rgba(250,100,100,0.6)','rgba(100,250,200,0.6)',
  'rgba(120,120,120,0.5)','rgba(120,240,120,0.5)','rgba(60,120,240,0.6)','rgba(200,120,120,0.5)','rgba(120,120,250,0.5)'],
  Color_For_Quality:['rgba(255,156,146,0.6)','rgba(250,100,100,0.6)','rgba(150,156,200,0.6)','rgba(180,250,200,0.6)'],
  QualityParamsHeading:"Quality Distribution of Different Parameters",
  CreditsParamHeading:"Monthly Credit Consumption",
  QualityWords:["Spectral","Conductivity","Solid-Waste","Histogram"],
  CreditWords:["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug"],
  LineChart01OptionText:'SWA and Flow Rate Index',
  Chart_02_Heading_01:"Quality Yesterday",
  Chart_02_Heading_02:"Quality in Last 3 Days",
  Chart_02_Heading_03:"Quality in Last 7 Days",
  Chart_02_Heading_04:"Quality in Last 30 Days",
  
  StableHeading: "Stable Quality",
  SelfHeading: "Self Quality"
};
export default HeadersConstant;

const ResponseConstant = {
    "Time_Labels":[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,19,20,21,22,23,24],
    "Day_Lables":["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"],
    "Water_Quality_Index": [1.5,2.5,3.5,1.2,2.3,3.4,2.2,3.2,1.2,3.5,5.4,2.6,2,1,1,4,2.2,2.6,3.4,4.5,4.6,4.8,2],
    "Water_Quantity_Index": [2200,2400,1200,1600,
                            2400,1200,1600,3400,
                            2200,2400,1200,2100,
                            1200,1600,3400,2200,
                            1200,1600,3400,5600,
                            3400,5600,1340,1500,],
    "Water_Quality_Index_Day":[1.24,1.35,1.68,1.23,1.35,2.45,6.43],
    "Water_Quantity_Index_Day":[120000,2400000,3200000,1245000,
                              2404000,4500000,3402000],
    "Quality_Analysis":{
                          "SPI":2.5,
                          "CDI":2.6,
                          "SWI":3.4,
                          "HSI":2.4
                      },
    "Previous_Comparision":{
                              "Yesterday_Quality":[
                                2.5,4.32,2.44,5.44,2.42,
                                3.5,5.2,1.44,6.24,5.41,
                                1.44,6.24,5.41,2.32,1.88,
                                3.5,5.2,1.44,6.24,5.41,
                                4.44,6,6.28,5.88
                              ],
                              "Yesterday_Quantity":[
                                2200,2400,1200,2100,
                                1200,1600,3400,2200,
                                1200,1600,3400,5600,
                                1600,3400,2200,2400,
                                2200,1600,3400,2200,
                                1200,3400,4500,2400
                              ],
                              "Last3Day_Quality":[
                                1.44,6.24,5.41,2.32,1.88,
                                3.5,5.2,1.44,6.24,5.41,
                                4.44,6,6.28,5.88,1.44,6.24,
                                2.5,4.32,2.44,5.44,2.42,
                                3.5,5.2,1.44,6.24,5.41,
                                2.45,1.48,2.66,3.42
                              ],
                              "Last3Day_Quantity":[
                                2200,4400,1200,2100,
                                3200,5600,3400,2200,
                                1500,1600,3400,5600,
                                1200,3400,2200,2400,
                                2200,1600,3400,2200,
                                3400,3400,2500,2900
                              ],
                              "Last7Day_Quality":[
                                1.44,4.24,5.41,2.32,1.88,
                                3.5,6.2,1.44,6.24,5.41,
                                1.24,6,6.28,2.88,5.44,6.24,
                                2.5,4.32,3.44,3.44,2.42,
                                4.5,5.4,3.44,6.24,5.41,
                                2.45,4.48,3.66,3.42
                              ],
                              "Last7Day_Quantity":[
                                2200,4400,1200,3100,
                                3200,2600,3400,2200,
                                1500,2200,1400,5600,
                                1200,3900,2200,1400,
                                2200,1600,3400,3200,
                                3400,3400,2600,5900
                              ],
                              "Monthly_Quality":[
                                2.44,4.24,5.41,3.32,1.88,
                                1.8,2.2,3.44,6.24,5.41,
                                1.24,6,4.28,2.88,3.44,6.24,
                                2.5,1.32,5.44,3.44,2.42,
                                5.5,5.4,2.44,5.24,5.41,
                                2.45,2.48,2.66,2.42
                              ],
                              "Monthly_Quantity":[
                                2200,4800,1200,3100,
                                1200,2700,3400,2200,
                                2500,2500,3400,5600,
                                4200,3400,3200,1400,
                                6200,1600,3400,3200,
                                1400,3400,6600,5900
                              ],
  
                          },
    "Stable_Comparision":{
                            "Stable_Quality":[2.5,2.8,3.2,2.8,2.5,3.2,3.2],
                            "Stable_Quantity":[1200,1400,1800,2400,3200,2800,2500],
                            "Self_Quality":[3.5,2.4,3.6,2.1,2.8,3.9,3.4],
                            "Self_Quantity":[1600,1700,1300,2200,3800,2200,2800],
                        },
    "Credit_Consumption_History":[2,3,2,3,5,4,2,2],
    "Industry_Name":[],
    "Industry_ID":[],
    "Industry_Allowance":[],
    "Industry_Credits":[],
    "Self_Data":{
                  "Self_Credits":2,
                  "Self_Consumption":1200,
                  "Self_Allowance":0,
                  "Expiry_Date":"12-March-2020",
                }
  };
  