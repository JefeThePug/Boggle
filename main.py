import os
import signal

from board import Board


TIME_LIMIT = 3


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def timer(signum, frame):
    raise Exception("Timeout!")


def timed_round(n):
    board = Board()
    signal.alarm(60 * TIME_LIMIT)

    msg = ""
    while True:
        try:
            clear()
            board.display()
            print(msg)
            guess = input("Guess a word: ").upper().strip().replace("QU", "Q")
            guess, msg = board.guess(guess)
            if guess:
                pass
            n += 1
        except Exception as exc:
            print(exc)
            break


signal.signal(signal.SIGALRM, timer)

print("Boggle!")

while True:
    log = input("What do you want to do? (start/quit): ").lower().strip()
    if log == "quit":
        print("Goodbye")
        break
    if log == "start":
        timed_round(0)
