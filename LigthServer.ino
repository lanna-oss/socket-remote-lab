#include<WiFi.h>

#define WIFI_AP_NAME "ESP32Light"
#define WIFI_AP_PASS NULL
#define WIFI_STA_NAME  "Test_Wifi" 
#define WIFI_STA_PASS  "2Many42Secret"
#define USE_STA_Mode  1
#define USE_AP_Mode  2


#define RedPin  12
#define GreenPin  14
#define YellowPin  27
#define BluePin  26

WiFiServer LightServer(1234);

void setup() {
  
  int Wifi_mode = USE_STA_Mode;
  /*
   *  You can change the wifi system by setting a parameter in Wifi_mode variable.    *
   *  USE_STA_Mode = STA Mode.
   *  USE_AP_Mode = AP mode.
   *  
   */
  Serial.begin(9600);
  pinMode(LED_BUILTIN, OUTPUT);
  pinMode(RedPin, OUTPUT);
  pinMode(GreenPin, OUTPUT);
  pinMode(YellowPin, OUTPUT);
  pinMode(BluePin, OUTPUT);
  if(Wifi_mode == USE_STA_Mode){
      Serial.print("WIFI STA Mode : ");
      Serial.println(WIFI_STA_NAME);
      WiFi.mode(WIFI_STA);
      WiFi.begin(WIFI_STA_NAME, WIFI_STA_PASS);

      while (WiFi.status() != WL_CONNECTED){
        delay(500);
        Serial.print("#");
        digitalWrite(LED_BUILTIN, !digitalRead(LED_BUILTIN));
      }
      Serial.println(" Loged in.");
      Serial.print("IP address: ");
      Serial.println(WiFi.localIP());
  } else
  {
    Serial.print("WIFI Soft AP : ");
    Serial.println(WIFI_AP_NAME);
    WiFi.softAP(WIFI_AP_NAME,WIFI_AP_PASS);
    Serial.print("ESP32 IP address: ");
    Serial.println(WiFi.softAPIP());
    Serial.println("The LightServer awaits remote command.");
  }

  LightServer.begin();
}

void loop() {

  WiFiClient client = LightServer.available();
  if (client) {
    char Remoter_msg[255] = "";
    while (client.connected()) {
      Serial.print("Remoter connected. ");
      while(client.available()> 0) {
        char c = client.read();
        strncat(Remoter_msg, &c,1);
      }
      if (Remoter_msg[0] == '\0'){ 
         Serial.print("Text is Empty.");
         }
      else {
      Serial.print("Text = \"");
      Serial.print(Remoter_msg);
      Serial.print("\". Send = \"");
      if(strcmp(Remoter_msg,"red on")==0){
         digitalWrite(RedPin, HIGH);
         client.write("Red on");
         Serial.print("Red on");
      } else 
      if(strcmp(Remoter_msg,"red off")==0){
         digitalWrite(RedPin, LOW);
         client.write("Red off");
         Serial.print("Red off");
      } else
      if(strcmp(Remoter_msg,"red status")==0){
         if (digitalRead(RedPin) == 0) {client.write("OFF"); Serial.print("OFF");} else
         if (digitalRead(RedPin) == 1) {client.write("ON");  Serial.print("ON"); }         
      } else
      if(strcmp(Remoter_msg,"green on")==0){
         digitalWrite(GreenPin, HIGH);
         client.write("Green on");
         Serial.print("Green on");
      } else 
      if(strcmp(Remoter_msg,"green off")==0){
         digitalWrite(GreenPin, LOW);
         client.write("Green off");
         Serial.print("Green off");
      } else
      if(strcmp(Remoter_msg,"green status")==0){
         if (digitalRead(GreenPin) == 0) {client.write("OFF"); Serial.print("OFF"); } else
         if (digitalRead(GreenPin) == 1) {client.write("ON");  Serial.print("ON"); }         
      } else    
      if(strcmp(Remoter_msg,"yellow on")==0){
         digitalWrite(YellowPin, HIGH);
         client.write("Yellow on");
         Serial.print("Yellow on");
       } else 
       if(strcmp(Remoter_msg,"yellow off")==0){
         digitalWrite(YellowPin, LOW);
         client.write("Yellow off");
         Serial.print("Yellow off");
       } else
       if(strcmp(Remoter_msg,"yellow status")==0){
         if (digitalRead(YellowPin) == 0) {client.write("OFF"); Serial.print("OFF"); } else
         if (digitalRead(YellowPin) == 1) {client.write("ON");  Serial.print("ON"); }         
       } else 
       if(strcmp(Remoter_msg,"blue on")==0){
         digitalWrite(BluePin, HIGH);
         client.write("Blue on");
         Serial.print("Blue on");
       } else 
       if(strcmp(Remoter_msg,"blue off")==0){
         digitalWrite(BluePin, LOW);
         client.write("Blue off");
         Serial.print("Blue off");
       } else
       if(strcmp(Remoter_msg,"blue status")==0){
         if (digitalRead(BluePin) == 0) {client.write("OFF"); Serial.print("OFF");} else
         if (digitalRead(BluePin) == 1) {client.write("ON");  Serial.print("ON"); }         
       } else 
         { 
         client.write("Not command");
         Serial.print("Not command");
         }
         Serial.print("\"");  
      }
          
    client.stop();
    Serial.println(" Disonnected.");
    }
  }
}
