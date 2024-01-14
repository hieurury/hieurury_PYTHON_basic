# PyQt6
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
import tkinter as tk
import random


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('My PyQt6 App')
        self.setGeometry(0, 100, 400, 300)

        layout = QVBoxLayout(self)
        button = QPushButton('first button', self)
        button.setMouseTracking(True)
        buttonSecond = QPushButton('second button', self)
        button.enterEvent = self.on_button_click
        buttonSecond.clicked.connect(self.message)
        
        button.setFixedSize(200, 50)
        button.setStyleSheet("background-color: #0005; color: #fff")
        button.move(400, 50)
        layout.addWidget(button)
        layout.addWidget(buttonSecond)

    def on_button_click(self, event):
        main = self.geometry()
        width = main.width()
        height = main.height()
        randX = random.randint(0, 1100)
        randY = random.randint(0, 480)
        currentPosX = self.x()
        currentPosY = self.y()
        print(randX, randY)
        self.move(randX, randY)
        
    def message(self):
        currentPos = self.pos()
        print(currentPos)



if __name__ == '__main__':
    app = QApplication([])
    widget = MyWidget()
    widget.show()
    app.exec()

