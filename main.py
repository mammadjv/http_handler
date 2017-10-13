from PyQt5.QtWidgets import QApplication
import httpView
import sys

app = QApplication(sys.argv)
ex = httpView.HttpView()
sys.exit(app.exec())