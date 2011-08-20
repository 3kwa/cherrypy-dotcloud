import json

import cherrypy
import cherrys

cherrypy.lib.sessions.RedisSession = cherrys.RedisSession

class Root:

    @cherrypy.expose
    def index(self):
        counter = cherrypy.session.get('counter', 0)
        cherrypy.session['counter'] = counter + 1
        return counter

with open('/home/dotcloud/environment.json') as f:
    environment = json.load(f)

config = {'/' :{
    'tools.sessions.on' : True,
    'tools.sessions.storage_type' : 'redis',
    'tools.sessions.host' : environment['DOTCLOUD_SESSION_REDIS_HOST'],
    'tools.sessions.port' : int(environment['DOTCLOUD_SESSION_REDIS_PORT']),
    'tools.sessions.password' : environment['DOTCLOUD_SESSION_REDIS_PASSWORD']
}}

application = cherrypy.tree.mount(Root(), '', config=config)
