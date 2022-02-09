#include <MobaTools.h>
int SPU = 2048;

MoToStepper stepperX(SPU, FULLSTEP);
MoToStepper stepperY(SPU, FULLSTEP);

String input;
String oldInput;

void setup()
{
  stepperX.attach( 3, 4, 5, 6);
  stepperY.attach( 7, 8, 9, 10);
  stepperX.setSpeed(150);
  stepperY.setSpeed(150);
  Serial.begin(9600);
}
void loop()
{
  while (!Serial.available());
  input = Serial.readString();
  Serial.print(input);
  if(input){
    oldInput = input;
  }
  while(input){
    if(Serial.available()){
      input = Serial.readString();
      Serial.print(input);
    }
    stepperX.doSteps(1);
    stepperY.doSteps(1);
  }
}