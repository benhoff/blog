###################
Qt Interface Design
###################

:date: 2017-06-18 17:21
:category: PyQt
:summary: Reviewing types of interface design for Qt
:status: draft

OK, so we've got a `hello world gui app`_ running, now we need to design an application. But first, let's talk about some general desktop GUI design. You might have used a lot of GUI applications, but you probably never noticed the design. Especially the ones that were done well. In fact, when's the last time you thought about the design of your web browser? If someone asked you'd to design a new web browser, what type of interface would you build? Weird to think about right? Luckily, a lot of people have worked through this before and come up with some overarching themes.


There are three main categories of interface designs that we're going to be looking at.

- Single Document Interfaces
- Tabbed Document Interfaces
- Multiple Document Interfaces

Let me first recommend you to this excellent blog post on `User Interface Design for Business Applications`_. Anything that is amazing is from there, and everything else is from the Qt documentation. I am just the integrator. Let's get started.

Single Document Interfaces
--------------------------

I'd recommend a single document interface for most GUIs.

Tabbed Document Interfaces
--------------------------

I'd recommend tabbed document interfaces for anything more complicated than a single page.

Multiple Document Interfaces
----------------------------

And then multiple document interfaces are just interesting.

.. _`hello world gui app`: {filename}/pyqt-hellow-world.rst
.. _`User Interface Design for Business Applications`: https://richnewman.wordpress.com/category/tabbed-document-interface/
.. review this for interest: https://msdn.microsoft.com/en-us/library/ms997505.aspx?ranMID=24542&ranEAID=TnL5HPStwNw&ranSiteID=TnL5HPStwNw-L9gN68KGHNTwS1y_SVKSfw&tduid=(0b68db1eaba6ffcc15fac5f2d8ab4540)(256380)(2459594)(TnL5HPStwNw-L9gN68KGHNTwS1y_SVKSfw)() 
