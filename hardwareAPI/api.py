# -*- coding: utf-8 -*-
import serial
import time

#Variable global
puertoSerial = '/dev/ttyACM0'
'''
Conecta con el hardware y le envía un comando que que el código que hay en arduino
sepa lo que le estamos pidiengo y nos devuelva la temperatura medida de un sensor.



'''
def getTemperaturaSensor1():

    #Nos conectamos al puerto SERIAL donde está arduino.
    arduino = serial.Serial(puertoSerial, baudrate=9600)
    #arduino.close()
    arduino.open()
    resultado=''
    #Le enviamos a arduino el comando S1 que el recibirá e interpretará como la tmp del sensor 1
    arduino.write('a')
    time.sleep(0.5)
    txt=''
    while arduino.inWaiting() > 0:
        txt += arduino.read(1)

    arduino.close()
    #Devolvemos un flotante con la temperatura
    if txt!='':
        return float(txt)
    else:
        txt='valor no tomado'
        return txt


def getTemperaturaMediaSensor1():

    #Nos conectamos al puerto SERIAL donde está arduino.
    arduino = serial.Serial(puertoSerial, 9600)
    #arduino.close()
    arduino.open()
    #Le enviamos a arduino el comando S1 que el recibirá e interpretará como la tmp del sensor 1
    arduino.write('b')
    time.sleep(13)
    txt=''
    while arduino.inWaiting() > 0:
        txt += arduino.read(1)
    arduino.close()
    if txt!='':
	#print "heere"
	#print "here"+txt+str(len(txt))
        return float(txt)
    else:
        txt='valor no tomado'
        return txt

'''
while True:
      comando = raw_input('Introduce un comando: ') #Input
      arduino.write(comando) #Mandar un comando hacia Arduino
      if comando == 'H':
            print('LED ENCENDIDO')
      elif comando == 'L':
            print('LED APAGADO')

arduino.close() #Finalizamos la comunicacion
'''

#Por si lo queremos ejecutar de forma independiente (que no tenga qu ser llamado desde otro lugar)
if __name__=="__main__":

    while True:
        print 'Introduce comando a ejecutar: '
        print '1 : lecturaTemperaturaSensor1'
        print '2 : lecturaTemperaturaMediaSensor1 '
        comando = raw_input()
        if comando=='1':
            print str(getTemperaturaSensor1())
        if comando=='2':
            print str(getTemperaturaMediaSensor1())
