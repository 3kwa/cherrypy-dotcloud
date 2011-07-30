import os.path

import cherrypy

from wsgi import application

def serve(port=8080):

    current_dir = os.path.dirname(os.path.abspath(__file__))
    config = {'/static' : {
        'tools.staticdir.on': True,
        'tools.staticdir.dir': os.path.join(current_dir, 'static')
        }}
    application.merge(config)

    cherrypy.server.socket_port = int(port)
    cherrypy.quickstart()
