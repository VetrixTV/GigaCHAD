
#include <MobaTools.h>
int SPU = 2048;

MoToStepper stepperX(SPU, FULLSTEP);
MoToStepper stepperY(SPU, FULLSTEP);

String input;
String oldInput;

void setup()
{
  // Initialisierung der Steppers
  stepperX.attach( 3, 4, 5, 6);
  stepperY.attach( 7, 8, 9, 10);
  stepperX.setSpeed(150);
  stepperY.setSpeed(150);
 
  Serial.begin(9600);
}
void loop()
{
  while (!Serial.available());
  // Einlesung des Inputs 
  input = Serial.readString();
  Serial.print(input);
  if (input) {
    oldInput = input;
  }
  while (input) {
    // Input neuvergeben wenn neuer Input vorhanden ist
    if (Serial.available()) {
      input = Serial.readString();
      Serial.print(input);
    }
    // zusammenschneidung der Input VAR auf Maximal 2 Zeichen
    input = input.substring(0,2);
    if (input.equals("UR")) {
      Serial.print("\nMoving up and to the right");
      stepperX.doSteps(1);
      stepperY.doSteps(1);
    } else if (input.equals("UL")) {
      Serial.print("\nMoving up and to the left");
      stepperX.doSteps(-1);
      stepperY.doSteps(1);
    } else if (input.equals("DR")) {
      Serial.print("\nMoving down and to the right");
      stepperX.doSteps(1);
      stepperY.doSteps(-1);
    } else if (input.equals("DL")) {
      Serial.print("\nMoving down and to the left");
      stepperX.doSteps(-1);
      stepperY.doSteps(-1);
    } else if (input.equals("US")) {
      Serial.print("\nMoving up and stop x movement");
      stepperX.doSteps(0);
      stepperY.doSteps(1);
    } else if (input.equals("DS")) {
      Serial.print("\nMoving down and stop x movement");
      stepperX.doSteps(0);
      stepperY.doSteps(-1);
    } else if (input.equals("RS")) {
      Serial.print("\nMoving right and stop y movement");
      stepperX.doSteps(1);
      stepperY.doSteps(0);
    } else if (input.equals("LS")) {
      Serial.print("\nMoving left and stop y movement");
      stepperX.doSteps(-1);
      stepperY.doSteps(0);
    } else if (input.equals("SS")) {
      Serial.print("\nStopping all movements");
      stepperX.doSteps(0);
      stepperY.doSteps(0);
    }


  }
}
