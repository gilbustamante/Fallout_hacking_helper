# Fallout Hacking Helper (FHH)
FHH helps make the "hacking" minigame in modern
[Fallout](https://en.wikipedia.org/wiki/Fallout_(series)) games easier.

## Requirements
* Python 3 or later

## Usage
```
python main.py
```
1. Enter each word from the in-game terminal. Enter an empty string to finish.
2. Pick a word in the game and enter it when prompted, along with how many
characters the game says are correct.
3. FHH will filter out any incompatible words and return a list of potentially
correct answers.
4. Repeat until you find the correct word.

The program isn't perfect (meaning you will sometimes run out of "guesses" if
you have bad luck choosing a word), but in my experience it has a pretty good
success rate.

## To Do
* Have the program suggest the next word to use.
* Maybe implement `PyTesseract` to read the words from a screenshot, eliminating
the need to enter them manually.
