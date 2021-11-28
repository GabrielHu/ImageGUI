import sys
from PyQt5.QtWidgets import QApplication
from imageGUI import imageGUI
# from controller import control

__version__ = '0.1'
__author__ = 'Renjiu Hu'


def main():
    # Create an instance of QApplication
    app = QApplication(sys.argv)
    window = imageGUI()
    window.show()
    # models = evalModel()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
