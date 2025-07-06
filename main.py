import sys
from start_screen import create_start_screen
from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Minesweeper")
        self.setFixedSize(QSize(600, 600))

        ## mineBoard: true for mine, false for no mine
        self.mineBoard = [[False for i in range(10)] for j in range(10)]
        ## numberBoard: board of numbers of adjacent mines (ie numbers displayed to player), 9 = is mine
        self.numberBoard = [[0 for i in range(10)] for j in range(10)]
        ## number of mines for this game. create different difficulty levels?
        self.mineCount = 0
        ## checkedBoard: true for revealed, false for unknown, keeps track of which squares have been checked
        self.checkedBoard = [[False for i in range(10)] for j in range(10)]
        self.actionToggle = QPushButton()
        self.display = QWidget()
        self.flaggingOn = False

if (__name__ == '__main__'):
    app = QApplication(sys.argv)

    window = MainWindow()
    create_start_screen(window)
    window.show()

    app.exec()