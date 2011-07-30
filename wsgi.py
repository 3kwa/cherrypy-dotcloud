import cherrypy

class Root:

    @cherrypy.expose
    def index(self):
        return """
<!DOCTYPE HTML>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>CherryPy on dotCloud : a match made in heaven</title>
</head>
<body>
	<img src="static/cherrypy.png" alt="CherryPy" />
    <img src="static/dotcloud.png" alt="dotCloud" />
</body>
</html>"""

application = cherrypy.tree.mount(Root(), '')

if __name__ == "__main__":

    import os.path

    current_dir = os.path.dirname(os.path.abspath(__file__))
    config = {'/static' : {
        'tools.staticdir.on': True,
        'tools.staticdir.dir': os.path.join(current_dir, 'static')
        }}
    application.merge(config)

    cherrypy.quickstart()
