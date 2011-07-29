Using CherryPy on DotCloud
==========================

Why?
----

It is so easy it is not funny! WSGI_ is your friend (read the doc_).

CherryPy_, a mature and maintained fun way to do web with Python_, does WSGI_
since 2004_.

The DotCloud_ team documented *trendier* options but I never tried to recover
from a bad first Django_ experience_.

Cherries blossom in the cloud too!

How?
----

Tell Dotcloud_ you are using a Python_ service in the **dotcloud.yml** file::

    www:
        type: python

Claim your love for CherryPy_ in the **requirements.txt** file (PIP style)::

    CherryPy==3.2.0

Then, in a file named **wsgi.py** file, create a wsgi_ callable called
**application**::

    import cherrypy

    class Root:

        @cherrypy.expose
        def index(self):
            return "Hello!"

    application = cherrypy.tree.mount(Root(), '')

Push and voila_!

What's next?
------------

Using GitHub tags (and branches) to write a step by step tutorial ... Maybe ;)

.. _2004: http://www.cherrypy.org/wiki/WSGI
.. _cherrypy: http://www.cherrypy.org
.. _wsgi: http://wsgi.org/
.. _doc: http://docs.dotcloud.com/services/python/
.. _python: http://www.python.org
.. _dotcloud: https://www.dotcloud.com
.. _django: http://www.djangoproject.com
.. _voila: http://f3250dc8.dotcloud.com/
.. _experience: http://colivri.org
