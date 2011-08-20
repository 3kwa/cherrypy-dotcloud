import json

import cherrypy

# pluging in a Redis backend for CherryPy sessions
# see http://pypi.python.org/pypi/cherrys
import cherrys
cherrypy.lib.sessions.RedisSession = cherrys.RedisSession

class Root:

    @cherrypy.expose
    def index(self):
        """ dummy controller counting the number of visits """
        counter = cherrypy.session.get('counter', 1)
        cherrypy.session['counter'] = counter + 1
        return "visit : %i" % counter

# getting the dotCloud environment variables
# see http://docs.dotcloud.com/guides/environment/
with open('/home/dotcloud/environment.json') as f:
    environment = json.load(f)

# configuring CherryPy sessions
config = {'/' :{
    'tools.sessions.on' : True,
    'tools.sessions.storage_type' : 'redis',
    'tools.sessions.host' : environment['DOTCLOUD_SESSION_REDIS_HOST'],
    'tools.sessions.port' : environment['DOTCLOUD_SESSION_REDIS_PORT'],
    'tools.sessions.password' : environment['DOTCLOUD_SESSION_REDIS_PASSWORD']
}}

application = cherrypy.tree.mount(Root(), '', config=config)
