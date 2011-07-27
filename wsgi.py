import cherrypy

class Root:

    @cherrypy.expose
    def index(self):
        return "Hello!"

application = cherrypy.tree.mount(Root(), '')
