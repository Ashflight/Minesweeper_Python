from PyQt6.QtCore import Qt, QSize
from PyQt6.QtWidgets import QLabel, QMainWindow, QPushButton, QVBoxLayout

## explains instructions and lets player select difficulty mode
def create_start_screen(mainWindow : QMainWindow):
    layout = QVBoxLayout()

    title = QLabel("MINESWEEPER")
    font = title.font()
    font.setPointSize(50)
    title.setFont(font)
    title.setAlignment(Qt.AlignmentFlag.AlignHCenter)
    layout.addWidget(title)

    instructions = QLabel("Pick a difficulty setting.")
    layout.addWidget(instructions)

    difficulties = ["Easy", "Medium", "Hard"]
    for i in range(3):
        button = QPushButton(difficulties[i])
        button.setFixedSize(QSize(100, 50))
        button.clicked.connect(lambda: difficulty_selected(button, mainWindow))


def difficulty_selected(button : QPushButton, mainWindow : QMainWindow)