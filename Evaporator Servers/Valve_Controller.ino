String m = "";
int Controller[] = {2,3,4,5,6,7};
int valvestat[] = {0,0,0};

void setup() {
 int i;
 for(i = 0;i<6;i++){
   pinMode(Controller[i], OUTPUT);
   digitalWrite(Controller[i], LOW);
 }
   Serial.begin(9600);

}

void loop() { 
  if (Serial.available()){
    char input;
    while (input != 'r'){
      if (Serial.available()){
         input = Serial.read();
         if (input != 'r'){
           m += input;
         }
         else if (input = 'r'){
           valve();
         }
         else{
           Serial.print("Invalid Entry.");
      }
    }
  }
}
}

void valve(){
  if(m.startsWith("i")){
    Serial.write("Valve and Relay Control\r\n");
  }  
  else if (m.startsWith("o") && m.endsWith("t")){
    digitalWrite(2, HIGH);
    valvestat[0] = 1;
    Serial.println("Turbo Valve Open\r\n");
    Serial.print("Turbo,");Serial.print(valvestat[0]);Serial.print(" Chamber,");Serial.print(valvestat[1]);Serial.print(" Gate,");Serial.println(valvestat[2]);
  }
  else if (m.startsWith("c") && m.endsWith("t")){
    digitalWrite(2, LOW);
    valvestat[0] = 0;
    Serial.println("Turbo Valve Closed\r\n");
    Serial.print("Turbo,");Serial.print(valvestat[0]);Serial.print(" Chamber,");Serial.print(valvestat[1]);Serial.print(" Gate,");Serial.println(valvestat[2]);
  }  
  else if (m.startsWith("o") && m.endsWith("c")){
    digitalWrite(3, HIGH);
    valvestat[1] = 1;
    Serial.println("Chamber Valve Open\r\n");
    Serial.print("Turbo,");Serial.print(valvestat[0]);Serial.print(" Chamber,");Serial.print(valvestat[1]);Serial.print(" Gate,");Serial.println(valvestat[2]);
  }
  else if (m.startsWith("c") && m.endsWith("c")){
    digitalWrite(3, LOW);
    valvestat[1] = 0;
    Serial.println("Chamber Valve Closed\r\n");
    Serial.print("Turbo,");Serial.print(valvestat[0]);Serial.print(" Chamber,");Serial.print(valvestat[1]);Serial.print(" Gate,");Serial.println(valvestat[2]);
  }  
  else if (m.startsWith("o") && m.endsWith("g")){
    digitalWrite(4, HIGH);
    valvestat[2] = 1;
    Serial.println("Gate Valve Open\r\n");
    Serial.print("Turbo,");Serial.print(valvestat[0]);Serial.print(" Chamber,");Serial.print(valvestat[1]);Serial.print(" Gate,");Serial.println(valvestat[2]);
  }
  else if (m.startsWith("c") && m.endsWith("g")){
    digitalWrite(4, LOW);
    valvestat[2] = 0;
    Serial.println("Gate Valve Closed\r\n");
    Serial.print("Turbo,");Serial.print(valvestat[0]);Serial.print(" Chamber,");Serial.print(valvestat[1]);Serial.print(" Gate,");Serial.println(valvestat[2]);
  }  
   else if (m.startsWith("o") && m.endsWith("4")){
    digitalWrite(5, HIGH);
    Serial.println("Valve 4 Open\r\n");
  }
  else if (m.startsWith("c") && m.endsWith("4")){
    digitalWrite(5, LOW);
    Serial.println("Valve 4 Closed\r\n");
  }  
    else if (m.startsWith("o") && m.endsWith("5")){
    digitalWrite(6, HIGH);
    Serial.println("Valve 5 Open\r\n");
  }
  else if (m.startsWith("c") && m.endsWith("5")){
    digitalWrite(6, LOW);
    Serial.println("Valve 5 Closed\r\n");
  } 
   else if (m.startsWith("o") && m.endsWith("6")){
    digitalWrite(7, HIGH);
    Serial.println("Valve 6 Open\r\n");
  }
  else if (m.startsWith("c") && m.endsWith("6")){
    digitalWrite(7, LOW);
    Serial.println("Valve 6 Closed\r\n");
  } 
  m = "";
      
  }  

