Using CherryPy on dotCloud
==========================

We are using tags to iterate through sections of an *exploratory tutorial* using CherryPy_ to discover dotCloud_:

1. quickstart_ from zero to hello in no time
2. static_ serving static content
3. local_ dev server (made spunkier using Fabric_)


Now to explore dotCloud_ a bit further let's look at the all mighty sessions_,
central to most web apps and an opportunity to roll out a new scallable service.

The Zen of ...
--------------

CherryPy_ has its own Zen_ (video_). It's first two koans state that:

    Common tasks should be fast and easy
    Doing nothing should be easier and faster

You want to use sessions_ in CherryPy_, turn them on in the configuration_::

    'tools.session.on' : True

That's all!

The default backend for sessions storage is memory. It works well for most
web applications but we want to be ready to scale beyond one CherryPy_ instance
hence will use something schnazier : Redis_

Redis on dotCloud
-----------------

To create a new redis instance on dotCloud_ we need to add a few line to our
build file::

    session:
        type: redis

Redis_ is notorious for its ease of deployement but that is trivial :P How do
we connect to that service you may wonder.

    ::

    $ dotcloud info tutorial.session
    cluster: wolverine
    config:
        redis_password: lshYSDfQDe
    created_at: 1310511988.2404289
    ports:
    -   name: ssh
        url: ssh://redis@bd0715e0.dotcloud.com:7473
    -   name: redis
        url: redis://redis:lshYSDfQDe@bd0715e0.dotcloud.com:7474
    state: running
    type: redis

But we know better than to hard code such things ...

dotCloud environment
--------------------

When dotCloud_ builds your application it create a file in the home directory of
your services named **environment.json**. For a Redis_ service it will contain
the following keys:

+ DOTCLOUD_*SESSION*_REDIS_HOST
+ DOTCLOUD_*SESSION*_REDIS_LOGIN
+ DOTCLOUD_*SESSION*_REDIS_PASSWORD
+ DOTCLOUD_*SESSION*_REDIS_PORT
+ DOTCLOUD_*SESSION*_REDIS_URL

Which we can use to configure_ CherryPy_!

Putting it all together
-----------------------

What's next?
------------

More play \o/!

.. _cherrypy: http://www.cherrypy.org
.. _dotcloud: https://www.dotcloud.com
.. _quickstart: https://github.com/3kwa/cherrypy-dotcloud/tree/quickstart
.. _static: https://github.com/3kwa/cherrypy-dotcloud/tree/static
.. _local: https://github.com/3kwa/cherrypy-dotcloud/tree/local-fabric
.. _fabric: http://fabfile.org
.. _zen: http://www.cherrypy.org/wiki/ZenOfCherryPy
.. _video: http://blip.tv/pycon-us-videos-2009-2010-2011/pycon-2010-the-zen-of-cherrypy-111-3352128
.. _sessions: http://www.cherrypy.org/wiki/CherryPySessions
.. _redis: http://redis.io
.. _environment: http://docs.dotcloud.com/guides/environment/
