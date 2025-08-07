const int pin = 10;

void setup(){
  Serial.begin(9600);
  pinMode(pin, OUTPUT);
}

void loop(){
  if (Serial.available()>0){
    analogWrite(pin, 0);
    int data = Serial.read();
    switch(data){
      case 'o':
      analogWrite(pin, 255);
      break;
      case 'x':
      analogWrite(pin, 0);
    }
  }
}







