# -*- coding: utf-8 -*-
from pymongo import MongoClient

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

for documento in cursor:
    print documento
