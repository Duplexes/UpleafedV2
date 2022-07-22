int x;
bool led1 = false;
bool led2 = false;
bool led3 = false;
bool led4 = false;
bool led5 = false;


// Remember to change led pinouts in production code
void setup() {
 Serial.begin(115200);
 Serial.setTimeout(1);
 pinMode(13, OUTPUT);
 pinMode(12, OUTPUT);
 pinMode(11, OUTPUT);
 pinMode(10, OUTPUT);
 pinMode(9, OUTPUT);
 pinMode(8, OUTPUT);
 pinMode(7, OUTPUT);
 pinMode(6, OUTPUT);
 pinMode(5, OUTPUT);
 pinMode(4, OUTPUT);
 pinMode(3, OUTPUT);
 pinMode(2, OUTPUT);
 pinMode(1, OUTPUT);
 digitalWrite(12, HIGH); // Red LED on
 digitalWrite(10, HIGH); // Red LED on
 digitalWrite(8, HIGH); // Red LED on
 digitalWrite(6, HIGH); // Red LED on
 digitalWrite(4, HIGH); // Red LED on
}

void loop() {
 while (!Serial.available());
 x = Serial.readString().toInt();
 if (x == 1) {
    Serial.println("LED1 Toggled to ON");
   if (led1 == false) {
     digitalWrite(13, HIGH);  // Green LED on
     digitalWrite(12, LOW);  // Red LED off
     led1 = true;
   } else {
     digitalWrite(13, LOW); // Green LED off
     led1 = false;
   }
    } else if (x == 2) {
    Serial.println("LED2 Toggled ");
    if (led2 == false) {
      digitalWrite(11, HIGH); // Green LED on
      digitalWrite(10, LOW); // Red LED off
      led2 = true;
    } else {
        digitalWrite(11, LOW); // Green LED off
        led2 = false;
    }
    }
    else if (x == 3) {
    Serial.println("LED3 Toggled ");
    if (led3 == false) {
      digitalWrite(9, HIGH); // Green LED on
        digitalWrite(8, LOW); // Red LED off
      led3 = true;
    } else {
        digitalWrite(9, LOW); // Green LED off
        led3 = false;
    }   }
    else if (x == 4) {
    Serial.println("LED4 Toggled ");
    if (led4 == false) {
      digitalWrite(7, HIGH); // Green LED on
        digitalWrite(6, LOW); // Red LED off
      led4 = true;
    } else {
        digitalWrite(7, LOW); // Green LED off
        led4 = false;
    }   }
    else if (x == 5) {
    Serial.println("LED5 Toggled ");
    if (led5 == false) {
      digitalWrite(5, HIGH); // Green LED on
      digitalWrite(4, LOW); // Red LED off
      led5 = true;
    } else {
        digitalWrite(5, LOW); // Green LED off
        led5 = false;
    }   }
    else {
      Serial.println("Invalid Input");
    }
}