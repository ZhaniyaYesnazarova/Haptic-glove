const int pin = 3;


void setup(){
  Serial.begin(9600);
  pinMode(pin, OUTPUT);
}

void loop(){
  if (Serial.available()>0){
    digitalWrite(pin, LOW);
    int data = Serial.read();
    switch(data){
      case 'o':
      digitalWrite(pin, HIGH);
      break;
      case 'x':
      digitalWrite(pin, LOW);
    }
  }
}







