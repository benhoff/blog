import sys
from PyQt5 import QtCore, QtWidgets

from facerecog import MainWidget, get_haarcascade_filepath


def main():
    # We need to make the QApplication before our QMainWindow
    # We also need to pass in our system argument values (sys.argv)
    app = QtWidgets.QApplication(sys.argv)
    main_window = QtWidgets.QMainWindow()
    # QMainWindow requires a central widget.
    haar_file = get_haarcascade_filepath()
    central_widget = MainWidget(haar_file)
    main_window.setCentralWidget(central_widget)
    # Show our main window
    main_window.show()
    # Start the event loop processing
    app.exec()


if __name__ == '__main__':
    main()
