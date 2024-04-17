import numpy as np

from rich.console import Console
from rich.columns import Columns
from rich.style import Style
from rich.table import Table

from helper import is_valid, letter_gen


class Board:
    def __init__(self):
        self.letters = np.array([*letter_gen()], dtype="<U2").reshape(4, 4)
        self.word_list = []
        self.score = 0

        # Display
        self.style = Style(color="black", bgcolor="navajo_white1", bold=1)
        self.buttons = {
            "justify": "center",
            "width": 3,
            "style": self.style,
            "vertical": "middle",
        }
        self.frame = {
            "show_lines": 1,
            "border_style": "orange4",
            "header_style": Style(color="dark_red", bgcolor="navajo_white1", bold=1),
            "width": 80,
        }
        self.table = {
            "show_header": 0,
            "show_lines": 1,
            "padding": (1, 2),
            "border_style": "black",
        }
        self.results = {
            "show_header": 0,
            "show_lines": 0,
            "border_style": "navajo_white1",
        }
        self.console = Console(color_system="truecolor")

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
        fixed_word = word.replace("Q", "QU").title()
        if len(word) < 3:
            return "Words must be at least 3 letters long."
        if fixed_word.lower() in self.word_list:
            return f"You already have {fixed_word}."

        message = ""
        if not self.on_board(word):
            message += f"{fixed_word} is not on the board. "
        if not is_valid(word):
            message += f"{fixed_word} is not a word."
        if not message:
            self.add_word(word)
        return message.strip() or f"Nice! ({fixed_word})"

    def add_word(self, word):
        word = word.replace("Q", "QU")
        self.word_list.append(word.lower())
        word_length = len(word)
        self.score += (
            (word_length == 7) + max(1, word_length - 3) if word_length < 8 else 11
        )

    def display(self):
        letters = np.where(self.letters == "Q", "Qu", self.letters)

        outer_table = Table(**self.frame)
        for s, style in zip(("BOGGLE", "Words Found:"), ("", "on navajo_white1")):
            outer_table.add_column(s, justify="center", style=style)

        table = Table(**self.table)
        for _ in range(4):
            table.add_column("   ", **self.buttons)
        for row in letters:
            table.add_row(*row)

        cols = Table(**self.results, expand=1)
        cols.add_column(" ")
        cols.add_row(
            Columns(self.word_list + ["", "", "", ""], equal=True, expand=True),
            style="black",
        )
        cols.add_section()
        cols.add_row(f"Score: {self.score}", style="white on dark_red")

        outer_table.add_row(table, cols)
        self.console.print(outer_table)
