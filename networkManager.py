from httplib2 import Http
from PyQt5.QtCore import QObject
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtCore import pyqtSignal
import validators as validator
import re


class NetManager(QObject):

    packet_received = pyqtSignal(str,str)
    def __init__(self):
        super().__init__()
        self.httpConnection = Http(disable_ssl_certificate_validation=True)

    @pyqtSlot(str,str)
    def on_url_clicked(self, url, method):
        print(url)
        resp, content = self.httpConnection.request(uri=url,method=method)
        print(resp , content)
        self.packet_received.emit(str(resp),str(content))