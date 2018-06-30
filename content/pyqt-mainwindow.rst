PyQt MainWindow
===============

:date: 2018-01-01 01:01
:category: PyQt
:status: draft
:summary: Setup our Main Window.

As part of our `PyQt Tutorial series`_, we've added in some `signals and slots`_, and done some basic `layout management`_. Now let's work on our main window a bit. What'd I like is a prompt that shows up everytime we've detected a face. We'll also put in some basic file handeling methods in as well. Ready?

As a reminder, `here's what our code looks like currently`_. We've got two custom widget, one widget which gives us some basic buttons for controls and houses the main camera, and a reimplemented widget from the ``facerecog`` package which handles the OpenCV logic for us. We've also got a ``main`` function which ties everything together.

We'll be leveraging our ``face_detected`` signal that we created in the last section of the tutorial. Let's create a big disclaimer that we've detected a face!

We'll subclass our QMainWindow to make concrete implementations and move some of the code from our ``main`` method into our implementation.

.. code-block:: python

  from PyQt5 import QtWidgets

  class StatusBar(QtWidgets.QStatusBar):
      def __init__(self, parent=None):
          super().__init__(parent)

  class MainWindow(QtWidgets.QMainWindow):
      def __init__(self, parent=None):
          super().__init__(parent)
          haar_file = get_haarcascade_filepath()
          central_widget = FaceSignalWidget(haar_file)
          self.setCentralWidget(central_widget)

.. image:: http://doc.qt.io/qt-5/images/mainwindowlayout.png
  :align: center

.. code-block:: python

  from PyQt5 import QtWidgets

  class StatusBar(QtWidgets.QStatusBar):
      def __init__(self, parent=None):
          super().__init__(parent)


.. _`PyQt Tutorial series`: {filename}/pyqt-tutorial.rst
.. _`signals and slots`: {filename}/pyqt-signals-slots.rst
.. _`layout management`: {filename}/pyqt-layout-design.rst
