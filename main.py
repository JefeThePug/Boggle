from board import Board

board = Board()
board.display()

guess = input("Guess a word: ").upper().strip().replace("QU", "Q")
print(board.guess(guess))
