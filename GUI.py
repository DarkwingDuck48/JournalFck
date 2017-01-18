import sys
import os
from PyQt5.QtWidgets import (QMainWindow, QPushButton, QApplication, QWidget, QGridLayout, QAction,
                             qApp, QFileDialog, QComboBox, QLineEdit, QHBoxLayout, QLabel, QTableWidget, QTableWidgetItem)
from Tool import Tool


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Окно
        self.setGeometry(500, 300, 500, 100)
        self.setWindowTitle("JournalChanger")
        self.mainwidget = QWidget(self)
        self.setCentralWidget(self.mainwidget)
        self.layout_grid = QGridLayout()
        self.mainwidget.setLayout(self.layout_grid)

        exitAction = QAction('&Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(qApp.quit)

        settings = QAction('&Mapping', self)
        settings.setStatusTip('Mappings settings')

        self.statusBar()

        self.menubar = self.menuBar()
        fileMenu = self.menubar.addMenu('&File')
        fileMenu.addAction(settings)
        fileMenu.addSeparator()
        fileMenu.addAction(exitAction)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())