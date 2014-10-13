#include <CapPin.h>
#include <unistd.h>
CapPin cPin_9  = CapPin(9);

void setup()
{
  Serial.begin(115200);
  Serial.println("start");
}

void loop() {
  Serial.println(cPin_9.readPin(2000));
}
