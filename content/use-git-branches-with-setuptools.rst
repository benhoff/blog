##################################
Using Git Branches With Setuptools
##################################

:date: 2017-12-28
:category: Random
:slug: using-get-branches-with-setuptools
:summary: Want to specify a git dependency in a setup.py? Here's how.

I wanted to add a git branch in a dependency for a project of mine in the `setup.py` file. Should be easy right?

Several hours of research later and pinging a project maintainer to bump the version in his branch later...

It's actual not too bad once you know how to do it.

In your `setup` method you need to have two arguments.

- install_requires
- dependency_links

In this case, I was trying to add `python-prompt-toolkit`_ 2.0.0 branch to my project (1.0.15 is currently in pypi).

Let's pick the easy one first, the install_requires.

.. code-block:: python

  install_requires = ['prompt-toolkit>=2.0.0']

This requirement parsing will currently fail due to the fact there isn't a prompt-toolkit version greater than or equal to 2.0.0 in pypi.

.. code-block:: python

  dependency_links = ['git+https://github.com/jonathanslenders/python-prompt-toolkit@2.0#egg=prompt-toolkit-2.0.0']

There's a couple of special things about the way this link is written that are poorly documented that is worth writing about.

1. `git+https://github.com/jonathanslenders/python-prompt-toolkit` is a standard documented way to install git links using pip.
2. The `@2.0` specifies the branch that we want to use. Note that this happens to be a number in this case, but can be whatever branch you need. I.e., `dev`
3. The `#egg=prompt-toolkit-2.0.0` is the most important bit. 

First all, we specify which package this dependency provides with the `#egg=prompt-toolkit` piece.
The most important part of it that isn't documented anywhere is that you *must* provide a version number. I did this here with the `-2.0.0`. The string can be anything, but it must be there.

So for example, if you wanted to specify a dependency on the development version of Vexbot, the dependency link could look like this:

.. code-block:: python

  dependency_links = ['git+https://github.com/benhoff/vexbot@dev#egg=vexbot-0']

You can throw in whatever version number you'd like so that you can help properly guide your user as to what version you really need (like I did with the `install_requires` constraint on prompt-toolkit).

You can use this to:

- Specify a private git repository as a dependency in setup.py
- Specify a patch version of a repository over the package in pypi
- Specify a package that isn't published to pypi but is on Github

Hope that helps!

.. _`python-prompt-toolkit`: https://github.com/jonathanslenders/python-prompt-toolkit
