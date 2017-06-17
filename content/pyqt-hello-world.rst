############################
PyQt Hello World Application
############################

:date: 2017-06-16 13:27
:category: PyQt
:summary: Creating the hello world app of desktop applications.

.. contents::

Getting Started
---------------

We're going to start with a hello world application, as sometimes getting everything installed and working correctly can be an emotionally terrifying experience. Just ask me. I've done software before.

So starting from nothing.

Install Python 
--------------

`Follow these installation instructions`_, based on your OS.

If you're running a linux distribution, you can likely use your native package manager.

Make sure if you're running Windows that you add Python to your path library. It should be a pop-up option during the install. If you mess up, `turn to Google`.


Make sure you install Python 3. This tutorial will not be for `Python 2`_ as Python 2 is reaching it's end of life for official support.


Create A Working Directory
--------------------------

Create a directory you want to work out of.

.. code-block:: console

  $ mkdir pyqt
  $ chdir pyqt


Create Virtual Environment
--------------------------

We're going to create and activate a virtual environment, so that your global site-packages stays clean. Hard to keep track of which project, installed which dependencies, otherwise.

.. code-block:: console

        $ python -m venv venv
        $ source venv/bin/activate

Install PyQt5
-------------

Right, now that our virtual environment is activated, let's install PyQt.

.. code-block:: console

        (venv) $ pip install PyQt5

Write Boilerplate Code
----------------------

Now, fire up your favorite text editor, it's time to start programming. We'll create a file name *__main__.py* practice a couple of nicety's: the creation of a main loop, and a standard script sequence

.. code-block:: python

  # file name: __main__.py

  def main():
      pass

  if __name__ == "__main__":
      main()

Write PyQt Specific Code
------------------------

Now, in our main function, we're going to create an instances of `QApplication`_ and `QMainWindow`_. I'd recommend reading the documentation_ on ``QApplication``, especially the section with the *main areas of responsibility*. The TLDR on ``QApplication`` responsibilities:

- event handling
- main settings

``QMainWindow`` is a magical class. It gives a lot of normal desktop interface aspects that you've come to expect, such as a menu bar, tool bars, and status bars... *for free*. Again, the `documentation is awesome`_, but check out the below figure to get a hint for the types of functionality that are integrated into the ``QMainWindow`` class.

.. figure:: http://doc.qt.io/qt-5/images/mainwindowlayout.png

  Notice that the Menu Bar and Status Bar are tied to QMainWindow. We'll come back to that.

So now that we now a little bit about what we're doing, let's write the rest of the code.

.. code-block:: python

  # file name: __main__.py

  import sys
  from PyQt5 import QtCore, QtWidgets

  def main():
      # We need to make the QApplication before our QMainWindow
      # We also need to pass in our system argument values (sys.argv)
      app = QtCore.QApplication(sys.argv)
      main_window = QtWidgets.QMainWindow()
      # QMainWindow requires a central widget, so we'll just pass in a 
      # blank widget for now
      blank_widget = QtWidgets.QWidget()
      main_window.setCentralWidget(blank_widget)
      # Show our main window
      main_window.show()
      # Start the event loop processing
      app.exec()

.. TODO Get photo evidence

That's it! You should see a small window open up. We've got the "Hello World" version for GUI programming.

Next time, we'll talk about some choices for our central widget design.

.. Reference for next post: https://richnewman.wordpress.com/category/tabbed-document-interface/

.. _QApplication: http://doc.qt.io/qt-5/qapplication.html
.. _QMainWindow: http://doc.qt.io/qt-5/qmainwindow.html
.. _`documentation is awesome`: http://doc.qt.io/qt-5/qmainwindow.html#details
.. _documentation: http://doc.qt.io/qt-5/qapplication.html#details
.. _`Follow these installation instructions`: http://python-guide-pt-br.readthedocs.io/en/latest/starting/installation/
.. _`Python 2`: https://pythonclock.org/
.. _`turn to Google`: https://stackoverflow.com/questions/6318156/adding-python-path-on-windows-7
