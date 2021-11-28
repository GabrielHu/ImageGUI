from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QPixmap, QPainter, QPen
from PyQt5.QtWidgets import *
from PIL import ImageQt
from paint import Draw


class imageGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        # set init UI
        self.resize(640, 480)
        self.setWindowTitle("Python Menus & Toolbars")
        self.centralWidget = QLabel(self)
        self.maskEdit = False
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
        # Creating menus using a title
        fileMenu = menuBar.addMenu("&File")
        fileMenu.addAction(self.openAction)
        fileMenu.addAction(self.saveAction)
        editMenu = menuBar.addMenu("&Edit")
        editMenu.addAction(self.maskAction)

    def _createActions(self):
        # Creating actions using the QAction constructor
        self.openAction = QAction("&Open...", self)
        self.openAction.setShortcut("Ctrl+O")
        self.saveAction = QAction("&Save...", self)
        self.saveAction.setShortcut("Ctrl+S")
        self.maskAction = QAction("&Manual mask...", self)
        self.maskAction.setShortcut("Ctrl+M")

    def _connectActions(self):
        # Connect File actions
        self.openAction.triggered.connect(self.openFile)
        self.saveAction.triggered.connect(self.saveFile)
        self.maskAction.triggered.connect(self.maskFile)

    def _defineActions(self):
        self.openFile = self.loadImage
        self.saveFile = self.saveImage
        self.maskFile = self.maskImage

    def loadImage(self):
        # load image
        try:
            fname = QFileDialog.getOpenFileName(
                self, "Select a file...", './', filter="Image Files (*)")
            imagePath = fname[0]
            pixmap = QPixmap(imagePath).scaledToWidth(640)
            self.centralWidget.setPixmap(pixmap)
        except Exception as e:
            print(e)

    def saveImage(self):
        # save image
        try:
            fname = QFileDialog.getSaveFileName(
                self, 'Save image', './', filter="Image Files (*)")
            if fname[0]:
                image = ImageQt.fromqpixmap(self.centralWidget.pixmap())
                image.save(fname[0])
        except Exception as e:
            print(e)

    def maskImage(self):
        # manual mask
        self.maskEdit = True
        self.drawing = False
        self.lastPoint = QPoint()
    
    def paintEvent(self, event):
        if self.maskEdit:
            painter = QPainter(self)
            painter.drawPixmap(self.rect(), self.centralWidget.pixmap())

    def mousePressEvent(self, event):
        if self.maskEdit and event.button() == Qt.LeftButton:
            self.drawing = True
            self.lastPoint = event.pos()

    def mouseMoveEvent(self, event):
        if self.maskEdit and event.buttons() and Qt.LeftButton and self.drawing:
            painter = QPainter(self.centralWidget.pixmap())
            painter.setPen(QPen(Qt.red, 3, Qt.SolidLine))
            painter.drawLine(self.lastPoint, event.pos())
            self.lastPoint = event.pos()
            self.update()

    def mouseReleaseEvent(self, event):
        if self.maskEdit and event.button == Qt.LeftButton:
            self.drawing = False
