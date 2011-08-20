import json

import cherrypy

class Root:

    @cherrypy.expose
    def index(self):
        counter = cherrypy.session.get('counter', 0)
        cherrypy.session['counter'] = counter + 1
        return counter

with open('/home/dotcloud/environment.js') as f:
    environment = json.load(f)

config = {'/' :{
    'tools.session.on' : True,
    'tools.session.storage_type' : 'redis',
    'tools.session.host' : environment['DOTCLOUD_DATA_REDIS_HOST'],
    'tools.session.port' : environment['DOTCLOUD_DATA_REDIS_PORT'],
    'tools.session.password' : environment['DOTCLOUD_DATA_REDIS_PASSWORD']
}}

application = cherrypy.tree.mount(Root(), '', config=config)
