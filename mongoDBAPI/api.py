# -*- coding: utf-8 -*-
from pymongo import MongoClient


def simulaUnDia():
    import datetime

    medidaMuestra={"_id":1, "tmp":"32.5", "date":"34.4"}

    client= MongoClient()
    db = client['temperaturas']
    coleccion=db['sensor1']


    for a in range(0, 50):
        #Inserta
        medidaMuestra['_id']=str(int(medidaMuestra['_id'])+1)
        medidaMuestra['tmp']=str(float(medidaMuestra['tmp'])+1)
        coleccion.insert(medidaMuestra)
        #Modifica

    cliente.close()

def insertarDato(dato):

    #Realizamos la conexión.
    client= MongoClient()
    db = client['temperaturas']
    coleccion=db['sensor1']
    coleccion.insert(dato)


def getTodo():


    print "USANDO GENERAL"


    #Creando la conexión:
    client= MongoClient()
    #Al no especificar host ni puerto está conectando en
    #localhost con el puerto 27017

    #Nos conectamos a la base de datos llamada temperaturas
    db = client['temperaturas']

    #Accedemos a la colección
    coleccion=db['sensor1']


    #Creamos un cursor para mostrar los elementos de la colección:
    cursor = db.sensor1.find()

    datos2={}

    i=1
    '''
    {u'tmp': u'22.4', u'date': u'19:38', u'_id': ObjectId('56708eeec805a73ee32feff1')}
    {u'tmp': u'22.4', u'date': u'19:38', u'_id': ObjectId('56708ef1c805a73ee32feff2')}
    {u'tmp': u'32.4', u'date': u'39:38', u'_id': ObjectId('56708ef9c805a73ee32feff3')}

    '''
    listaA=[]
    listaB=[]
    for medida in cursor:
        #Ahora cada documento dentro del cursor es un diccionario.
        print medida['tmp']
        listaA.append(i)
        listaB.append(float(medida['tmp']))
        datos2[str(i)]=float(medida['tmp'])
        i+=1;

    client.close()

    print datos2



    datos={'a':32.5, 'b':34.4, 'c':43.5 }
    print datos

    #listaA=[1,2,3,4]
    #listaB=[10,20,30,40]

    datos3={
        'listaA':listaA,
        'listaB':listaB
    }
    return datos3
