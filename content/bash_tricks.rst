Bash String Subsitution
#######################

:date: 2017-06-08 13:19
:category: programming
:slug: bash-string-subsitution
:authors: Ben Hoff
:summary: Learning how to do string subsitution in bash commands

A little personal confession: I'm really bad at the command line. And by bad, I mean willfully ignorant. I often know there's a better way to work in the command line and I often don't learn how to do it.

For example, one of the little tricks that has saved me a lot of time is the use of the double exclaimation marks to redo and edit a command.

`$ pacman -S interesting-package`

`error: you cannot perform this operation unless you are root`

`$sudo !!`

`sudo pacman -S interesting-package`

Using the double exclaimation marks will save you from retyping all of the things when you forget something simple like a sudo. It's saved my sanity many a times.

One example of my willful ignorance, is with misspelling things on the command line'

`$ git comit -m 'really long commit message which should convince me to stop typing these directly into the command line'`

`$ git: 'comit' is not a git command. Did you mean commit`

Dammit. Up until today, I've pressed the up arrow to bring the command back up, then used the left arrow to navigate all the way back to my mistake before fixing it.

The crazy thing is I know there's a way to do a simple string subsitution. I've just been too lazy to look it up.

Until today. Today, with the use of Google, I become a power user.

As a vim user this is the syntax that I'll remember.

`$ !!:s/comit/commit`

Alternatively, if you've invested in a saner text editor, a simplier syntax is:

`$ ^comit^commit^`

Now, if only I could remember the way to navigate to the beginning of a command line (`Ctl-e?`.... `Ctl-a?`)

or learn how to use my bash history....

Well there's always tomorrow.
