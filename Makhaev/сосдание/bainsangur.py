
from PyQt5.QtCore import Qt 
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QLabel
from PyQt5.QtGui import QFont 

app = QApplication([])
window = QWidget()
window.resize(500, 500)
window.move(200,200)
window.setWindowTitle('Я сила!')


 
line1 = QHBoxLayout()
line2 = QHBoxLayout()
line3 = QHBoxLayout()
line1.addWidget("That?", alignment=Qt.AlignCenter)
line2.addWidget("02,07,2006", alignment=Qt.AlignCenter)
line2.addWidget('Байсангур занимаеться бизнес', alignment=Qt.AlignCenter)

window.show()
app.exec_()