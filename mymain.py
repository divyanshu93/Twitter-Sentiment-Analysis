
import sys
from PyQt4.Qt import *
from mainwindow import *
from PyQt4.QtGui import QApplication
from mainwindow import Ui_MainWindow

class Window(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self, parent = None):

        QMainWindow.__init__(self, parent)
        # or better
        # super(Window, self).__init__(parent)

        self.setupUi(self)

if __name__ == "__main__":

    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
