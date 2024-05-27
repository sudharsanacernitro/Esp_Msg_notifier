#include <ESP8266WiFi.h>
#include <ESP8266WebServer.h>
#include <LiquidCrystal.h>

// Set up the LCD object with the pin configuration
LiquidCrystal lcd(D6, D5, D1, D2, D3, D4);

const char* ssid = "a";
const char* password = "1234567890";

ESP8266WebServer server(80);
String message="";

void handleRoot() {
  if (server.hasArg("message")) {
     message = server.arg("message");
    Serial.println("Received message: " + message);
    
    server.send(200, "text/plain", "Message received");
  } else {
    server.send(400, "text/plain", "No message received");
  }
}

void setup() {
  Serial.begin(115200);
  WiFi.begin(ssid, password);
  lcd.begin(16, 2);                 // Initialize 16x2 LCD Display

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  Serial.println("");
  Serial.print("Connected to ");
  Serial.println(ssid);
  Serial.print("IP address: ");
  Serial.println(WiFi.localIP());

  server.on("/", handleRoot);
  server.begin();
  Serial.println("HTTP server started");
}

void loop() {
  server.handleClient();

  if(message!="")
  {
    lcd.clear();
  lcd.setCursor(0, 0); // Position cursor at the start of the first line
    lcd.print("--"+message);
    for (int i = 0; i < message.length()+2; i++) {
    lcd.scrollDisplayLeft();
    delay(500);
  }
  }
}
