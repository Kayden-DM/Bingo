Bingo
A GUI Python game built with CustomTkinter where the player gets 5 random numbers and draws numbers one at a time, trying to mark all of theirs in as few draws as possible.

Concepts Used
Sets — marked and all_drawn track drawn numbers efficiently and prevent repeats.

Grid Layout — board_frame uses math.ceil(math.sqrt(...)) to build a roughly square button grid.

Widget Rebuilding — build_board() destroys and regenerates buttons on reset, stored in a board dict for lookup.

Features
Random Player Board — 5 unique numbers from 1–99 are chosen via random.sample.

Draw & Mark System — each draw is checked against the player's numbers, turning matches green.

Win Detection & Counter — when all numbers are marked, the game ends and reports how many draws it took.

Improvements
Rename numbers() — the function shadows the concept and reads oddly (numbers(5)); a name like pick_numbers() is clearer.

Show Full Draw History — only the latest draw is displayed; a scrolling list of past draws would make the game easier to follow.

Disable on Empty Pool — when all numbers are drawn, the message shows but draw_btn stays enabled; disable it alongside the win state.
