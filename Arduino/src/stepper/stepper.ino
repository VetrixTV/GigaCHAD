#include <Stepper.h>
int SPU = 2048;
Stepper Motor(SPU, 3, 5, 4, 6);

int stepCount = 0;

void setup()
{
  Motor.setSpeed(5);
  Serial.begin(9600);
}
void loop()
{
 if(true){
  Motor.step(1);
 } else {
  Motor.step(-1);
 }
}
