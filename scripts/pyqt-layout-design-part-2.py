import sys
from PyQt5 import QtCore, QtWidgets

class MasterWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        # Create a label, push button and line edit widgets
        label = QtWidgets.QLabel('This is a label')
        run_push_button = QtWidgets.QPushButton('Click Me')
        line_edit = QtWidgets.QLineEdit('Default line edit text')

        layout = QtWidgets.QGridLayout()
        # add widgets
        layout.addWidget(label, 0, 0)
        layout.addWidget(line_edit, 1, 0)
        layout.addWidget(run_push_button, 1, 1)

        # create our layout, a vertical layout
        # layout = QtWidgets.QVBoxLayout()
        # add widgets
        # layout.addWidget(label)
        # layout.addWidget(line_edit)
        # layout.addWidget(run_push_button)

        # set the layout of our master widget
        self.setLayout(layout)


def main():
    # We need to make the QApplication before our QMainWindow
    # We also need to pass in our system argument values (sys.argv)
    app = QtWidgets.QApplication(sys.argv)
    main_window = QtWidgets.QMainWindow()
    # QMainWindow requires a central widget.
    central_widget = MasterWidget()
    main_window.setCentralWidget(central_widget)
    # Show our main window
    main_window.show()
    # Start the event loop processing
    app.exec()


if __name__ == '__main__':
    main()
