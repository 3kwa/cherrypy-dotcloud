Using CherryPy on DotCloud
==========================

In the quickstart_ section we saw how easy it is to use CherryPy_ on dotCloud_, skipping the installing dotCloud_, creating an app and deploying it. Let's briefly correct that omission.

One step back
-----------

Installing dotCloud_ is as east as pip_::

    $ pip install dotcloud

You can then create a dotCloud_ app (let's call it **cherrypy**)::

    $ dotcloud create cherrypy

If it is the first time you run the ``dotcloud`` command you will be prompted for
your API key which you can find in the dotCloud_ settings_ section.

In dotCloud_ lingo **cherrypy** is the *deployment name* and guess what, deploying is a breeze::

    $ dotcloud push cherrypy

Yes it is that easy_!

Looking at the logs
-------------------

One of the many commands ``dotcloud`` understand is ``logs``::

    $ dotcloud logs cherrypy.www

Which runs the equivalent of ``tail -f`` on the relevant logs. We specified
the *deployment name* and the *service name*. So far we only have one service called **www***.

The error.log contains two lines related to static content, let's focus on the first::

    2011/07/30 09:28:25 [error] 13377#0: *32 open() "/home/dotcloud/current/static/favicon.ico" failed (2: No such file or directory), client: 10.68.47.216, server: hello-default-www-0, request: "GET /favicon.ico HTTP/1.0", host: "f3250dc8.dotcloud.com"

Most browsers look for a favicon_, we don't have one yet. A good opportunity to look at static content.

Static
------

Unless specified otherwise browsers look for the favicon_ at the **root** under
the name **favicon.ico**. A dotCloud_ instance is smart enough to serve it from
the **static** folder.


.. _quickstart: https://github.com/3kwa/cherrypy-dotcloud/tree/quickstart
.. _cherrypy: http://www.cherrypy.org
.. _dotcloud: https://www.dotcloud.com
.. _settings: https://www.dotcloud.com/accounts/settings
.. _easy: http://f3250dc8.dotcloud.com/
.. _favicon: http://en.wikipedia.org/wiki/Favicon
