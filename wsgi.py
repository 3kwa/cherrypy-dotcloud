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
