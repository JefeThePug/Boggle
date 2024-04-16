import numpy as np

from random import choice, randint
from rich.console import Console
from rich.style import Style
from rich.table import Table


class Board:
    def __init__(self):
        self.letters = np.array([*Board.letter_gen()], dtype="<U2").reshape(4, 4)

        # Display
        self.style = Style(color="black", bgcolor="navajo_white1", bold=1)
        self.buttons = {
            "justify": "center",
            "width": 3,
            "style": self.style,
            "vertical": "middle",
        }
        self.table = {
            "show_header": 0,
            "show_lines": 1,
            "padding": (1, 2),
            "border_style": "black",
        }
        self.console = Console()

    @staticmethod
    def letter_gen():
        DICE = [
            "RIFOBX", "IFEHEY", "DENOWS", "UTOKND",
            "HMSRAO", "LUPETS", "ACITOA", "YLGKUE",
            "QBMJOA", "EHISPN", "VETIGN", "BALIYT",
            "EZAVND", "RALESC", "UWILRG", "PACEMD",
        ]
        while DICE:
            die = DICE.pop(randint(0, len(DICE) - 1))
            yield choice(die)

    def is_adjacent(self, word, used, row, col, i):
        if i == len(word):
            return True
        used[row, col] = True
        for dr in range(-1, 2):
            for dc in range(-1, 2):
                if dr == 0 == dc:
                    continue
                r, c = row + dr, col + dc
                if (
                    r in range(4)
                    and c in range(4)
                    and not used[r, c]
                    and self.letters[r, c] == word[i]
                ):
                    if self.is_adjacent(word, used, r, c, i + 1):
                        return True
                    used[r, c] = False
        return False

    def on_board(self, word):
        for r in range(4):
            for c in range(4):
                if self.letters[r, c] == word[0]:
                    if self.is_adjacent(word, np.zeros((4, 4), dtype=bool), r, c, 1):
                        return True
        return False

    def is_word(self, word):
        #! coming soon
        return True

    def guess(self, word):
        if len(word) < 3:
            return False
        return self.on_board(word) and self.is_word(word)

    def display(self):
        letters = np.where(self.letters == "Q", "Qu", self.letters)
        table = Table(**self.table)
        for _ in range(4):
            table.add_column("   ", **self.buttons)
        for row in letters:
            table.add_row(*row)
        self.console.print(table)
