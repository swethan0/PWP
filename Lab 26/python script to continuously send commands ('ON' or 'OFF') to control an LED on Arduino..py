const int ledPin = 13; // Built-in LED pin

void setup() {
  pinMode(ledPin, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  if (Serial.available() > 0) {
    String command = Serial.readStringUntil('\n');
    command.trim(); // clean whitespace

    if (command == "ON") {
      digitalWrite(ledPin, HIGH);
    } 
    else if (command == "OFF") {
      digitalWrite(ledPin, LOW);
    }
  }
}
