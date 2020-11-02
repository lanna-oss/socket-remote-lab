#define RedPin  12
#define GreenPin  14
#define YellowPin  27
#define BluePin  26
#define delayTime 1000

void MeanOfStatus(int Pinnum){
  if(digitalRead(Pinnum) == 0){
    Serial.println(" (Inactivate)");
  }
  if(digitalRead(Pinnum) == 1){
    Serial.println(" (Active)");
  }
}


void setup() {
  Serial.begin(9600);
  Serial.println("Test LED.");
  pinMode(RedPin, OUTPUT); 
  pinMode(GreenPin, OUTPUT);
  pinMode(YellowPin, OUTPUT);
  pinMode(BluePin, OUTPUT);
}

void loop() {
  digitalWrite(RedPin, HIGH); // sets active for Red pin.
  Serial.print("Red Pin status = ");
  Serial.print(digitalRead(RedPin));
  MeanOfStatus(RedPin);
  delay(delayTime);            // waits for a second

  digitalWrite(RedPin, LOW);  // sets inactive for Red pin.
  Serial.print("Red Pin status = ");
  Serial.print(digitalRead(RedPin));
  MeanOfStatus(RedPin);
  delay(delayTime);

  digitalWrite(GreenPin, HIGH); // sets active for Red pin.
  Serial.print("Green Pin status = ");
  Serial.print(digitalRead(GreenPin));
  MeanOfStatus(GreenPin);
  delay(delayTime);            // waits for a second

  digitalWrite(GreenPin, LOW);  // sets inactive for Red pin.
  Serial.print("Green Pin status = ");
  Serial.print(digitalRead(GreenPin));
  MeanOfStatus(GreenPin);
  delay(delayTime);

  digitalWrite(YellowPin, HIGH); // sets active for Red pin.
  Serial.print("Yellow Pin status = ");
  Serial.print(digitalRead(YellowPin));
  MeanOfStatus(YellowPin);
  delay(delayTime);            // waits for a second

  digitalWrite(YellowPin, LOW);  // sets inactive for Red pin.
  Serial.print("Yellow Pin status = ");
  Serial.print(digitalRead(YellowPin));
  MeanOfStatus(YellowPin);
  delay(delayTime);

  digitalWrite(BluePin, HIGH); // sets active for Red pin.
  Serial.print("Blue Pin status = ");
  Serial.print(digitalRead(BluePin));
  MeanOfStatus(BluePin);
  delay(delayTime);            // waits for a second

  digitalWrite(BluePin, LOW);  // sets inactive for Red pin.
  Serial.print("Blue Pin status = ");
  Serial.print(digitalRead(BluePin));
  MeanOfStatus(BluePin);
  delay(delayTime);
}
