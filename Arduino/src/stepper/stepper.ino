#include <Stepper.h>
int SPU = 2048;
Stepper MotorX(SPU, 3, 5, 4, 6);
Stepper MotorY(SPU, 9, 10, 11, 8);

char input;
void setup()
{
  MotorX.setSpeed(5);
  MotorY.setSpeed(5);
  Serial.begin(9600);
}
void loop()
{
  while (!Serial.available());
  input = Serial.readString().charAt(0);

  switch (input) {
    case 'U':
      MotorY.step(1);
      delay(2000);
      break;
    case 'D':
      MotorY.step(-1);
      delay(2000);
      break;
    case 'R':
      MotorX.step(1);
      delay(2000);
      break;
    case 'L':
      MotorX.step(-1);
      delay(2000);
      break;
    default:
      Serial.println("Whatever is: ");
      Serial.println(input);
      break;
  }
}
