#include <MobaTools.h>
int SPU = 2048;

MoToStepper stepperX(SPU);
MoToStepper stepperY(SPU);

String input;
String oldInput;

void setup()
{
  stepperX.attach( 3, 5, 4, 6);
  stepperY.attach( 9, 10, 11, 8);
  stepperX.setSpeed(5);
  Serial.begin(9600);
}
void loop()
{
  //while (!Serial.available());
  //input = Serial.readString();

  //Serial.print(input);

  stepperX.doSteps(5);
}
