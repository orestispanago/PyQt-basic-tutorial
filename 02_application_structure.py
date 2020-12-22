import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow


class Window(QMainWindow):

    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(50, 50, 500, 300)
        self.setWindowTitle('pyqt5 Tuts')
        self.setWindowIcon(QIcon('python-logo.png'))
        self.show()


app = QApplication(sys.argv)
Gui = Window()
sys.exit(app.exec_())
