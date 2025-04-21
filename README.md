# Wordle and Wordle Solve Assist

Python 3.13 recreation of the game wordle, along with a solve assist that can efficiently filter out words from the `allwords.txt` file. The solve assist gets heavy help from Zulkarnine Mahmud's [WordleSolver](https://github.com/zulkarnine/WordleSolver).

## Functions

With this repository, you can do the following:

1. **Play the infamous Wordle game**: You can simply fork this repository and play it locally on your device.
2. **Cheat**: If you give up and want to quickly solve the word, you can open up `wordlesolveassist\main.py` and just tell it what your guess or guesses were, and below your guess simply input something like `gbbyb`, where "G" stands for green correct, "Y" stands for yellow or partially correct and "B" means blank, or in other words, wrong. Bear in mind, it doesn't matter whether it's in uppercase or lowercase.

## How to Use

1. Run the program in a Python environment.
2. Follow the screen prompts.
3. Have fun!

## Packages

1. Python 3 (doesn't matter what version)
2. `enum` module. (Built-in, don't worry)

## Example Usage

### Playing Wordle

1. Run the Wordle game:
   ```bash
   python wordleplay/wordle.py
   New game begun.
   enter your guess: apple
   Feedback: 🟩 🟥 🟥 🟩 🟩
   attempts remaining: 5
   enter your guess: angel
   Feedback: 🟩 🟩 🟩 🟨 🟨
   attempts remaining: 4
   enter your guess: angle
   ok u win. word was angle
   ```
