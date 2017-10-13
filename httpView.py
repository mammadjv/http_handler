import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtCore import pyqtSignal
from networkManager import NetManager
import json


class HttpView(QWidget):

    send_signal = pyqtSignal(str,str)
    def __init__(self):
        super().__init__()
        self.title = 'HttpHandler'
        self.left = 200
        self.top = 50
        self.width = 800
        self.height = 700
        self.url_line = QLineEdit(self)
        self.submit_button = QPushButton(self)
        self.text_area = QTextEdit(self)
        self.netManager = NetManager()
        self.netManager.packet_received.connect(self.on_packet_received)

        self.send_signal.connect(self.netManager.on_url_clicked)

        self.initUI()

    @pyqtSlot()
    def on_clicked(self):
        if self.url_line.text() == "":
            print('url_line is empty!')
            return
        self.text_area.setText("")
        self.send_signal.emit(self.url_line.text(), 'OPTIONS')
        self.send_signal.emit(self.url_line.text(), 'GET')

    @pyqtSlot(str , str)
    def on_packet_received(self, resp, content):
        resp = resp[1:len(resp)-1]
        header_list = resp.split("', ")
        header_show = ""
        for header in header_list:
            header_show = header_show + header + '\n\n'
        header_show = header_show + self.text_area.toPlainText()
        self.text_area.setText(header_show)

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.url_line.setText("http://www.varzesh3.com/")
        self.url_line.setGeometry(self.width/10, self.height/10, 7*self.width/10, self.height/20)

        self.submit_button.setGeometry(82*self.width/100, self.height/10, self.width/10, self.width/20)

        self.text_area.setGeometry(self.width/10, 2*self.height/10, 8*self.width/10, 7*self.height/10)
        self.text_area.setReadOnly(True)
        self.submit_button.clicked.connect(self.on_clicked)
        self.submit_button.setText('submit!')
        self.show()