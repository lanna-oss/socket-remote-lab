#include<WiFi.h>

#define WIFI_AP_NAME "ESP32Light"
#define WIFI_AP_PASS NULL

#define RedPin  12
#define GreenPin  14
#define YellowPin  27
#define BluePin  26

WiFiServer LightServer(1234);

void setup() {

  Serial.begin(9600);
  pinMode(LED_BUILTIN, OUTPUT);
  pinMode(RedPin, OUTPUT);
  pinMode(GreenPin, OUTPUT);
  pinMode(YellowPin, OUTPUT);
  pinMode(BluePin, OUTPUT);
  Serial.print("WIFI Soft AP : ");
  Serial.println(WIFI_AP_NAME);

  WiFi.softAP(WIFI_AP_NAME,WIFI_AP_PASS);

  Serial.print("ESP32 IP address: ");
  Serial.println(WiFi.softAPIP());


  LightServer.begin();
}

void loop() {

  WiFiClient client = LightServer.available();
  if (client) {
    char Python_msg[255] = "";
    while (client.connected()) {
      Serial.println("Remoter connected.");
      while(client.available()> 0) {
        char c = client.read();
        strncat(Python_msg, &c,1);
      }
      Serial.print("Python Message: ");
      Serial.println(Python_msg);

      if(strcmp(Python_msg,"red on")==0){
         digitalWrite(RedPin, HIGH);
         client.write("Red on");
      } else 
      if(strcmp(Python_msg,"red off")==0){
         digitalWrite(RedPin, LOW);
         client.write("Red off");
      } else
      if(strcmp(Python_msg,"red status")==0){
         if (digitalRead(RedPin) == 0) {client.write("OFF");} else
         if (digitalRead(RedPin) == 1) {client.write("ON");}         
      } else
      if(strcmp(Python_msg,"green on")==0){
         digitalWrite(GreenPin, HIGH);
         client.write("Green on");
      } else 
      if(strcmp(Python_msg,"green off")==0){
         digitalWrite(GreenPin, LOW);
         client.write("Green off");
      } else
      if(strcmp(Python_msg,"green status")==0){
         if (digitalRead(GreenPin) == 0) {client.write("OFF");} else
         if (digitalRead(GreenPin) == 1) {client.write("ON");}         
      } else    
      if(strcmp(Python_msg,"yellow on")==0){
         digitalWrite(YellowPin, HIGH);
         client.write("Yellow on");
       } else 
       if(strcmp(Python_msg,"yellow off")==0){
         digitalWrite(YellowPin, LOW);
         client.write("Yellow off");
       } else
       if(strcmp(Python_msg,"yellow status")==0){
         if (digitalRead(YellowPin) == 0) {client.write("OFF");} else
         if (digitalRead(YellowPin) == 1) {client.write("ON");}         
       } else 
       if(strcmp(Python_msg,"blue on")==0){
         digitalWrite(BluePin, HIGH);
         client.write("Blue on");
       } else 
       if(strcmp(Python_msg,"blue off")==0){
         digitalWrite(BluePin, LOW);
         client.write("Blue off");      
       } else
       if(strcmp(Python_msg,"blue status")==0){
         if (digitalRead(BluePin) == 0) {client.write("OFF");} else
         if (digitalRead(BluePin) == 1) {client.write("ON");}         
       }
          
    client.stop();
    Serial.println("Disonnected");
    }
   delay(10);
  }
}