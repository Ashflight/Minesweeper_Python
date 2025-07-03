from game import create_game_screen

from PyQt6.QtCore import Qt, QSize
from PyQt6.QtWidgets import QLabel, QMainWindow, QPushButton, QVBoxLayout, QWidget

## explains instructions and lets player select difficulty mode
def create_start_screen(mainWindow : QMainWindow):
    layout = QVBoxLayout()

    title = QLabel("MINESWEEPER")
    font = title.font()
    font.setPointSize(50)
    title.setFont(font)
    title.setAlignment(Qt.AlignmentFlag.AlignHCenter)
    title.setFixedHeight(100)
    layout.addWidget(title)

    instructions = QLabel("Pick a difficulty setting.")
    font2 = instructions.font()
    font2.setPointSize(15)
    instructions.setFont(font2)
    instructions.setFixedHeight(30)
    layout.addWidget(instructions)

    difficulties = ["Easy", "Medium", "Hard", "Very Hard"]
    for i in range(4):
        button = QPushButton(difficulties[i])
        button.setObjectName(difficulties[i])
        buttonFont = button.font()
        buttonFont.setPointSize(15)
        button.setFont(buttonFont)
        button.setFixedSize(QSize(150, 75))
        button.clicked.connect(lambda _, b=button: difficulty_selected(b, mainWindow))
        layout.addWidget(button, alignment=Qt.AlignmentFlag.AlignHCenter)

    widget = QWidget()
    widget.setLayout(layout)
    mainWindow.setCentralWidget(widget)


def difficulty_selected(button : QPushButton, mainWindow : QMainWindow):
    mineCounts = {"Easy" : 20,
                  "Medium" : 30,
                  "Hard" : 40,
                  "Very Hard" : 50}
    mainWindow.mineCount = mineCounts[button.objectName()]
    create_game_screen(mainWindow)