#################
Types of Programs
#################

:date: 2017-06-17 22:01
:category: Random
:slug: types-of-programs
:summary: Experienced programmers know one thing beginner programmers don't: types of programs.

I've had a lot of people ask my how to learn how to program.

And my favorite analogy for that, is that learning programming is a lot like learning carpentry. No one really asks how you become a carpenter. They just go off and build things. Tables, chairs, shelves, boxes.

Programming is the same way. You should just go off and build things. However, you're not sitting on a desktop application right now, or eating off a command line tool everyday. Programming doesn't have simple real life analogies that you can figure out how to build. And it's also hard to see how programming things are constructed.

So when you tell people to go off and build things, they're not going to know what to build. How do you Google something that you don't even know anything about?

So during this post, we're going to go over some of the major client-side types of applications you can build. Or to go back to the earlier carpenter analogy... we're going to talk about some of the furniture that you can build that you interact with on a daily basis. The programming desks and chairs, if you will.

Up front disclaimer, the libraries I'm going to discuss are all Python libraries. However, if you're programming in any other language, you should be able to Google ``java tui library`` for example and come up with similar libraries in your preferred language.

.. contents::

Command Line Interfaces
-----------------------

First and most simple is the command line interface (CLI). Love or hate them, a lot things in the programming world are CLI's. These programs are run from the shell and usually have different arguments passed in. Very popular in system administration due to the lack of graphical user interfaces installed in servers.

Python is a great example of a command line interface program.

.. code-block:: console

  $ python runfile.py

In this case, ``python`` is the program being run, while ``runfile.py`` is the argument being passed in.

I often use the ``-m`` module flag in order to make virtual environments for example.

.. code-block:: console

  $ python -m venv myvenv 

``python`` is again the program being run, the ``-m`` "module" flag tells python that I want to run a particular python module (the ``venv`` module in this case), and the ``venv`` module takes another argument to specify what I want the directory for the virtual environment to be named (``myvenv`` in this case).

One of the more advanced command line (non-programming-related) programs I've used is youtube-dl_.

The basic syntax for calling this program goes something like this

.. code-block:: console

  $ youtube-dl [OPTIONS] URL [URL...]

Several libraries in python exist to help you program a CLI.

Probably the most beginner friendly one is click_. However Python comes bundled with two in the standard library, including argparse_ and getopt_. I tend to use ``argparse`` in my personal projects. Your mileage may vary.

CLI's are common for scripting programs.

Terminal User Interfaces
------------------------

Terminal User Interfaces (TUIs) really only got named that way after Graphical User Interfaces (GUIs) came into existence. These programs are run in the terminal and tend to take over and redraw the entire terminal. According to Wikipedia, TUIs display computer graphics in text form. I just tend to think of them as programs that can be run from, and take over, the terminal.

Probably the best know TUIs are famous text editors, including Vim and EMACS.

.. image:: https://upload.wikimedia.org/wikipedia/commons/8/8c/Vim-%28logiciel%29-console.png
  :height: 324px
  :width: 546px

Again, there are several libraries to help implement TUIs. The curses_ library is probably the most well know library to create a TUI, although it is only available in linux. urwid_ is a bit more fully featured library for TUI creation.

TUI's are probably less common, although I've been interested in creating some for my own personal projects (not enough free time to grok the development process with ``urwid``). All of the goodness of a CLI, as you're still in the terminal, with a little bit more ease of use (man pages or help only get's you so far).

Graphical User Interfaces
-------------------------

According to Wikipedia, Graphical User Interfaces (GUIs) are a type of interface that allows users to interact with electronic devices through graphical icons and visual indicators. If you figure out what that means, let me know. That aside, GUI's are the bread and butter of computing. Your web browser is a GUI. Your games run in GUIs. If you've ever used the Windows or Mac Operating Systems, the predominate way you interact with the computer is through the use of GUI's.

.. figure:: https://upload.wikimedia.org/wikipedia/en/5/54/Microsoft_Office_2016_Screenshots.png
  :height: 360
  :width: 546

  ^ All GUIs.

Python has a host of libraries for building GUIs. There's the GTK_ library. My personal favorite, the Qt_ framework (especially the PyQt_ bindings of the Qt framework). The Python standard library also has tkinter_.

GUIs are used to build just about anything, and most normal people would look at you funny if you told them a program needed to be run from the terminal. The only thing that has surpassed them in popularity has been...

Web Pages
---------

You could argue this one, but the truth is a lot of applications today are created to be served as a web page. The web page has become a standard user interface paradigm.

The standard stack for a client side webpage uses html (words and format), CSS (styling), and JavaScript (dynamic scripting).

If you want to build something programmatic on a web page, you need to program in JavaScript. Or at least for the client (user facing) side. On the backside/server-side... Different story. 

Flask_ or django_ are two web frameworks for python. ``Django`` is a bit more full featured with database model helper classes built in, while ``flask``, as a micro framework, is much less opinionated.

I would recommend looking into a static site generator such as pelican_ if you're looking at creating something that just needs to be read.

`Jupyter notebooks`_ are also a great way to deliver content via the web.

Web pages are a very common way to deliver an application experience. They are arguably the most cross-platform and consistent user experience.

Knowledge Application
---------------------

So how does this information help you? We've covered the major types of client-side interfaces. If you wanted some inspiration for projects, but want to minimize the user interface portions of your programming, I might suggest researching existing CLI's that sound interesting or implement your own. Want something a little bit more discoverable and easy to navigate, but still in the terminal (maybe a low usage application)? TUIs, my friend. Need to create something that others will use on the computer? Maybe get into some GUI programming. Bowing down to the overwhelming web pressure? Well go learn some JavaScript for your client-side needs. But if it's a back-end you need, maybe ``flask`` or ``django`` can save you.

The point is to help provide a little bit of information into the terminology and types of programming applications, so that when you want to make your programming chair, you're a little more knowledgable about where to go searching.


.. _argparse: https://docs.python.org/3/library/argparse.html
.. _curses: https://docs.python.org/3/library/curses.html
.. _getopt: https://docs.python.org/3/library/getopt.html
.. _click: http://click.pocoo.org/5/
.. _youtube-dl: https://github.com/rg3/youtube-dl
.. _urwid: https://github.com/urwid/urwid
.. _GTK: https://www.gtk.org/A
.. _Qt: https://www.qt.io/
.. _PyQt: https://riverbankcomputing.com/software/pyqt/intro
.. _tkinter: https://docs.python.org/3/library/tk.html
.. _flask: http://flask.pocoo.org/
.. _django: https://www.djangoproject.com/
.. _pelican: https://blog.getpelican.com/
.. _`jupyter notebooks`: http://jupyter.org/ 
