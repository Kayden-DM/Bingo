## Bingo
A desktop bingo game built with CustomTkinter. It draws random numbers from 1 to 99, highlights any that match the player's five numbers, and tracks how many draws it takes to mark them all.

## Features
Random Board — Generates five unique player numbers from 1 to 99 using random.sample().

Grid Layout — Arranges the player's numbers in a square grid sized with math.ceil(math.sqrt(...)).

Draw Numbers — Picks a random undrawn number each click and shows it in the history label.

Auto-Marking — Turns matching player numbers light green and adds them to the marked set.

Progress Counter — Displays how many numbers have been marked out of the total.

Win Detection — Ends the game and disables the Draw button when all player numbers are marked, showing the total draws taken.

Reset — Regenerates the board and clears all state for a fresh game.

Exhausted Pool — Prints "All numbers drawn!" if every number from 1 to 99 has been drawn.

## Technologies Used
text
| Technology | Purpose |
|---|---|
| Python | Application logic |
| `customtkinter` | Desktop GUI |
| `random.sample()` | Generates unique player numbers |
| `random.choice()` | Draws a random remaining number |
| `math.ceil()` / `math.sqrt()` | Calculates grid columns |
| `set` | Tracks marked and drawn numbers efficiently |
| `global` | Updates game state across functions |
| `.grid()` | Positions board buttons in a grid |
<!-- -->
## How to Use It
Install Python 3.6 or newer from python.org and make sure it's added to your PATH.

Install CustomTkinter by running pip install customtkinter.

Save the code as bingo.py.

Open a terminal in the folder containing the file.

Run python bingo.py.

Click Draw repeatedly until all five of your numbers are marked; use Reset to start a new game.

## Improvements
Show all drawn numbers — the history label only shows the most recent draw, so players can't see which numbers have already come up; keeping a list of drawn numbers and displaying them would make the game easier to follow.

Add a board size option — the number of player numbers is hardcoded to 5 in reset(); letting the player choose (e.g. 3, 5, or 10) would add variety without much extra code.
