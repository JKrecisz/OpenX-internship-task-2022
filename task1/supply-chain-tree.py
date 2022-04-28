"""
--------------------------------------------------------------------------------
    The program present whole Supply Chain tree for OpenX in an easy to read way
--------------------------------------------------------------------------------
    Autor: Jakub Krecisz                                      Krakow, 27.04.2022
--------------------------------------------------------------------------------
"""

import sys
import json
from urllib.request import urlopen
from PyQt5.QtWidgets import QApplication, QMainWindow, QTreeView
from PyQt5.Qt import QStandardItemModel, QStandardItem
from PyQt5.QtGui import QFont, QColor


class StandardItem(QStandardItem):
    def __init__(self, txt='', font_size=12, set_bold=False, color=QColor(0, 0, 0)):
        super().__init__()
        font = QFont('Open Sans', font_size)
        font.setBold(set_bold)

        self.setEditable(False)
        self.setForeground(color)
        self.setFont(font)
        self.setText(txt)


class AppDemo(QMainWindow):
    def __init__(self, jsonData):
        super().__init__()
        self.setWindowTitle('OpenX supply chain tree')
        self.resize(500, 700)

        treeView = QTreeView()
        treeView.setHeaderHidden(True)

        treeModel = QStandardItemModel()
        rootNode = treeModel.invisibleRootItem()

        for seller in jsonData["sellers"]:
            rootNode.appendRow(StandardItem(seller["name"], 16))

        treeView.setModel(treeModel)
        treeView.expandAll()
        self.setCentralWidget(treeView)


if __name__ == '__main__':
    file = urlopen("https://openx.com/sellers.json")
    jData = json.load(file)

    app = QApplication(sys.argv)
    demo = AppDemo(jData)
    demo.show()
    sys.exit(app.exec_())
