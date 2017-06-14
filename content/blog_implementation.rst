Blog Implementation Stream of Conscious
#######################################

:date: 2017-06-04 21:27
:tags: blog, implementation
:category: blog
:slug: blog-implementation
:authors: Ben Hoff
:summary: Starting implementation of the blog as a work in progress.

All right, let's start implementing a blog.

First off, let's get the Github Pages up first.

Going to `Github Pages site`_ gives the instructions. 

.. _`Github Pages site`: https://pages.github.com/

I need to create a repository named after my username and push the repo. Easy enough. Next I need to create an index.html file. Github recommends "hello world". Sounds good to me.

Using git to add and push my local repo up to the newly created repository. Visiting benhoff.github.io now shows our the new web page, hello world! Neat!

Cool, now that I've got my page up, on to the static website generation. I'll start by installing pelican in a virtual environment.

.. code-block:: console

    $ mkdir swdev/blog

    $ cd swdev/blog

    $ python -m venv venv

    $ source  venv bin activate

    (venv) $ pip install pelican

Pelican has a quick start. Hold my breath here ;)

.. code-block:: console

    (venv) $ pelican-quickstart

Oh man, I need a blog title? Hoff's heroes? Let's just stick with Ben's Blog for now. The only other question I'm stumped on is the generation of a Fabfile/Makefile. Let's say yes for now, and we can always delete it later.

Looks like pelican is familiar with using Github pages. Nice.

Awesome, the quickstart dumped a bunch of new files and folders into the directory. I've already written an initial thoughts post about this blog. Let's dump that in the content directory.

.. code-block:: console

    $ mv initial_blog_thoughts.txt content/initial_blog_thoughts.rst

I'm following the content tutorial here_.

.. _here: http://docs.getpelican.com/en/stable/content.html

There's a bunch of metadata that pelcian says I'm missing, including the date, tags, category, slug, authors, and summary. Let's go ahead and add all of those.

I'll need to go through and add in some of the resturctured text for the post, but I'll do it later.

Right now, I want to add in some ``pages``. According to Pelican, Pages are for _About_ and _Contact_ pages. That sounds good.

.. code-block:: console

    $ mkdir pages

Uh, I thought I could create an ``index.html``? Doesn't look like I can, I'll just follow the next step in the tutorial and see where I end up.

.. code-block:: console

    (venv) $ pelican /path/to/my/content

Looks like the content needs to be the file directory and not the actual content.

Nice, the output directory has an index file in it already. Let's check it out using my browser.

Ok, I'm not in love with the theme, but I can work with everything else.

Let's push this up and do it live.

Ok, not as easy as I would like. We're adventuring now. Pelican recommends_ the use of `ghp-import`. I hate this kind of adventuring, since I'm pretty sure it's not going to work. Sigh. Here we go.

.. _recommends: http://docs.getpelican.com/en/stable/tips.html

.. code-block:: console

    (venv) $ pip install ghp-import

    (venv) $ ghp-import output

    (venv) $ git push git@github.com:benhoff/benhoff.github.io.git gh-pages:master

Yea, that didn't work. Looks like since I've already pushed I'm going to have issues. Color me surprised. I swear, this is my surprised face.

I've now got a ``gh-pages`` branch. That might be worth looking into. After some digging looks like I need to push the gh-pages branch.

.. code-block:: console

    $ git push origin gh-pages

That didn't appear to work. Maybe deleting my old "hello world" index file will help.

Nope. Now we're just 404ing. Looks like for a user page, content must be in the master. Well screw that. Let's create a new repo for the blog code and then I'll just push the github.io pages separate.

*New repo named `blog`*

.. code-block:: console

    $ git remote set-url git@github.com:benhoff/blog.git

    $ git remote add publish git@github.com:benhoff/benhoff.github.io

    $ git push -f publish gh-pages:master

I'll still have to manually push the gh-pages branch, but this is good enough for now.

