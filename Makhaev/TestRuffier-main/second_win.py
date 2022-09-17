from instr import *
from final_win import *


from email.mime import application
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
        QApplication, QWidget, 
        QHBoxLayout, QVBoxLayout, 
        QGroupBox, QRadioButton,
        QPushButton, QLabel, QListWidget, QLineEdit)

class TestWin(QWidget):
    def __init__(self):
        ''' окно в котором проводится опрос '''
        super().__init__()

        # создаём и настраиваем графические эелементы:
        self.initUI()

        #устанавливает связи между элементами
        self.connects()

        #устанавливает, как будет выглядеть окно (надпись, размер, место)
        self.set_appear()
        
        # старт:
        self.show()

    def initUI(self):
        self.btn_next = QPushButton(txt_sendresults)
        self.btn_next1 = QPushButton(txt_starttest1)
        self.btn_next2 = QPushButton(txt_starttest2)
        self.btn_next3 = QPushButton(txt_starttest3)

        self.text_name = QLabel(txt_name)
        self.text_age = QLabel(txt_age)
        self.text_test1 = QLabel(txt_test1)
        self.text_test2 = QLabel(txt_test2)
        self.text_test3 = QLabel(txt_test3)
        self.text_timer = QLabel(txt_timer)
        self.line_name = QLineEdit(txt_hintname)
        self.line_age = QLineEdit(txt_hintage)
        self.line_test1 = QLineEdit(txt_hinttest1)
        self.line_test2 = QLineEdit(txt_hinttest2)
        self.line_test3 = QLineEdit(txt_hinttest3)
        
        self.r_line = QVBoxLayout()
        self.h_line = QVBoxLayout()
        self.r_line.addWidget(self.text_timer, alignment = Qt.AligCenter)
        self.l_line.addWidget(self.text_name, alignment = Qt.AligLeft)
        self.l_line.addWidget(self.line_name, alignment = Qt.AligLeft)
        self.l_line.addWidget(self.text_age, alignment = Qt.AligLeft)
        self.l_line.addWidget(self.line_age, alignment = Qt.AligLeft)
        self.l_line.addWidget(self.text_test1, alignment = Qt.AligLeft)
        self.l_line.addWidget(self.btn_test1, alignment = Qt.AligLeft)
        self.l_line.addWidget(self.line_test1, alignment = Qt.AligLeft)
        self.l_line.addWidget(self.text_test2, alignment = Qt.AligLeft)
        self.l_line.addWidget(self.line_test2, alignment = Qt.AligLeft)
        self.l_line.addWidget(self.btn_text2, alignment = Qt.AligLeft)
        self.l_line.addWidget(self.line_test3, alignment = Qt.AligLeft)
        self.l_line.addWidget(self.text_test3, alignment = Qt.AligLeft)
        self.l_line.addWidget(self.btn_test3, alignment = Qt.AligLeft)
        self.h_line.addLayout(self.l_line)
        self.h_line.addLayout(self.r_line)
        self.setLayout(self.h_line)
    def next_click(self):
        pass

    def connects(self):
        pass

    ''' устанавливает, как будет выглядеть окно (надпись, размер, место) '''
    def set_appear(self):
        pass 
