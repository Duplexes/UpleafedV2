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
}

void loop() {
 while (!Serial.available());
 x = Serial.readString().toInt();
 if x == 1 {
    Serial.println("LED1 Toggled ");
   if led1 == false {
     digitalWrite(LED_BUILTIN, HIGH);
     led1 = true;
   } else {
     digitalWrite(LED_BUILTIN, LOW);
     led1 = false;
   }
    } else if x == 2 {
    Serial.println("LED2 Toggled ");
    if led2 == false {
      digitalWrite(LED_BUILTIN, HIGH);
      led2 = true;
    } else {
        digitalWrite(LED_BUILTIN, LOW);
        led2 = false;
    }
    }
    else if x == 3 {
    Serial.println("LED3 Toggled ");
    if led3 == false {
      digitalWrite(LED_BUILTIN, HIGH);
      led3 = true;
    } else {
        digitalWrite(LED_BUILTIN, LOW);
        led3 = false;
    }   }
    else if x == 4 {
    Serial.println("LED4 Toggled ");
    if led4 == false {
      digitalWrite(LED_BUILTIN, HIGH);
      led4 = true;
    } else {
        digitalWrite(LED_BUILTIN, LOW);
        led4 = false;
    }   }
    else if x == 5 {
    Serial.println("LED5 Toggled ");
    if led5 == false {
      digitalWrite(LED_BUILTIN, HIGH);
      led5 = true;
    } else {
        digitalWrite(LED_BUILTIN, LOW);
        led5 = false;
    }   }
    else {
      Serial.println("Invalid Input");
    }
}