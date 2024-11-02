# Boggle Game

A terminal-based Boggle game implemented in Python, featuring a 4x4 board where players attempt to find as many valid words as possible within a set time limit. Enhanced with rich for colorful and structured console output, this game includes real-time scoring and validation of guesses.

## Features

- **Timer**: Each game round is timed (default is 3 minutes).
- **Interactive Console UI**: Enhanced console output and prompts using the rich library.
- **Scoring System**: Words entered by the player are validated using an online dictionary API, and scores are updated after each successful guess.

  - **Scoring**
    ```
    - 3 or 4 letter words - 1 point
    - 5 letter words - 2 points
    - 6 letter words - 3 points
    - 7 letter words - 5 points
    - 8+ letter words - 11 points
    ```
- **Realistic Boggle Board**: Letters are generated based on standard Boggle dice.

## Prerequisites

- Python 3.7+
- rich, numpy, and requests libraries:

  ```bash
  pip install rich requests numpy
  ```
  or
  ```bash
  pip install -r requirements.txt
  ```

## How to Play

1. **Run the game** by executing the script in a terminal. 
```bash
python main.py
```

2. **Choose an option** from the prompt:
   - **start**: Start a new Boggle round.
   - **quit**: Exit the game.

3. **Find words** on the displayed board:
   - Words must follow [Boggle rules](https://en.wikipedia.org/wiki/Boggle), connecting adjacent letters.
   - Type words in the console prompt and press Enter.

4. **End of Game**: When the timer expires, your final score is displayed.

## Code Overview

### main.py

- Manages game flow and handles player input.
- Includes timed_round for managing the round timer and clear for refreshing the console screen.
- Uses Console and Prompt from rich to stylize console interactions.

### board.py

- Defines the Board class to manage the board's setup, word-checking, and scoring.
- **Display**: Uses rich's Table and Columns to print the Boggle board and guessed words.
- **Game Logic**: 
  - guess(word): Checks if the word is on the board, valid, and not already guessed.
  - on_board(word): Verifies if a word can be formed on the board by connecting adjacent letters.
  - is_adjacent(word): Recursively checks if letters in the word connect according to Boggle rules.

### helper.py

- **is_valid(word)**: Calls an online dictionary API to validate words.
- **letter_gen()**: Generates a random selection of letters for the board, based on the typical distribution of letters on Boggle dice.

### Constants

The helper.py file includes ASCII art messages (A, B, and C) displayed at the start of the game.

## Customization

You can adjust the time limit by modifying the TIME_LIMIT variable in main.py:

```py
TIME_LIMIT = 3  # Default time in minutes
```

## Example

```bash
python main.py
```
```
[Boggle ASCII art]

What do you want to do? [start, quit]
$ start

[Board appears]

Guess a word: 
$ test

Nice! (test)
Guess a word:


Time's up!
Your final score was 1.
```

## License

This Boggle game implementation is open-source and available for personal or educational use.

## Author

Developed by JefeThePug.

---

Enjoy the challenge of finding words and beating your high score!
