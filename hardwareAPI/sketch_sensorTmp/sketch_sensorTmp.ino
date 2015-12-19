/*
Skecth para el proyecto Sensor TMP
Autor: Juan Antonio Fernandez Sanchez
Fecha: Diciembre 2015
*/

int ledPeticionWeb = 13;

int leds[3]={4,7,8};

int ledRojo = 2;
int ledAzul1 = 4;
int ledAzul2 = 7;
int ledAzul3 = 8;

int sensor1=0;

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

      // b = toma de temperatura del sensor1 con una media
      if (c == 'b') { 

         float medidas[3];        
         
         for(int i=0; i<3; i++){
           digitalWrite(leds[i], HIGH);
           int value = analogRead(sensor1);
           float millivolts = (value / 1024.0) * 5000;
           medidas[i] = millivolts / 10;
           if(i!=2) 
             delay(5000);
         }
         /*
         //Tomamos la primera medida:
         digitalWrite(ledAzul1, HIGH);
         float toma1=((analogRead(sensor1)/1024.0)*5000)/10;
         delay(200);
     
         
         //Esperamos cinco segundos.
         delay(5000);
         
         //Tomamos la segunda medida:
         digitalWrite(ledAzul2, HIGH);
         float toma2=((analogRead(sensor1)/1024.0)*5000)/10;
         delay(200);
         
         
         //Esperamos cinco segundos.
         delay(5000);
         
         
         //Tomamos la tercera medida:
         digitalWrite(ledAzul3, HIGH);
         float toma3=((analogRead(sensor1)/1024.0)*5000)/10;
         delay(200);
         */
                          
         //Calculamos la media
         digitalWrite(ledRojo, HIGH);
         float media=(medidas[0]+medidas[1]+medidas[2])/3;
         delay(200);
         
         for(int i=0; i<3; i++)
          digitalWrite(leds[i], LOW); 
//         digitalWrite(ledAzul1, LOW);
//         digitalWrite(ledAzul2, LOW);
//         digitalWrite(ledAzul3, LOW);
         digitalWrite(ledRojo, LOW);
         
         Serial.println(media);
         
      } else if (c == 'L') { //Si es una 'L', apago el LED
      
         //Se trata de una peticin de lectura media, para lo cual se toman tres medidas espaciadas por cinco segundos y se devuelve el valor medio
         //de las tres obtenido.
      
         digitalWrite(ledRojo, LOW);
      } else  if (c == 'a') { 
        
         //Si es una 'H', enciendo el LED
         digitalWrite(ledRojo, HIGH);
         digitalWrite(ledPeticionWeb, HIGH);
         
         int value = analogRead(sensor1);
         float millivolts = (value / 1024.0) * 5000;
         float celsius = millivolts / 10;
         //Enviamos los datos por el serial 
         Serial.println(celsius);
               
         //Dejamos un pe;queño delay para que sea visible la interaccion
         delay(500);
         
         digitalWrite(ledRojo, LOW);
         digitalWrite(ledPeticionWeb, LOW);
      }
   }
}
