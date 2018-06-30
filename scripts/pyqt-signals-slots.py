import sys
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

       # Connect our signal `clicked` to our method `start_recording`
       record_button.clicked.connect(self.video_recording.start_recording)

       # alias out the method call `image_data_slot` to make the code
       # line shorter
       image_data_slot = self.face_detect_widget.image_data_slot

       # connect our signal `image_data` to our method `image_data_slot`
       self.video_recording.image_data.connect(image_data_slot)


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


def main():
    # We need to make the QApplication before our QMainWindow
    # We also need to pass in our system argument values (sys.argv)
    app = QtWidgets.QApplication(sys.argv)
    main_window = QtWidgets.QMainWindow()
    # QMainWindow requires a central widget.
    haar_file = get_haarcascade_filepath()
    central_widget = FaceSignalWidget(haar_file)
    main_window.setCentralWidget(central_widget)
    # Show our main window
    main_window.show()
    # Start the event loop processing
    app.exec()


if __name__ == '__main__':
    main()
