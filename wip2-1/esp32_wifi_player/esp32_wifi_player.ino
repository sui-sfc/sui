#include <WiFi.h>
#include <WiFiUdp.h>
#include "I2S.h"

const char ssid[] = "ESP32_wifi"; // SSID
const char pass[] = "esp32pass";  // password
const int localPort = 10000;      // ポート番号

const IPAddress ip(192, 168, 4, 1);       // IPアドレス(ゲートウェイも兼ねる)
const IPAddress subnet(255, 255, 255, 0); // サブネットマスク

WiFiUDP udp;
char packetBuffer[40000];

void setup() {
  
  Serial.begin(115200);

  WiFi.softAP(ssid, pass);           // SSIDとパスの設定
  delay(100);                       
  WiFi.softAPConfig(ip, ip, subnet); // IPアドレス、ゲートウェイ、サブネットマスクの設定

  Serial.print("AP IP address: ");
  IPAddress myIP = WiFi.softAPIP();
  Serial.println(myIP);

  Serial.println("Starting UDP");
  udp.begin(localPort); 

  Serial.print("Local port: ");
  Serial.println(localPort);
  I2S_Init();
}

void loop() {
 
  int packetSize = udp.parsePacket();
 
  if (packetSize) {
 
    int len = udp.read(packetBuffer, packetSize);
    //終端文字設定
    if (len > 0) packetBuffer[len] = '\0';
 
    Serial.print(udp.remoteIP());
    Serial.print(" / ");
    Serial.println(packetSize); 
    I2S_Write(packetBuffer,packetSize);  // I2S
  }
}
