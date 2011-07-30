Using CherryPy on dotCloud
==========================

We are using tags to iterate through sections of an *exploratory tutorial* using CherryPy_ to discover dotCloud_:

1. quickstart_ from zero to hello in no time
2. static_ serving static content

Although dotCloud_ makes it super easy to have something up and running, in
development mode we favor working locally and pushing for testing, staging or production.

CherryPy server
---------------

CherryPy_ comes with a *production-ready, HTTP/1.1-compliant server*. To
paraphrase SQLite_ `when to use`_ document, the CherryPy_ server could be used as is for *99.9% of the websites around*. It is that good ;)

Quick and dirty
---------------

The quickest way to have a local *development* server running is to use the
idiomatic `if __name__ == "__main__"` block::

    if __name__ == "__main__":
        cherrypy.quickstart

Adding these 2 lines at then end of **wsgi.py** and we are good to go::

    $ python wsgi.py

We have a server running (on 127.0.0.1:8080 by default) with autoreload and
many other goodies, and it appears to be working. Opening a browser we see
*Hello!* and the favicon and looking at the log everything seems fine but ...

Shameless promotion
-------------------

CherryPy_ is configured to automagically use its favicon if none is available!
If **Root.index** returns *elaborate* html::

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
    </html>

Duh!

Static configuration
--------------------

Despite having both PNGs in the static folder, CherryPy_ doesn't know *yet*
how to look for them. Let's tweak our `if __name__ == "__main__"` block
a little::

    if __name__ == "__main__":

        import os.path

        current_dir = os.path.dirname(os.path.abspath(__file__))
        config = {'/static' : {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': os.path.join(current_dir, 'static')
            }}
        application.merge(config)

        cherrypy.quickstart()

CherryPy_ comes with a collection of `builtin tools`_, one of them to serve
static content. To configure_ CherryPy_ we use a Python_ dictionnary.

We are telling CherryPy_ to use the **staticdir** tool to serve requests
for **/static**. Then, we update the configuration of the WSGI_ **application**
used by dotCloud_ ... done?

Fabric
------

We would probably be better off keeping the CherryPy_ related code away from the
dotCloud_ WSGI_ code. Why not use the brilliant Fabric_ for that?

Let's move the `if __name__ == "__main__"` block into a **serve** Fabric_ task (defined in **fabfile.py**). Now to run our local dev server we do::

    $ fab serve

And if we want to run it on another port::

    $ fab server:3000

Schnazy, isn't it?

.dotcloudignore
---------------

**fabfile.py** does not need to be pushed on dotCloud_. There are ways_ to
exclude files from being pushed but ... none satisfying.

What's next?
------------

Not sure yet, probably something session related!

.. _quickstart: https://github.com/3kwa/cherrypy-dotcloud/tree/quickstart
.. _static: https://github.com/3kwa/cherrypy-dotcloud/tree/static
.. _cherrypy: http://www.cherrypy.org
.. _dotcloud: https://www.dotcloud.com
.. _sqlite: http://www.sqlite.org
.. _`when to use`: http://www.sqlite.org/whentouse.html
.. _`builtin tools`: http://www.cherrypy.org/wiki/BuiltinTools
.. _configure: http://www.cherrypy.org/wiki/ConfigAPI
.. _Python: http://www.python.org
.. _wsgi: http://www.wsgi.org
.. _fabric: http://fabfile.org
.. _ways: http://docs.dotcloud.com/guides/git-hg/#excluding-files-from-the-push
