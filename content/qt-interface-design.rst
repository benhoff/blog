###################
Qt Interface Design
###################

:date: 2017-06-26 17:21
:category: PyQt
:summary: Reviewing types of interface design for Qt
:slug: qt-interface-design

As part of our `PyQt Tutorial series`_, we've got a `hello world gui app`_ running. Now we need to design our application. So let's talk about some general desktop GUI design. You might have used a lot of GUI applications, but you probably never noticed their design. Especially (and super ironically) if it was done well. As a fun exercise, if someone asked you to design a web browser right now, what would your interface look like? 

If you're stumped, don't worry. A lot of people have thought about this before and have ideas. Three main ones in fact.

- Single Document Interface
- Tabbed Document Interface
- Multiple Document Interface

Single Document Interfaces
--------------------------

In a Single Document Interface, there's only a single window for each instance of the application. LibreOffice Writer, Microsoft Word, and most other word processors share this design.

.. image:: {static}/images/libreoffice-snap.png

Each document, or application, that's opened gets its own window. The window management is done by the native Desktop Environment.

I'd recommend a single document interface for most GUIs as long as the functionality is simple. Make sure that when you're designing your gui that pulling up multiple instances won't lock up resources (ports, databases, files, etc.).

.. TODO add in some example code of a single document design.

Single document design in PyQt is the default. We've pretty much got it going in our hello world example. The only thing we need to do is add some content to our Gui and organize it. I typically subclass a ``QWidget`` and use ``QLayout`` with ``QWidget.setLayout`` function to group things logically. ``QLayout`` has some subclasses that can be used to logically arrange things. A favorite is to use ``QVBoxLayout`` or ``QHBoxLayout`` since things kind of mostly resize correctly in Qt.

As I mentioned before, Single Document Interface programs are easy to program. A couple of cons however include the fact that it may be challenging to jam advanced functionality into them. Depending on the design or back end, if your user pulls up two instances, it can choke the system resources.

So what do you do if your interfaces need to be more complicated? Let's look at a few alternatives.

Tabbed Document Interfaces
--------------------------

Tabbed Document Interfaces are an extension of the Single Document Interface. Earlier when I asked what you might use to build a web browser... Well if you're on desktop, you probably thought of a tabbed interface. It's the most common.

.. image:: {static}/images/chrome-snap.png

I'd recommend tabbed document interfaces for anything more complicated than a single page.

Qt has a custom class to handle creating tabbed interfaces. ``QTabWidget`` and the ``QTabWidget.addWidget`` functionality are good spots to start. You can also make your own custom one looking at ``QTabBar``. I'll typically label the tabs logically and try to jam the most interesting/useful information in the left-most tabs (following the left to right reading pattern).

I think the biggest con that I can think of off the top of my head for a Tabbed design is the inability to change to a single document interface to refer to a previous tab. Web browsers got rid of this limitation by allowing you to pull a tab into a new window. While I believe this can be done with Qt, it would take a large amount of coding to accomplish.

Multiple Document Interfaces
----------------------------

And then multiple document interfaces are just interesting. I haven't seen many Multiple Document Interfaces out in the wild. The best example I have off the top of my head of a Multiple Document Interface that I've used is Solidworks, or other mechanical drafting software. Excel also has a Multiple Document Interface.

.. image:: https://i-msdn.sec.s-msft.com/dynimg/IC6922.gif

I'm not sure when the best time to use Multiple Document Interfaces would be. The challenge is that instead of letting the desktop environment control the window management, your program does instead. This can break the natural flow of the user, although this may be mitigated if you develop specifically for one platform (looking at you, Windows).

You can create an MDI in Qt using the ``QMdiArea`` and then adding windows using ``QMdiArea.addSubWindow``.

I'd recommend checking out the `wikipedia`_ page on the topic. The `Microsoft Developers Network`_ also has some documentation that might be of further use.

Mixed
-----

As I've hinted at several times already, there's always the option to mix these main interfaces as much as possible. Keep in mind as well, that there is a lot of support for toolbars and dock widgets (check out the ``QMainWindow`` documentation). The Integrated Developer Environment (IDE) ``Spyder`` is a great example of using dock widgets to great effect. 

As I wrap up, I'd like to recognize this excellent blog post on `User Interface Design for Business Applications`_. I default to Single Document Interfaces as much as possible until complexity gets me, and then I switch to a tabbed interface. But the aforementioned post helped me ensure I wasn't overlooking a design while I was crafting my latest creation.

Wrap Up
-------

Now that we know a couple of different design patterns, let's go ahead and apply them! Which is exactly what we'll do in the next section where we look at `layout management in PyQt`_. Or, if you'd like to jump around, `go to the top level index`_ and jump to the section of the tutorial that interests you most.


.. _`hello world gui app`: {static}/pyqt-hello-world.rst
.. _`User Interface Design for Business Applications`: https://richnewman.wordpress.com/category/tabbed-document-interface/
.. _`wikipedia`: https://en.wikipedia.org/wiki/Multiple_document_interface
.. _`Micrsoft Developers Network`: https://msdn.microsoft.com/en-us/library/ms997505.aspx?ranMID=24542&ranEAID=TnL5HPStwNw&ranSiteID=TnL5HPStwNw-L9gN68KGHNTwS1y_SVKSfw&tduid=(0b68db1eaba6ffcc15fac5f2d8ab4540)(256380)(2459594)(TnL5HPStwNw-L9gN68KGHNTwS1y_SVKSfw)() 
.. _`PyQt Tutorial series`: {static}/pyqt-tutorial.rst
.. _`layout management in PyQt`: {static}/pyqt-layout-design.rst
.. _`go to the top level index`: {static}/pyqt-tutorial.rst
