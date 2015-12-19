/*
Skecth para el proyecto Sensor TMP
Autor: Juan Antonio Fernandez Sanchez
Fecha: Diciembre 2015
*/

int ledPeticionWeb = 13;

int ledRojo = 2;
int ledAzul1 = 4;
int ledAzul2 = 7;
int ledAzul3 = 8;

void setup () {
   pinMode(ledPeticionWeb, OUTPUT);
   pinMode(ledRojo, OUTPUT); //LED 13 como salida
   pinMode(ledAzul1, OUTPUT);
   pinMode(ledAzul2, OUTPUT);
   pinMode(ledAzul3, OUTPUT);
   
   Serial.begin(9600); //Inicializo el puerto serial a 9600 baudios
}
 
void loop () {
   if (Serial.available()) { //Si está disponible
      char c = Serial.read(); //Guardamos la lectura en una variable char
      if (c == 'T') { 
        
         //Si es una 'H', enciendo el LED
         digitalWrite(ledPeticionWeb, HIGH);
         
         int value = analogRead(0);
         float millivolts = (value / 1024.0) * 5000;
         float celsius = millivolts / 10; 
         Serial.print(celsius);
         delay(500);
         
         digitalWrite(ledPeticionWeb, LOW);
         
         
         //Tomamos la primera medida:
         digitalWrite(ledAzul1, HIGH);
         float toma1=((analogRead(0)/1024.0)*5000)/10;
         delay(200);
         digitalWrite(ledAzul1, LOW);
         
         //Esperamos cinco segundos.
         delay(5000);
         
         //Tomamos la segunda medida:
         digitalWrite(ledAzul2, HIGH);
         float toma2=((analogRead(0)/1024.0)*5000)/10;
         delay(200);
         digitalWrite(ledAzul2, LOW);
         
         //Esperamos cinco segundos.
         delay(5000);
         
         //Tomamos la tercera medida:
         digitalWrite(ledAzul3, HIGH);
         float toma3=((analogRead(0)/1024.0)*5000)/10;
         delay(200);
         digitalWrite(ledAzul3, LOW);
         
         
         
         //Calculamos la media
         digitalWrite(ledRojo, HIGH);
         float media=(toma1+toma2+toma3)/3;
         delay(200);
         digitalWrite(ledRojo, LOW);
         
        // Serial.print(media);
         
      } else if (c == 'L') { //Si es una 'L', apago el LED
      
         //Se trata de una peticin de lectura media, para lo cual se toman tres medidas espaciadas por cinco segundos y se devuelve el valor medio
         //de las tres obtenido.
      
         digitalWrite(ledRojo, LOW);
      }
   }
}
