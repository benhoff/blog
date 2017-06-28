#########################
Vexbot State of the Union
#########################

:status: draft

All right, let's talk about Vexbot_.

Vexbot was created to scratch a very specific itch, conglomerating multiple chat sources into one place. No other bot (to my knowledge) can do this.

Vexbot does this by launching a subprocess for each chat provider (IRC, XMPP, Youtube, etc.) and using messaging (via zmq_) to co-locate them all. The GUI application, chatimusmaximus_ provides the user interface so that I could see all of the chat streams in one central place.

Vexbot has some simple chat processing, including direct string matching, and some natural language processing using the bag of words method to guess intent. These pieces are significantly underdeveloped.

Most of the time has been spent devoted to two important pieces: settings and process management.

On the settings management piece, I was originally using YAML_ to manage all the settings. Originally I thought this was a good approach as it allowed me to leave comments in the configuration file. So I could leave instructions for following. I quickly realized that you couldn't store credentials/settings for multiple services/servers. I started exploring SqlAlchemy for this purpose, but have yet to finish up an implementation that I'm happy with.

As I was creating my SQL database, I realized that there are some things that only really have one configuration. To that end, I would like create a ConfigParser instance that can load those types of configuration.

So now I've got an SQL database and a configuration file that I need to unify into one easy to use API. This has been... difficult.


Lastly, I've been thinking about the process management side of it. I would really like to offload the process management piece onto another piece of software. I've been thinking about using systemd to do this.

Additionally, I've been exploring expanding the command line interface. The Python Prompt Toolkit promised some interesting functionality that I wanted to take advantage of. I'd also like to create a Text User Interface.


.. _Vexbot:
.. _zmq: 
.. _chatimusmaximus:
.. _YAML:
