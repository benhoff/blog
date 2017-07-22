import cv2
from PyQt5 import QtWidgets, QtCore

from facerecog import get_haarcascade_filepath

# TODO: fix API
from facerecog.crop_face import CropFace


class FaceRecognizer(QtCore.QObject):
    def __init__(self,
                 face_classifier_filepath=None,
                 eye_classifier_filepath=None,
                 parent=None):

        super().__init__(parent)
        if face_classifier_filepath is None:
            face_classifier_filepath = get_haarcascade_filepath()
        if eye_classifier_filepath is None:
            eye_classifier_filepath = get_haarcascade_filepath('eyes')

        self.fisher_faces = cv2.faces.createFisherFaceRecognizer()
        # Need an integer as the key, and image as the
        self._images = {}
        self._eye_classifier = cv2.CascadeClassifier(eye_classifier_filepath)
        # TODO: decide if I want to do this here, or just faces in.
        # self._face_classifier = cv2.CascadeClassifier(face_classifier_filepath)

    def face_image_slot(self, face_image, label: int):
        eyes = self._eye_classifier.detectMultiScale(face_image,
                                                     scale_factor=1.3,
                                                     minNeighbors=3,
                                                     flags=cv2.CASCADE_SCALE_IMAGE)

        if len(eyes) > 2:
            # TODO: error? signal?
            return

        face_image = CropFace(face_image, eyes[0], eyes[1])

        try:
            self._images[label].append(face_image)
        except KeyError:
            self._images[label] = [face_image,]

    def train(self):
        labels = tuple(self._images.keys())
        images = tuple(self._images.values())
        self.fisher_faces.train(images, labels)


    def load_recognizer(self, filepath):
        self.fisher_faces.load(filepath)

    def save_recognizer(self, filepath):
        self.fisher_faces.save(filepath)


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
