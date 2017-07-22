######################
PyQt Signals and Slots
######################

:date: 2017-07-21 7:40
:category: PyQt
:slug: pyqt-signals-slots
:summary: Figuring out how to use signals and slots

Ok, so we've gone through some basic `layout management`_ in addition to a conversation about some `interface design`_, now when I click buttons I want things to happen!

In order to achieve that goal, we're going to have to learn about signals and slots.

Let me let you in on a little secret. Signals and slots? They're magical. Seriously, they are pretty cool.

Let's go back to our face recognition example. This time since we know layouts due to the `layout management`_ post, we're going to build our own widget so that we can better hook up our signals and slots.

This is going to track closely to the `face detection post`_ where I originally created this widget.

.. code-block:: python

  from PyQt5 import QtCore, QtWidgets
  from facerecog import (RecordVideo,
                         FaceDetectionWidget,
                         get_haarcascade_filepath)

  class FaceRecogControl(QtWidgets.QWidget):
      def __init__(self, parent=None):
           super().__init__(parent)
           haar_filepath = get_haarcascade_filepath()
           self.face_detect_widget = FaceDetectionWidget(haar_filepath)

           self.video_recording = RecordVideo()
           record_button = QtWidgets.QPushButton('Run')

           layout = Qtwidgets.QVBoxLayout()
           layout.addWidget(self.face_detect_widget)
           layout.addWidget(record_button)

           self.setLayout(layout)

You'll notice that in the code above, I didn't put the ``QPushButton`` (instance member name of ``record_button``), as a instance member. Since I added the push button to our layout, the layout will actually keep a reference to the instance, preventing garbage collection.

So all of that code should be review. Create a layout, add some widgets to the layout, and then set the layout on our widget.

Now let's go ahead and wire our creation up using signals and slots.

As the `documentation states`_, signals and slots are used for communication between objects. In this case, we want to communicate between our push button object and our record video object. Specially, when we push the "Run" button, we want our video recording object to start recording.

So looking at the `push button documentation`_, we can see that we have several signals available to us. The one we're interested in is ``clicked``. Now the function that we want called after our button is ``clicked`` is the ``start_recording`` method on the ``VideoRecord`` instance. To do this, we'll call the ``connect`` method on the ``clicked`` class instance and pass our ``start_recording`` method in as the argument. We also need to wire our ``image_data`` signal to our ``image_data_slot``. That's a lot of words. Let's see it in action.

.. code-block:: python

  class FaceRecogControl(QtWidgets.QWidget):
      def __init__(self, parent=None):
           super().__init__(parent)
           haar_filepath = get_haarcascade_filepath()
           self.face_detect_widget = FaceDetectionWidget(haar_filepath)

           self.video_recording = RecordVideo()
           record_button = QtWidgets.QPushButton('Run')

           layout = Qtwidgets.QVBoxLayout()
           layout.addWidget(self.face_detect_widget)
           layout.addWidget(record_button)

           self.setLayout(layout)

           # Connect our signal `clicked` to our method `start_recording`
           record_button.clicked.connect(self.video_recording.start_recording)

           # alias out the method call `image_data_slot` to make the code
           # line shorter
           image_data_slot = self.face_detect_widget.image_data_slot

           # connect our signal `image_data` to our method `image_data_slot`
           self.video_recording.image_data.connect(image_data_slot)

In PyQt, we can connect signals to any method call as long as the signatures match. In the case of our ``clicked`` method, no arguments are transmitted when the signal is emitted. However, if we look at the `QComboBox signal documentation`_, we'll see that some of the signals (``activated`` for example) emit arguments that we need to catch in our method call.

Let's go ahead and define our own custom signal. For example, maybe we want to transmit a signal whenever a face is detected in our widget. Let's go ahead and subclass our ``FaceDetectionWidget``. We'll create a ``face_detected`` signal and override our ``image_data_slot`` method to emit the face detected signal whenever we find a face.

.. code-block:: python

  class FaceSignalWidget(FaceDetectionWidget):
       # Create our signal
       face_detected = QtCore.pyqtSignal()

       def image_data_slot(self, image_data):
           faces = self.detect_faces(image_data)
           # If faces our found, `emit` our signal
           if faces:
               self.face_detected.emit()

           # NOTE: this code is same as base class ----------------------------
           for (x, y, w, h) in faces:
               cv2.rectangle(image_data, (x, y), (x+w, y+h), self._red, self._width)

           self.image = self.get_qimage(image_data)
           if self.image.size() != self.size():
               self.setFixedSize(self.image.size())

           self.update()
           # -----------------------------------------------------------------

Notice that we call the ``emit`` method on the ``face_detected`` signal.

But how do we emit arguments? Well we'll need to define the arguments that we want to pass in our signal. So let's say that we not only want to emit the fact that we detected a face, but we want to emit the coordinates of the face as well.

.. code-block:: python

  class FaceSignalWidget(FaceDetectionWidget):
       face_detected = QtCore.pyqtSignal()
       # define our `face_detection_coords` signal
       face_detection_coords = QtCore.pyqtSignal(int, int, int, int)

       def image_data_slot(self, image_data):
           faces = self.detect_faces(image_data)
           # If faces our found, `emit` our signal
           if faces:
               self.face_detected.emit()

           for (x, y, w, h) in faces:
               cv2.rectangle(image_data, (x, y), (x+w, y+h), self._red, self._width)
               # emit the coordinates, or at least the (x,y), width and height
               self.face_detection_coords.emit(x, y, w, h)

           # NOTE: this code is same as base class ----------------------------
           self.image = self.get_qimage(image_data)
           if self.image.size() != self.size():
               self.setFixedSize(self.image.size())

           self.update()
           # -----------------------------------------------------------------

Note that signals are always defined as class variables instead of instance variables. If you're confused about the difference, this `stack overflow post`_ does a good job of differentiating the two.

That should be enough to get you started. Be sure to check out the `PyQt documentation on signals and slots`_ for a more in depth treatment.

.. _`PyQt documentation on signals and slots`: http://pyqt.sourceforge.net/Docs/PyQt5/signals_slots.html
.. _`stack overflow post`: https://stackoverflow.com/questions/8959097/what-is-the-difference-between-class-and-instance-variables 
.. _`QComboBox signal documentation`: http://doc.qt.io/qt-5/qcombobox.html
.. _`push button documentation`: http://doc.qt.io/qt-5/qabstractbutton.html#signals
.. _`documentation states`: http://doc.qt.io/qt-5/signalsandslots.html
.. _`layout management`: {filename}/pyqt-layout-design.rst
.. _`know layouts`: {filename}/pyqt-layout-design.rst
.. _`interface design`: {filename}/qt-interface-design.rst
.. _`face detection post`: {filename}/face-detection-in-pyqt.rst
