import sys
from PyQt5 import QtCore, QtWidgets


def main():
    # We need to make the QApplication before our QMainWindow
    # We also need to pass in our system argument values (sys.argv)
    app = QtWidgets.QApplication(sys.argv)
    main_window = QtWidgets.QMainWindow()
    # QMainWindow requires a central widget, so we'll just pass in a
    # blank widget for now
    blank_widget = QtWidgets.QWidget()
    main_window.setCentralWidget(blank_widget)
    # Show our main window
    main_window.show()
    # Start the event loop processing
    app.exec()


if __name__ == '__main__':
    main()
