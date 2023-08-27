from random import choice, randint
import numpy as np

class Board:
    def __init__(self):
        self.letters = "".join(Board.letter_gen())

    @staticmethod
    def letter_gen():
        DICE = [
            "RIFOBX", "IFEHEY", "DENOWS", "UTOKND", "HMSRAO", "LUPETS", "ACITOA", "YLGKUE",
            "QBMJOA", "EHISPN", "VETIGN", "BALIYT", "EZAVND", "RALESC", "UWILRG", "PACEMD"
        ]
        while DICE:
            die = DICE.pop(randint(0, len(DICE) - 1))
            yield choice(die)

    def get_matrix(self):
        matrix = np.array(list(self.letters), dtype=str)
        return matrix.reshape((4,4))
        
    def __str__(self):
        letters = "  ".join(list(self.letters)) + "  "
        return "\n".join(letters[xi: xi+12] for xi in range(0, len(letters), 12)).replace("Q ", "Qu")
    