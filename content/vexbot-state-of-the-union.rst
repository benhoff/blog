#########################
Vexbot State of the Union
#########################

:date: 2017-07-01 16:30
:category: Random
:slug: vexbot-state-of-the-union

All right, let's talk about Vexbot_.

Vexbot was created to scratch a very specific itch, conglomerating multiple chat sources into one place. No other bot (to my knowledge) can do this [1]_.

Vexbot does this by launching a subprocess for each chat provider (IRC, XMPP, Youtube, etc.) and using messaging (via zmq_) to communicate between them all. The GUI application, chatimusmaximus_ provides the user interface so that I could see all of the chat streams in one central place.

Vexbot has some simple chat processing, including direct string matching, and some natural language processing using the bag of words method to guess intent. These pieces are significantly underdeveloped. The reason that these important pieces are underdeveloped is because a large amount of recent developer time has has been spent devoted to two important pieces: settings and process management [2]_.

For settings management, I was originally using YAML_ to manage all the settings. I really liked this approach as it allowed me to leave comments in the configuration file for my users. For a simple stationary setup, this would work well. However, for changing values programmatically, the limitations of this system were quickly apparent. I wanted to create a quick setup feature where the setup could be programmed from the command line, likely using a Text User Interface (TUI). YAML files aren't the best format for doing this, frankly.

I started exploring SQLALchemy_ for this purpose, but have yet to finish up an implementation that I'm happy with. The current idea is that more "dynamic" services (IRC, XMPP) will get their own table for settings. Other, more static services will use the INI_ format. The python standard library configparser_ library handles the INI format nicely, it's easy enough to write out programmatically, and common to rewrite using a text editor.

So now I've got an SQL database and a configuration file that I need to unify into one easy to use API. I also need to settle on schema that I like. It'll take work, but I'm happy enough with the work.

The thing I'm not happy about is the process management piece.

Right not the process management is done in python, using the subprocess_ module. And I'm really not happy about it.

The point of Vexbot is not to duplicate any functionality that I have to. And man, have you ever noticed how good operating systems are at process management? Problem being that operating systems are hilariously un-cross platform.

I would probably double down and use systemd, but it forces me to bump up to the system level, instead of staying in userland. It's an unsolved issue. For now, I'll stick with using as much as the subprocess module as possible. Start, stop, kill, restart, update processes. The whole shebang.

Once the settings and the process management piece is taken care of, I'll get back to the natural language processing and expanding the plugins.

.. [1] The next closest well supported piece of software that I could find in Python was errbot_. Errbot had some limitations though, mainly only allowing a single chat provider at a time. Errbot does allow one thing that Vexbot does not, a unified API for chat related programming regardless of backend.

.. [2] It should be noted that the inital push was to get simple one-way text communication working between the various supported text services. Two way communication, or in-service commands haven't been, and continue to not be, a priority.

.. _INI: https://en.wikipedia.org/wiki/INI_file
.. _configparser: https://docs.python.org/3/library/configparser.html
.. _Vexbot: https://github.com/benhoff/vexbot
.. _zmq: http://zeromq.org/
.. _chatimusmaximus: https://github.com/benhoff/CHATIMUSMAXIMUS
.. _YAML: http://www.yaml.org/start.html
.. _errbot: https://github.com/errbotio/errbot
.. _SQLALchemy: https://www.sqlalchemy.org/
.. _subprocess: https://docs.python.org/3/library/subprocess.html
