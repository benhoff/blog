Title: Python Extra Requires Woes
Date: 2019-11-21 21:39
Category:Other
Slug: python-extras-requires
Authors: Ben Hoff
Summary: Installing extras when running setup.py

One of the small things that I always forget or abuse in projects is "extras_requires". In python project "setup.py" file, you can drop small hints, or tier out the installation requirements so that users don't have to download every single dependency in the world to get your project running. This is achieved by the use of "extras_requires".

The problem is, I never remember how to install the extras when using my desired installation method of:

```bash
$ python setup.py develop`
```

Currently the only way I know how to do it is to do a "pip install -e .[my-extras-here]". I would like to be able to define the extras requires during development install. I've opened a [Stackoverflow question](https://stackoverflow.com/questions/58986867/use-python-setup-py-to-install-different-dependencies-with-develop-vs-install) to find out if it's possible. But based on some research, I don't think there is any way to do it.

I'll just change the project for now to include all the dependencies for my desired use case. I think the use of "extras_requires" for most of my personal projects is probably an anti-pattern.
