import os
import signal

from rich.console import Console
from rich.prompt import Prompt

from board import Board
from helper import A, B, C


TIME_LIMIT = 3


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def timer(signum, frame):
    raise Exception("Time's up!")


def timed_round():
    board = Board()

    signal.alarm(60 * TIME_LIMIT)

    msg = ""
    while True:
        try:
            clear()
            board.display()
            if msg:
                console.print(f"  {msg}  ", end="", style="dark_red on white")
            console.print("\nGuess a word: ", end="", style="bold orange4")
            guess = input().upper().strip().replace("QU", "Q")
            msg = board.guess(guess)
        except Exception as exc:
            console.print(exc, style="bold white on dark_red")
            console.print("Your final score was ", style="navajo_white1", end="")
            console.print(f" {board.score} ", style="bold white on dark_red")
            break


signal.signal(signal.SIGALRM, timer)
console = Console()

clear()
console.print(A, style="bold navajo_white1")
console.print(B, style="bold orange4")
console.print(C, style="bold red")

while True:
    log = Prompt.ask("\nWhat do you want to do?", choices=["start", "quit"])
    if log == "quit":
        console.print("[magenta]Goodbye\n")
        break
    if log == "start":
        timed_round()
