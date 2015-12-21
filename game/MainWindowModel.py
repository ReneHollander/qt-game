"""
Created on 21.12.2015

:author: Rene Hollander
"""


class MainWindowModel(object):
    """
    Model of the MainWindow

    :var amount: Amount of buttons
    :var games: Amount of games player
    :var open: Amount of numbers that still need guessing
    :var current: Number that is expected now
    :var correct: Amount of correct guesses
    :var wrong: Amount of wrong guesses
    :var total: Total number of guesses
    """

    def __init__(self, amount_buttons):
        """
        Creates a new Model for the GameWindow with the given amount of buttons

        :param amount_buttons: Amount of Buttons that can be ordered
        """

        self.amount = amount_buttons
        self.games = 0
        self.reset()

    def reset(self):
        """
        Reset the current game
        """

        self.open = self.amount
        self.current = 1
        self.correct = 0
        self.wrong = 0
        self.total = 0

    def correct_guess(self):
        """
        Adjusts scores when a correct ordering was done
        """

        self.current += 1
        self.correct += 1
        self.open -= 1
        self.total += 1

    def wrong_guess(self):
        """
        Adjusts scores when a false ordering was done
        """

        self.wrong += 1
        self.total += 1
