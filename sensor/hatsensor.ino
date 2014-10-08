#include <CapPin.h>
#include <unistd.h>
CapPin cPin_9  = CapPin(9);

void setup()
{
  Serial.begin(115200);
  Serial.println("start");
}

void loop() {
  long pinValue = cPin_9.readPin(2000);
  
  if (pinValue > 1000) {
    Serial.println("YEP");
  } else {
    Serial.println("NOPE");
  }
  delay(1000);

}
