import numpy as np

from rich.console import Console
from rich.style import Style
from rich.table import Table

from helper import is_valid, letter_gen


class Board:
    def __init__(self):
        self.letters = np.array([*letter_gen()], dtype="<U2").reshape(4, 4)

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

    def guess(self, word):
        if len(word) < 3:
            return False, "Words must be at least 3 letters long."
        A, B = self.on_board(word), is_valid(word)
        msg = (
            f"{(word.title() + ' is not on the board. ')*(not A)}{(word.title() + ' is not a word. ')*(not B)}"
            or f"Nice! ({word.title()})"
        )
        return A and B, msg

    def display(self):
        letters = np.where(self.letters == "Q", "Qu", self.letters)

        table = Table(**self.table)
        for _ in range(4):
            table.add_column("   ", **self.buttons)
        for row in letters:
            table.add_row(*row)
        self.console.print(table)
