import sys
import os
import json
from PyQt5.QtWidgets import (QMainWindow, QPushButton, QApplication, QWidget, QGridLayout, QAction, QVBoxLayout,
                             qApp, QFileDialog, QHBoxLayout, QLabel)
from table import Table


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.mappingtables = ''
        # Окно
        self.setGeometry(500, 300, 500, 100)
        self.setWindowTitle("JournalChanger")
        self.mainwidget = QWidget(self)
        self.setCentralWidget(self.mainwidget)
        self.layout_grid = QGridLayout()
        self.mainwidget.setLayout(self.layout_grid)
        # Exit
        exitAction = QAction('&Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(qApp.quit)

        # Mapping Settings Actions
        self.newmappingAction = QAction('New mapping')
        self.newmappingAction.setShortcut('Ctrl+N')
        self.newmappingAction.triggered.connect(self.showmapping)

        self.openmappingAction = QAction('Open mapping')
        self.openmappingAction.setShortcut('Ctrl+O')
        self.openmappingAction.triggered.connect(self.showmapping)

        self.statusBar()

        self.menubar = self.menuBar()
        self.fileMenu = self.menubar.addMenu('&File')
        self.settings = self.fileMenu.addMenu('&Mappings')
        self.settings.addAction(self.newmappingAction)
        self.settings.addAction(self.openmappingAction)
        self.fileMenu.addSeparator()
        self.fileMenu.addAction(exitAction)

        # buttons
        self.but1 = QPushButton("Show Mappings")
        self.layout_grid.addWidget(self.but1)
        self.but1.clicked.connect(self.showmapping)

    def showmapping(self):
        if self.sender().text() == "New mapping":
            filename = 'New'
        elif self.sender().text() == "Open mapping" or self.sender().text() == "Show Mappings":
            filename = QFileDialog.getOpenFileName(self, 'Open Mapping File', os.getcwd())
        else:
            print("test Button activated")
        self.mappingtables = MappingWindow(filename)
        self.mappingtables.show()


class MappingWindow(QMainWindow):
    def __init__(self, filename):
        super().__init__()
        self.filename = filename
        # Window
        self.setGeometry(500, 300, 500, 100)
        self.setWindowTitle("Mappings")
        self.mappingwidget = QWidget(self)
        self.setCentralWidget(self.mappingwidget)
        self.vbox_grid = QVBoxLayout()
        self.hbox_table_grid = QHBoxLayout()
        self.hbox_label_grid = QHBoxLayout()
        self.mappingwidget.setLayout(self.vbox_grid)

        # Toolbar actions
        # Exit
        exitAction = QAction('&Close', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip("Close mappings")
        # Add row
        addrows = QAction('Add Row', self)
        addrows.triggered.connect(self.addrow)
        addrows.setStatusTip("Add row to tables")
        # Delete row
        delrow = QAction('Del Row', self)
        delrow.triggered.connect(self.delrow)
        delrow.setStatusTip("Delete selected row")

        self.statusBar()

        self.menu = self.menuBar()
        fileMenu = self.menu.addMenu('&File')
        fileMenu.addAction(addrows)
        fileMenu.addAction(exitAction)

        self.toolbar = self.addToolBar("&Add")
        self.toolbar.addAction(addrows)
        self.toolbar.addAction(delrow)

        # Table for mapping
        self.sourcetable = Table(self.filename, 'Source')
        self.hbox_table_grid.addWidget(self.sourcetable)
        self.hbox_table_grid.addSpacing(40)
        self.targettable = Table(self.filename, 'Target')
        self.hbox_table_grid.addWidget(self.targettable)

        self.label1 = QLabel("Source")
        self.label2 = QLabel('Target')
        self.hbox_label_grid.addWidget(self.label1)
        self.hbox_label_grid.addSpacing(40)
        self.hbox_label_grid.addWidget(self.label2)

        self.vbox_grid.addLayout(self.hbox_label_grid)
        self.vbox_grid.addLayout(self.hbox_table_grid)

        self.butsave = QPushButton('Save mapping')
        self.butsave.clicked.connect(self.writemapping)

        self.vbox_grid.addWidget(self.butsave)

    def addrow(self):
        row = self.sourcetable.rowCount() + 1
        self.sourcetable.setRowCount(row)
        self.targettable.setRowCount(row)

    def delrow(self):
        # delete selected row from source and target tables
        rowtodel = self.sourcetable.currentRow()
        self.sourcetable.removeRow(rowtodel)
        self.targettable.removeRow(rowtodel)

    def writemapping(self):
        filesave = QFileDialog.getSaveFileName(self, "Save mapping", os.getcwd(), "JSON files(*.json)")
        print(filesave)
        mappings = {}
        for i in range(0, self.sourcetable.rowCount()):
            mapp = (dict
                (
                Source=dict(
                    account=self.sourcetable.item(i, 0).text(),
                    ICP=self.sourcetable.item(i, 1).text(),
                    MovProd=self.sourcetable.item(i, 2).text(),
                    VarLob=self.sourcetable.item(i, 3).text(),
                    MktOvr=self.sourcetable.item(i, 4).text(),
                    AuditDim=self.sourcetable.item(i, 5).text(),
                    RelPartDisc=self.sourcetable.item(i, 6).text(),
                    CostCenterDisc=self.sourcetable.item(i, 7).text(),
                    CustomType=self.sourcetable.item(i, 8).text()
                ),
                Target=dict(
                    account=self.targettable.item(i, 0).text(),
                    ICP=self.targettable.item(i, 1).text(),
                    MovProd=self.targettable.item(i, 2).text(),
                    VarLob=self.targettable.item(i, 3).text(),
                    MktOvr=self.targettable.item(i, 4).text(),
                    AuditDim=self.targettable.item(i, 5).text(),
                    RelPartDisc=self.targettable.item(i, 6).text(),
                    CostCenterDisc=self.targettable.item(i, 7).text(),
                    CustomType=self.targettable.item(i, 8).text()
                )
                )
            )
            mapp2 = dict.fromkeys([self.sourcetable.item(i, 0).text()], mapp)
            mappings.update(mapp2)
        mappingtowrite = dict.fromkeys(['Mappings'], mappings)
        print(mappingtowrite)
        with open(filesave[0], 'w', encoding='utf-8') as writefile:
            x = json.dumps(mappingtowrite, sort_keys=True, indent=4, ensure_ascii=False)
            writefile.write(x)
        writefile.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
