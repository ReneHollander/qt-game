"""
Created on 21.12.2015

:author: Rene Hollander
"""

import sys
import time as time_

from PySide.QtCore import Qt
from PySide.QtGui import *

from game.MainWindowModel import MainWindowModel
from game.MainWindowView import Ui_MainWindow
from random import shuffle


def millis():
    """
    Get the current time in milliseconds since epoch

    :return: Current time in milliseconds since epoch
    :rtype: int
    """

    return int(round(time_.time() * 1000))


class MainWindowController(QMainWindow):
    """
    Controller for the MainWindow
    """

    def __init__(self, parent=None):
        """
        Creates a new Controller for the MainWindow

        :param parent: Parent
        """

        super().__init__(parent)
        self.view = Ui_MainWindow()
        self.view.setupUi(self)

        # Iterate all game buttons defined in the view
        self.buttons = []
        for key in self.view.__dict__:
            if key.startswith('button_order_'):
                button = self.view.__dict__[key]
                # Add the button to the list of buttons
                self.buttons.append(button)
                # register the signal handler for the current button
                button.clicked.connect(self.button_click_callback)

        self.model = MainWindowModel(len(self.buttons))

        self.start_time = -1

        # Start the first game
        self.new_game()

    def update_labels(self):
        """
        Update the labels that display the game state
        """

        self.view.label_correct.setText(str(self.model.correct))
        self.view.label_open.setText(str(self.model.open))
        self.view.label_total.setText(str(self.model.total))
        self.view.label_games.setText(str(self.model.games))
        self.view.label_wrong.setText(str(self.model.wrong))

    def new_game(self):
        """
        Starts a new game
        """

        self.model.games += 1
        self.update_labels()

        self.enable_buttons()
        self.randomize_buttons()

    def button_click_callback(self):
        """
        Callback for the buttons with numbers on them
        """

        sender = self.sender()
        if type(sender) == QPushButton:

            if self.start_time == -1:
                self.start_time = millis()

            value = int(sender.text())
            # check if the current number matches the text of the button
            if value == self.model.current:
                self.model.correct_guess()
                sender.setEnabled(False)
            else:
                self.model.wrong_guess()

            self.update_labels()
        else:
            raise RuntimeError("Invalid sender type triggered event: " + type(sender))

        # if there are no open fields anymore, the game is won
        if self.model.open == 0:
            self.win()

    def randomize_buttons(self):
        """
        Randomize the order of the buttons
        """

        # reset the current values
        self.model.reset()
        # randomize the sequence of the buttons
        shuffle(self.buttons)

        # set the text of the buttons in ascending order
        number = 1
        for button in self.buttons:
            button.setText(str(number))
            number += 1

        self.update_labels()

    def enable_buttons(self):
        """
        Reenable all buttons
        """

        for button in self.buttons:
            button.setEnabled(True)

    def win(self):
        """
        Triggered when the game is won
        """

        diff = (millis() - self.start_time) / 1000.0
        self.start_time = -1

        q = QMessageBox()
        q.setWindowTitle("Gewonnen!")
        q.setTextFormat(Qt.RichText)
        q.setText("Benötigte Schritte: " + str(self.model.total) + "<br />Benötigte Zeit: " + str(diff) + "s")
        q.exec()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    c = MainWindowController()
    c.show()
    sys.exit(app.exec_())
