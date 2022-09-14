/*
 * Super simple money making button, the perfect gift for any Managing Director, or Director of Finance.
 * Raises profits with every press.
 */
 
#include <Bounce.h>

// Bouncy Bounce
Bounce button9 = Bounce(8, 10);
String MillionPounds [ 5 ] = {"Work Harder!!1!1", "Keep working subordinates!", "Make it chargable", "Work!!!!!1", "Money please", "ONE MILLION POUNDS!"};
const int len = sizeof(MillionPounds) / sizeof(MillionPounds[0]);

void setup() {
  pinMode(8, INPUT_PULLUP);
}

void loop() {
  button9.update();

  // Magic Button!
  if (button9.risingEdge()) {
    Keyboard.println(MillionPounds[random(len)]);
    delay(200);
  }
}
