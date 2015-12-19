# -*- coding: utf-8 -*-
'''
Ejecución:
> python main.py
serving on http://127.0.1.1:8080
'''
from paste.urlparser import StaticURLParser
from paste.cascade import Cascade
from paste import httpserver
import mimetypes
import webapp2
import socket
import os
import jinja2
#Importamos todas las funciones implementadas en el fichero api.py en el directorio mongoDB
from mongoDB.api import *


STATIC_DIR = os.sep + 'tostatic' + os.path.abspath(os.path.dirname(__file__)) + os.sep + 'static'

template_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.getcwd()))


class HelloWorld(webapp2.RequestHandler):

    def get(self):
        template = template_env.get_template('templates/index.html')
        template_values = {'STATIC_DIR': STATIC_DIR }
        self.response.write(template.render(template_values))

class StaticView(webapp2.RequestHandler):
    def get(self, path):
        path = os.sep + path
        try:
            f = open(path, 'r')
            self.response.headers.add_header('Content-Type', mimetypes.guess_type(path)[0])
            self.response.out.write(f.read())
            f.close()
        except Exception, e:
            print 'Problem in StaticView:', e
            self.response.set_status(404)

class Prueba(webapp2.RequestHandler):

    def get(self):
        template = template_env.get_template('index2.html')
        #temperaturasSensor1={'a':234, 'b':253}

        datos=getTodo()


        template_values = {'STATIC_DIR': STATIC_DIR, 'coreTemp' : '23', 'sensorTemp' : '38', 'datos':datos}
        self.response.write(template.render(template_values))


# Create the main app
app = webapp2.WSGIApplication([
    ('/', Prueba),
    (r'/tostatic/(.+)', StaticView),
])

def main():
    httpserver.serve(app, host=socket.gethostname(), port='8080')

if __name__ == '__main__':
    main()
