import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QAction, \
    QMessageBox, QCheckBox, QProgressBar, QLabel, QComboBox, QStyleFactory,\
    QFontDialog, QColorDialog, QCalendarWidget


class Window(QMainWindow):

    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(50, 50, 500, 400)
        self.setWindowTitle('pyqt5 Tuts')
        self.setWindowIcon(QIcon('python-logo.png'))

        extractAction = QAction("&GET TO THE CHOPPAH!!!", self)
        extractAction.setShortcut("Ctrl+Q")
        extractAction.setStatusTip('Leave The App')
        extractAction.triggered.connect(self.close_application)

        self.statusBar()

        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu('&File')
        fileMenu.addAction(extractAction)

        extractAction = QAction(QIcon('todachoppa.png'), 'Flee the Scene', self)
        extractAction.triggered.connect(self.close_application)

        self.toolBar = self.addToolBar("Extraction")
        self.toolBar.addAction(extractAction)

        fontChoice = QAction('Font', self)
        fontChoice.triggered.connect(self.font_choice)
        #self.toolBar = self.addToolBar("Font")
        self.toolBar.addAction(fontChoice)

        fontColor = QAction('Font bg Color', self)
        fontColor.triggered.connect(self.color_picker)

        self.toolBar.addAction(fontColor)

        cal = QCalendarWidget(self)
        cal.move(200,150)
        cal.resize(200,200)

        self.home()

    def home(self):
        btn = QPushButton("Quit", self)
        btn.clicked.connect(self.close_application)
        btn.resize(btn.minimumSizeHint())
        btn.move(100, 100)

        checkBox = QCheckBox('Enlarge Window', self)
        checkBox.stateChanged.connect(self.enlarge_window)
        checkBox.move(100, 60)
        checkBox.adjustSize()

        self.progress = QProgressBar(self)
        self.progress.setGeometry(200, 80, 250, 20)

        self.download_btn = QPushButton("Download", self)
        self.download_btn.move(200, 120)
        self.download_btn.clicked.connect(self.download)

        self.styleChoice = QLabel("Styles:", self)
        self.styleChoice.move(50, 150)

        comboBox = QComboBox(self)
        comboBox.addItems(QStyleFactory.keys())
        # comboBox.addItem("motif")
        # comboBox.addItem("Windows")
        # comboBox.addItem("cde")
        # comboBox.addItem("Plastique")
        # comboBox.addItem("Cleanlooks")
        # comboBox.addItem("windowsvista")
        comboBox.move(50, 250)

        comboBox.activated[str].connect(self.style_choice)

        self.show()

    def color_picker(self):
        color = QColorDialog.getColor()
        self.styleChoice.setStyleSheet("QWidget { background-color: %s}" % color.name())

    def font_choice(self):
        font, valid = QFontDialog.getFont()
        if valid:
            self.styleChoice.setFont(font)

    def style_choice(self, text):
        self.styleChoice.setText(text)
        QApplication.setStyle(QStyleFactory.create(text))

    def download(self):
        self.completed = 0

        while self.completed < 100:
            self.completed += 0.0001
            self.progress.setValue(self.completed)

    def enlarge_window(self, state):
        if state == Qt.Checked:
            self.setGeometry(50, 50, 1000, 600)
        else:
            self.setGeometry(50, 50, 500, 300)

    def close_application(self):
        choice = QMessageBox.question(self, 'Extract!',
                                      "Get into the chopper?",
                                      QMessageBox.Yes | QMessageBox.No)
        if choice == QMessageBox.Yes:
            print("Extracting Naaaaaaoooww!!!!")
            sys.exit()


app = QApplication(sys.argv)
Gui = Window()
sys.exit(app.exec_())


