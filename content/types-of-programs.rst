#################
Types of Programs
#################

:date: 2017-06-17 22:01
:category: random
:slug: types-of-programs
:summary: Experienced programmers know one thing beginner programmers don't: types of programs.
:status: draft

My favorite analogy for learning to program, is that it's a lot like learning carpentry. If someone wants to learn carpentry, they make things. Tables, chairs, desks. The thing that an aspiring carpenter has over an aspiring programmer? Carpenters know what kinds of things can be made.

So let's talk about the major user-facing types of programs that can be created.

Command Line Interfaces
-----------------------

Love to love them, or love to hate them, a lot things in the programming world are command line interfaces. These are run from the shell and usually have command line arguments passed in. Very popular in system administration due to the lack of graphical user interfaces installed in servers.

Python is a great example of a command line interface program.

.. code-block:: shell

  $ python runfile.py

In this case, ``python`` is the program being run, while ``runfile.py`` is the argument being passed in.

One of the more advanced command line (non-programming-related) programs I've used is youtube-dl_.

The basic syntax for calling this program goes something like this

.. code-block:: shell

  $ youtube-dl [OPTIONS] URL [URL...]

Git comes to mind as a command line interface I use daily.

Several libraries exist to help you program a CLI.

Probably the most beginner friendly is click_.

Bundled with Python is argparse_ and getopt_. I tend to use ``argparse`` in my projects.

Terminal User Interfaces
------------------------

Terminal User Interfaces (TUIs) really only got named that way after Graphical User Interfaces (GUIs) came into existence. Probably the best know TUIs are text editors, including Vim and EMACS.

.. image:: https://en.wikipedia.org/wiki/Text-based_user_interface#/media/File:Vim-(logiciel)-console.png

The curses_ library is probably the most well know library to create a TUI, although it is only available in linux.

urwid_ is a bit more full featured library for TUI creation.

Graphical User Interfaces
-------------------------

Graphical User Interfaces (GUIs) are the bread and butter of computing. Your web browser is a GUI. If you've ever used the Windows Operating System, the predominate way you interact with the computer is through the use of GUI's.

There's the GTK library.

My personal favorite, the Qt libraries (especially the PyQt bindings of the Qt framework).

tkinter.

Web Pages
---------

You could argue this one, but the truth is a lot of applications today are created to be served as a web page. The web page has become a standard user interface paradigm.

There's not a whole lot of ways to serve a dynamic/interface style to the end user.

I would recommend looking into a static site generator such as pelican_ if you're looking at creating something that just needs to be read.

flask_ is a microframework.
django_ is a bit more full featured with database model helper classes built in.

`jupyter notebooks`_ are also a great way to deliver content via the web


.. _argparse: https://docs.python.org/3/library/argparse.html
.. _curses: https://docs.python.org/3/library/curses.html
.. _getopt: https://docs.python.org/3/library/getopt.html
.. _click: http://click.pocoo.org/5/
.. _youtube-dl: https://github.com/rg3/youtube-dl
.. _urwid: https://github.com/urwid/urwid
