#####################################
Face Recognition With PyQt and OpenCV
#####################################

:date: 2017-06-10 14:25
:category: Blog
:slug: face-recognition
:summary: Working through adding Discourse Comments to the blog.
:status: draft

Oh man, this is going to be messy. All right, let's get started.

There's a lot of ground work for this post. The end goal is to take live images and record a classifier that will recognize your face, on the fly.

So what do we need for this? We'll need to gather several images to train our classifier. We'll also need to do some preprocessing, IE take an image, find the face, and rotate/crop it based on the eyeball coordinates.

We'll present this to our reader using a photo booth style. So let's work on that piece first.

We'll use a ``QLabel`` to display the image, ``QComboBox`` to choose the number of images that we want to take and picture delay and a ``QPushButton`` to get the thing to go.

.. TODO think about adding a flash?

.. code-block:: python

  from PyQt5 import QtWidgets, QtCore

  class PhotoBoothWidget(QtWidgets.QWidget):
       def __init__(self, parent=None):
           super().__init__(parent)
           self.label = QtWidgets.QLabel()
           number_label = QtWidgets.QLabel('Number of Pictures to Take')
           self.number_chooser = QtWidgets.QComboBox()
           self.number_chooser.addItems(['4', '5', '6', '7', '8', '9', '10'])
           self.delay_label = QtWidgets.QLabel('Number of Seconds to Delay')
           self.delay_chooser = QtWidgets.QComboBox()
           self.delay_chooser.addItems(['1', '1.5', '2', '4', '5', '7', '10'])

           self.go_button = QtWidgets.QPushButton('Run')

           form_layout = QtWidgets.QFormLayout()
           form_layout.addRow(number_label, self.number_chooser)
           form_layout.addRow(self.delay_label, self.delay_chooser)

           layout = QtWidgets.QVBoxLayout()
           layout.addLayout(form_layout)
           layout.addWidget(self.label)
           layout.addWidget(self.go_button)

           self.setLayout(layout)

       def image_data_slot(self, image_data):
            faces = self.detect_faces(image_data)
            for (x, y, w, h) in faces:
                 cv2.rectangle(image_data, (x, y), (x+w, y+h), self._red, self._width)

            self.image = self._get_qimage(image_data)

            if self.image.size() != self.size():
                self.setFixedSize(self.image.size())
            pixmap = QtWidgets.QPixmap.fromImage(self.image)

            self.label.setPixmap(pixmap)


        def _get_qimage(self, image: np.ndarray):
            height, width, colors = image.shape
            bytesPerLine = 3 * width
            QImage = QtGui.QImage

            image = QImage(image.data,
                           width,
                           height,
                           bytesPerLine,
                           QImage.Format_RGB888)

             image = image.rgbSwapped()
             return image



