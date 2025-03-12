#include <Arduino.h>
#include <Adafruit_SPIDevice.h>
Adafruit_SPIDevice ADS1299 = Adafruit_SPIDevice(5);
// put function declarations here:
void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  Serial.printf("Starting Serial \n");
  if (!ADS1299.begin()) {
    Serial.println("Could not initialize SPI device");
    while (1);
  }
}

void loop() {
  // put your main code here, to run repeatedly:
  uint8_t buf[24];
  ADS1299.read(buf,24);
  Serial.printf("me hooopppppeeee: ");
  for(int i = 0; i < 24; i++){
    Serial.printf("%d, ",buf[i]);
  }
  Serial.printf("\n");
  delay(100);
}