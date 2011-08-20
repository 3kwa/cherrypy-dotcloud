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

CherryPy_ has its own Zen_ (video_). It's first two koans state that::

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

+ DOTCLOUD_SESSION_REDIS_HOST
+ DOTCLOUD_SESSION_REDIS_LOGIN
+ DOTCLOUD_SESSION_REDIS_PASSWORD
+ DOTCLOUD_SESSION_REDIS_PORT
+ DOTCLOUD_SESSION_REDIS_URL

Note that *SESSION* is the name of the Redis_ service we specified in the build
file. It can be whatever you want.

::

    with open('/home/dotcloud/environment.json') as f:
        environment = json.load(f)

Is all you need to load the content of **environment.json** in the aptly name
**environment** variable :P

We can use this information to configure_ CherryPy_ but first ...

Dependencies
------------

CherryPy_ doesn't support Redis_ backend out of the box. The cherrys_ python
package comes to the rescue ;) First let's add 2 lines to our requirements.txt

::

    cherrys>=0.3
    hiredis

We talked about it before, straightforward pip_ freeze_ format.

Putting it all together
-----------------------

Now we plug in the redis backend into CherryPy_ (explicit is better than
implicit cf PEP20_)::

    import cherrys
    cherrypy.lib.sessions.RedisSession = cherrys.RedisSession

And configure_ our application::

    config = {'/' :{
        'tools.sessions.on' : True,
        'tools.sessions.storage_type' : 'redis',
        'tools.sessions.host' : environment['DOTCLOUD_SESSION_REDIS_HOST'],
        'tools.sessions.port' : environment['DOTCLOUD_SESSION_REDIS_PORT'],
        'tools.sessions.password' : environment['DOTCLOUD_SESSION_REDIS_PASSWORD']
    }}

Voila_ : a dummy web application that counts the number of visits :P

What's next?
------------

More play **\\o/**

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
.. _configure: http://docs.cherrypy.org/stable/concepts/config.html
.. _configuration: http://docs.cherrypy.org/stable/concepts/config.html
.. _cherrys: http://pypi.python.org/pypi/cherrys
.. _pip: http://www.pip-installer.org/
.. _freeze: http://www.pip-installer.org/en/latest/index.html#freezing-requirements
.. _pep20: http://www.python.org/dev/peps/pep-0020/
.. _voila: http://78a277f4.dotcloud.com/
