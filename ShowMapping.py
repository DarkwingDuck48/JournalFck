import sys
import os
import os.path
import json
from PyQt5.QtWidgets import (QMainWindow, QPushButton, QApplication, QWidget, QGridLayout, QAction,
                             qApp, QFileDialog, QComboBox, QLineEdit, QHBoxLayout, QLabel, QTableWidget, QTableWidgetItem)


class MainWindow():
    def __init__(self):
        pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())