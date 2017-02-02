import json
import sys
import os, os.path
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem, QScrollBar


class Table(QTableWidget):
    def __init__(self, filename, tabletype):
        super(Table, self).__init__()
        self.filename = filename
        self.tabletype = tabletype
        self.setColumnCount(9)
        self.columnname = ['Account', 'ICP', 'MovProd', 'VarLob', 'MktOvr', 'AuditDim', 'RelPartDisc1',
                           'CostCenterDisc2', 'CustType']
        self.v_scrollBar = QScrollBar()
        self.setVerticalScrollBar(self.v_scrollBar)

        for i in range(len(self.columnname)):
            self.setHorizontalHeaderItem(i, QTableWidgetItem(self.columnname[i]))
        if self.filename == 'New':
            self.setRowCount(2)
        else:
            with open(self.filename[0], "r", encoding="utf-8") as file:
                alldict = json.load(file)
                mappings = alldict["Mappings"]
                self.setRowCount(len(mappings.keys()))
                row = 0
                keylist = []
                for acc in mappings.keys():
                    keylist.append(acc)
                keylist.sort()
                for acc in keylist:
                    self.setItem(row, 0, QTableWidgetItem(mappings[acc][self.tabletype]['account']))
                    self.setItem(row, 1, QTableWidgetItem(mappings[acc][self.tabletype]['ICP']))
                    self.setItem(row, 2, QTableWidgetItem(mappings[acc][self.tabletype]['MovProd']))
                    self.setItem(row, 3, QTableWidgetItem(mappings[acc][self.tabletype]['VarLob']))
                    self.setItem(row, 4, QTableWidgetItem(mappings[acc][self.tabletype]['MktOvr']))
                    self.setItem(row, 5, QTableWidgetItem(mappings[acc][self.tabletype]['AuditDim']))
                    self.setItem(row, 6, QTableWidgetItem(mappings[acc][self.tabletype]['RelPartDisc']))
                    self.setItem(row, 7, QTableWidgetItem(mappings[acc][self.tabletype]['CostCenterDisc']))
                    self.setItem(row, 8, QTableWidgetItem(mappings[acc][self.tabletype]['CustomType']))
                    if row <= self.rowCount():
                        row += 1
                    else:
                        break
