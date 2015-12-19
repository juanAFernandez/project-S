# -*- coding: utf-8 -*-
from datetime import datetime

#importamos la API de mongo que está en el directorio padre
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

from mongoDBAPI.api import *
from hardwareAPI.api import *


'''
Para obtener el tiempo con el formato que nos interesa en este momento.
'''
def getTmp():
    return getTemperaturaMediaSensor1()
    #return '150.5'

def getTimeNow():
    #Captura el tiempo en este instante:
    date=datetime.now()
    #Devlvemos el tiempo
    return str(date.day)+'-'+str(date.month)+'-'+str(date.year)+'  '+str(date.hour)+':'+str(date.minute)

def medirYAlmacenar():

    #Creamos el diccionario
    medidaMuestra={}
    #No insertaremos el id, dejaremos que sea mongo quien lo haga por nosotros.
    #medidaMuestra['_id']=str(3723)
    medidaMuestra['tmp']=getTmp()
    medidaMuestra['date']=getTimeNow()
    print "Insertado "+ str(medidaMuestra)
    insertarDato(medidaMuestra)
    #coleccion.insert(medidaMuestra)


'''
Una futura mejora de la función será que recopile los datos cada cinco minutos, siendo estos
los minutos del reloj del sistema.
'''

def capturaPeriodica():
    while(True):
        print("tomando DATO")
        medirYAlmacenar()
        #Especificamos el tiempo de espera entre medidas
        time.sleep(30)

if __name__=="__main__":

    #capturaPeriodica()
    #print getTimeNow()

    capturaPeriodica()
