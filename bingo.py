import tkinter as tk
import random
import math

player_numbers = []
marked = set()
all_drawn = set()
game_over = False
board = {}


def numbers(count):
    return random.sample(range(1, 100), count)


def build_board():
    for widget in board_frame.winfo_children():
        widget.destroy()
    board.clear()

    cols = math.ceil(math.sqrt(len(player_numbers)))
    for i, num in enumerate(player_numbers):
        row = i // cols
        col = i % cols
        btn = tk.Button(board_frame, text=str(num), font=("Arial", 18),
                        width=4, height=2)
        btn.grid(row=row, column=col, padx=3, pady=3)
        board[num] = btn


def update_status():
    status_label.configure(text=f"Marked {len(marked)} / {len(player_numbers)}")


def draw():
    global game_over
    if game_over:
        return

    remaining = [n for n in range(1, 100) if n not in all_drawn]
    if not remaining:
        history_label.configure(text="All numbers drawn!")
        return

    number = random.choice(remaining)
    all_drawn.add(number)
    history_label.configure(text=f"Drawn: {number}")

    if number in player_numbers:
        marked.add(number)
        board[number].configure(bg="lightgreen")

    update_status()

    if len(marked) == len(player_numbers):
        game_over = True
        status_label.configure(text=f"You win! It took {len(all_drawn)} draws.")
        draw_btn.configure(state="disabled")


def reset():
    global player_numbers, marked, all_drawn, game_over, board
    player_numbers = numbers(5)
    marked = set()
    all_drawn = set()
    game_over = False
    board = {}

    build_board()
    update_status()
    history_label.configure(text="Drawn: -")
    draw_btn.configure(state="normal")


root = tk.Tk()
root.title("Bingo")

board_frame = tk.Frame(root)
board_frame.pack(pady=20)

status_label = tk.Label(root, text="", font=("Arial", 14))
status_label.pack()

history_label = tk.Label(root, text="Drawn: -", font=("Arial", 14))
history_label.pack(pady=5)

draw_btn = tk.Button(root, text="Draw", font=("Arial", 16), width=12, command=draw)
draw_btn.pack(pady=10)

reset_btn = tk.Button(root, text="Reset", font=("Arial", 12), width=10, command=reset)
reset_btn.pack(pady=5)

reset()
root.mainloop()