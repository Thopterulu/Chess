from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtCore import Qt

class board(QWidget):
    def draw_board(self):
        pass

    def white_case(self, event, x: int, y: int):
        painter = QPainter(self) # recupere le QPainter du widget
        painter.setPen(Qt.red) # add a red pen
        painter.setBrush(Qt.lightGray) # set a light gray brush
        painter.drawRect(x,y,120,40) # dessine le rectangle

    def brown_case(self, x: int, y: int):
        painter = QPainter(self) # recupere le QPainter du widget
        painter.setPen(Qt.red) # add a red pen
        painter.setBrush(Qt.lightGray) # set a light gray brush
        painter.drawRect(x,y,120,40) # dessine le rectangle
