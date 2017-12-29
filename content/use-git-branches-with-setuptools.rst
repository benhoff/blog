##################################
Using Git Branches With Setuptools
##################################

:date: 2017-12-28
:category: Random
:slug: using-git-branches-with-setuptools
:summary: Want to specify a git dependency in a setup.py? Here's how.

I wanted to add a git branch in a dependency for a project of mine in the `setup.py` file. Should be easy right?

Several hours of research later and pinging a project maintainer to bump the version in his branch later...

And it's actual not too bad once you know how to do it. So let's figure out how to do it.

In the `setup` method of `setup.py` you need to have two arguments.

- install_requires
- dependency_links

In this case, I was trying to add the `python-prompt-toolkit`_ 2.0.0 branch to my project (Version 1.0.15 is currently in pypi).

Let's pick the easy one first, the install_requires.

.. code-block:: python

  install_requires = ['prompt-toolkit>=2.0.0']

This requirement parsing will currently fail due to the fact there isn't a prompt-toolkit version greater than or equal to 2.0.0 in pypi. So let's fix that by specifying the 2.0.0 branch with in the dependency links.

.. code-block:: python

  dependency_links = ['git+https://github.com/jonathanslenders/python-prompt-toolkit@2.0#egg=prompt-toolkit-2.0.0']

There's a couple of special things about the way this link is written that are poorly documented, and thus worth writing about.

1. `git+https://github.com/jonathanslenders/python-prompt-toolkit` -> Standard documented way to install git links using pip. Nothing to see here, just an FYI.
2. The `@2.0` specifies the branch that we want to use. Note that this happens to be a number in this case, but can be whatever branch you need. I.e., `dev` would be a common interesting branch name that could be used by specifying `@dev`.
3. The `#egg=prompt-toolkit-2.0.0` is the most important bit and worth expounding on a little more.

We need to specify which package this dependency link provides. We do this with the `#egg=PACKAGE_NAME` syntax. In this case, this dependency link provides the package `prompt-toolkit`, ie `#egg=prompt-toolkit`

But the most important part of this portion of a dependency link, and one that isn't documented at all, is that you *must* provide a version number. I've done this here with the `-2.0.0`. The version number you provide can be any version, but it must be there.

So for example, if you wanted to specify a dependency on the development version of Vexbot, the dependency link could look like this:

.. code-block:: python

  dependency_links = ['git+https://github.com/benhoff/vexbot@dev#egg=vexbot-0']
  
Note the `-0` specifying the version number at the end of the vexbot dependency link.

You can throw in whatever version number you'd like so that you can help properly guide your user as to what version you really need (like I did with the `install_requires` constraint on prompt-toolkit).

Please note that dependency links are useful! You can use them to:

- Specify a private git repository as a dependency in setup.py
- Specify a patch version of a repository over the package in pypi
- Specify a package that isn't published to pypi but is on Github

Hope that helps!

.. _`python-prompt-toolkit`: https://github.com/jonathanslenders/python-prompt-toolkit
