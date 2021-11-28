from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import *

class imageGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(640,480)
        self.setWindowTitle("Python Menus & Toolbars")
        self.centralWidget = QLabel(self)
        # Action define
        self._createActions()
        self._defineActions()
        self._connectActions()
        self._createMenuBar()

        # Create a layout and add your label to it
        layout = QVBoxLayout()
        layout.addWidget(self.centralWidget)

        # Create a central widget for QMainWindow and assign the layout
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def _createMenuBar(self):
        menuBar = self.menuBar()
        menuBar.setNativeMenuBar(False)
        self.setMenuBar = menuBar
        # Creating menus using a QMenu object
        fileMenu = menuBar.addMenu("&File")
        fileMenu.addAction(self.openAction)
        # Creating menus using a title
        editMenu = menuBar.addMenu("&Edit")

    def _createActions(self):
        # Creating actions using the second constructor
        self.openAction = QAction("&Open...", self)
        self.openAction.setShortcut("Ctrl+O")

    def _connectActions(self):
        # Connect File actions
        self.openAction.triggered.connect(self.openFile)

    def _defineActions(self):
        self.openFile = self.loadImage

    def loadImage(self):
        # load image
        try:
            fname = QFileDialog.getOpenFileName(self,"Select a file...", './',filter="Image Files (*)")
            imagePath = fname[0]
            pixmap = QPixmap(imagePath).scaledToWidth(640)
            self.centralWidget.setPixmap(pixmap)
            # self.resize(pixmap.width(),pixmap.height())
        except Exception as e:
            print(e)