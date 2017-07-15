Bash String Subsitution
#######################

:date: 2017-06-08 13:19
:category: Random
:slug: bash-string-substitution
:summary: Learning how to do string substitution in bash commands

A little personal confession: I'm really bad at the command line. And by bad, I mean willfully ignorant. I often know there's a better way to work in the command line and I often don't learn how to do it.

For example, one of the little tricks that has saved me a lot of time is the use of the double exclamation marks to redo and edit a command.

.. code-block:: console

    $ pacman -S interesting-package
    error: you cannot perform this operation unless you are root
    $ sudo !!
    sudo pacman -S interesting-package

Using the double exclamation marks will save you from retyping all of the things when you forget something simple like a sudo. It's saved my sanity many a times.

One example of my willful ignorance, is with misspelling things on the command line

.. code-block:: console

    $ git comit -m 'really long commit message'
    git: 'comit' is not a git command. See 'git --help'
    
    The most similar command is
            commit

Dammit. Up until today, I've pressed the up arrow to bring the command back up, then used the left arrow to navigate all the way back to my mistake before fixing it.

The crazy thing is I know there's a way to do a simple string substitution. I've just been too lazy to look it up.

Until today. Today, with the use of Google, I become a power user.

As a vim user this is the syntax that I'll remember.

.. code-block:: console

    $ !!:s/comit/commit

Alternatively, if you've invested in a saner text editor, a simpler syntax is:

.. code-block:: console

    $ ^comit^commit^

Now, if only I could remember the way to navigate to the beginning of a command line (`Ctl-e?`.... `Ctl-a?`)

or learn how to use my bash history....

Well there's always tomorrow.
