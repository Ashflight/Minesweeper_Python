from PyQt6.QtWidgets import QLabel, QMainWindow

## creates game at desired difficulty level to let player play
def create_game_screen(mainWindow : QMainWindow):
    ## placeholder screen
    placeholder = QLabel("PLACEHOLDER")
    mainWindow.setCentralWidget(placeholder)

    ## set up boards first
    ## creates digging/flagging toggle
    ## set up display, click display to dig or flag