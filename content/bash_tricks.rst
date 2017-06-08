Bash String Subsitution
#######################

:date: 2017-06-08 13:19
:category: programming
:slug: bash-string-subsitution
:authors: Ben Hoff
:summary: Learning how to do string subsitution in bash commands

A little personal confession: I'm really bad at the command line. And it's not that I'm just bad, it's that I actively know there's a better way to do it and I often don't.

One of the little tricks that has saved me is the use of the double exclaimation marks.

`$ pacman -S interesting package`
`error: you cannot perform this operation unless you are root`
`sudo !!`

Using the double exclaimation marks will save you from retyping all of those things. It's saved my sanity many a times.

The one thing I have never looked into is how to search and replace the command.

Until today.

`git comit -m 'really long commit message which should convince me to stop typing these directly into the command line'`
`git: 'comit' is not a git command. Did you mean commit`
Dammit.

the way to fix this? As a vim user this is the syntax that I'll remember.

`!!:s/comit/commit`

Alternatively,

`^comit^commit^`

The next thing I'm going to learn is how to search my bash history. Probably. Maybe.
