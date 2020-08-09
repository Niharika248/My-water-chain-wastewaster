const int sensorPin = A0;
const int BuzzerTrigger = 7;
const int threshold = 120;
const int conductivityThreshold = 130;
int lightCal;
int lightVal;
void setup()
{
  lightCal = analogRead(sensorPin);
  pinMode(BuzzerTrigger, OUTPUT);
  pinMode(A1,INPUT);
  pinMode(A0,INPUT);
  digitalWrite(BuzzerTrigger,LOW);
  Serial.begin(9600);
}

void loop()
{
  lightVal = analogRead(sensorPin);
  //Serial.print("Value is :  ");
  if(analogRead(A1)>conductivityThreshold)//||lightVal>threshold-18)// || )
    digitalWrite(BuzzerTrigger,HIGH);
  else
    digitalWrite(BuzzerTrigger,LOW);
  //Serial.println(lightVal);
  Serial.print("Resistor value: ");
  Serial.print(analogRead(A1));
  Serial.print(" And Spectral reading is: ");
  Serial.println(lightVal);
}
