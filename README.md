# Tic Tac Toe

A text-based Tic Tac Toe game for the terminal, written in **Python** (no external libraries).
Built as the Day 84 project of the *100 Days of Code: The Complete Python Pro Bootcamp*.

## Features

- 3×3 board drawn in the terminal after every move
- Two players (X and O) or play against the computer, which picks random free cells
- Input validation: letters, numbers out of range and occupied cells are rejected without crashing
- Win detection (rows, columns, diagonals) and draw detection
- Option to play again

## Run

```bash
python3 main.py
```

Requires Python 3.8+.

## Example

```
1 | 2 | 3
---+---+---
4 | 5 | 6
---+---+---
7 | 8 | 9
Player X, enter a cell number (1-9):
```

## Structure

| Function | Purpose |
|---|---|
| `print_board(board)` | Draws the board |
| `ask_move(board, player)` | Asks for a move and validates it |
| `computer_move(board)` | Picks a random free cell |
| `check_winner(board)` | Returns `"X"`, `"O"` or `None` |
| `is_draw(board)` | Checks whether the board is full |
| `play_game(vs_computer)` | One full game |
| `main()` | Starts games until the player quits |
