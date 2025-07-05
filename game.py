from random import randint

from PyQt6.QtCore import Qt, QSize
from PyQt6.QtWidgets import QGridLayout, QLabel, QMainWindow, QPushButton, QVBoxLayout, QWidget

## creates game at desired difficulty level to let player play
def create_game_screen(mainWindow : QMainWindow):
    ## set up mineBoard first
    index = 0
    while (index < mainWindow.mineCount):
        y = randint(0, 9)
        x = randint(0, 9)
        if (mainWindow.mineBoard[y][x] == False): 
            mainWindow.mineBoard[y][x] = True
            index += 1
    ## set up numberBoard
    for i in range(10):
        for j in range(10):
            counter = 0 
            for a in range(-1, 2):
                for b in range(-1, 2):
                    if (i + a < 0 or i + a > 9 or j + b < 0 or j + b > 9 or (a == 0 and b == 0)):
                        continue
                    elif (mainWindow.mineBoard[i + a][j + b] == True):
                        counter += 1
            mainWindow.numberBoard[i][j] = counter
    ## creates digging/flagging toggle
    layout = QVBoxLayout()
    mainWindow.actionToggle = QPushButton("Current Mode: Digging")
    mainWindow.actionToggle.setCheckable(True)
    mainWindow.actionToggle.clicked.connect(lambda: action_toggled(mainWindow))
    layout.addWidget(mainWindow.actionToggle)
    ## set up display, click display to dig or flag
    displayLayout = QGridLayout()
    for i in range(10):
        for j in range(10):
            button = QPushButton()
            button.setFixedSize(QSize(50, 50))
            button.setObjectName(str(i) + str(j))
            button.clicked.connect(lambda _, b=button: grid_clicked(b, mainWindow))
            displayLayout.addWidget(button, i, j)
    mainWindow.display.setLayout(displayLayout)
    mainWindow.display.setFixedSize(QSize(500, 500))
    layout.addWidget(mainWindow.display)
    widget = QWidget()
    widget.setLayout(layout)
    mainWindow.setCentralWidget(widget)

def action_toggled(mainWindow : QMainWindow):
    mainWindow.flaggingOn = not mainWindow.flaggingOn
    if (mainWindow.flaggingOn):
        mainWindow.actionToggle.setText("Current Mode: Flagging")
    else:
        mainWindow.actionToggle.setText("Current Mode: Digging")

def grid_clicked(button : QPushButton, mainWindow : QMainWindow):
    coordstr = button.objectName()
    y = int(coordstr[0:1])
    x = int(coordstr[1:2])
    if(mainWindow.flaggingOn):
        flag(mainWindow.display, y, x)
    elif (mainWindow.mineBoard[y][x]):
        mainWindow.setCentralWidget(QLabel("YOU LOST"))
        ## TODO: add a screen freeze, don't just delete the entire screen upon the game ending. 
        ## TODO: add a win checker. the checkedBoard should make it reasonably feasible. 
    else: 
        dig(mainWindow, y, x)

def flag(display : QWidget, y, x):
    layout = display.layout()
    if (not isinstance(layout, QGridLayout)):
        return
    button = layout.itemAtPosition(y, x)
    button = button.widget()
    if (not isinstance(button, QPushButton)):
        return
    if (button.text() == "|>"):
        button.setText("")
    else: 
        button.setText("|>")

def dig(mainWindow, y, x):
    layout = mainWindow.display.layout()
    if (not isinstance(layout, QGridLayout)):
        return
    for i in range(-1, 2):
        for j in range(-1, 2):
            if (y + i < 0 or y + i > 9 or x + j < 0 or x + j > 9):
                continue
            elif (not (mainWindow.checkedBoard[y + i][x + j] or mainWindow.mineBoard[y + i][x + j])):
                mainWindow.checkedBoard[y + i][x + j] = True
                if (mainWindow.numberBoard[y + i][x + j] == 0):
                    label = QLabel()
                    label.setFixedSize(QSize(50, 50))
                    dig(mainWindow, y + i, x + j)
                else: 
                    label = QLabel(str(mainWindow.numberBoard[y + i][x + j]))
                    label.setFixedSize(QSize(50, 50))
                    font = label.font()
                    font.setPointSize(30)
                    label.setFont(font)
                    label.setAlignment(Qt.AlignmentFlag.AlignCenter)
                oldWidget = layout.itemAtPosition(y + i, x + j)
                oldWidget = oldWidget.widget()
                layout.removeWidget(oldWidget)
                layout.addWidget(label, y + i, x + j)
                oldWidget.deleteLater()