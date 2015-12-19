# -*- coding: utf-8 -*-
import webapp2
import subprocess
import jinja2
import os
import serial
import time

STATIC_DIR = os.sep + 'tostatic' + os.path.abspath(os.path.dirname(__file__)) + os.sep + 'static'

template_env = jinja2.Environment(
	loader=jinja2.FileSystemLoader(os.getcwd())
	)
'''
arduino=serial.Serial('/dev/ttyACM1', baudrate=9600, timeout=3.0)
arduino.close()
arduino.open()
#txt=''
'''

class HelloWebapp2(webapp2.RequestHandler):
    def get(self):

	#Para raspberry Pi
	#vcgencmd es una herramienta propia de raspberry pi para acceder a la información especifica como temperaturas, frecuencias, etc...
	raspberry=False

	#txt=''

	if(raspberry):
		#Temperatura del procesador
		bashCommand = "/opt/vc/bin/vcgencmd measure_temp"
		process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
		coreTemp = process.communicate()[0]
	else:
		coreTemp = "not available"

	sensorTemp=''
	arduino.write('T')
	while arduino.inWaiting() > 0:
		#txt+="hola"
		sensorTemp+=arduino.read(1)

	templateVars = {"coreTemp" : coreTemp, "sensorTemp": sensorTemp}
	template = template_env.get_template('index.html')
	self.response.out.write(template.render(templateVars))

class Prueba(webapp2.RequestHandler):

    def get(self):
        template = template_env.get_template('index2.html')
        template_values = {'STATIC_DIR': STATIC_DIR }
        self.response.write(template.render(template_values))


app = webapp2.WSGIApplication([
    ('/h', HelloWebapp2),
	('/', Prueba),
], debug=True)

def main():
    from paste import httpserver
    httpserver.serve(app, host='localhost', port='8081')

if __name__ == '__main__':
    main()
