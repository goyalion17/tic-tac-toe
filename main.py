import random


# 1. Поле 3x3, яке малюється текстом після кожного ходу.
def print_board(board):
    for i in range(0, 9, 3):
        print(" " + " | ".join(board[i:i+3]) + " ")
        if i < 6:
            print("---+---+---")

# 2. Два гравці (X і O) по черзі вводять номер клітинки (1-9).
def ask_move(board, player):
    while True:
        # 3. Перевірка ходу: клітинка має бути вільною, а введення коректним
        #    (не буква, не число поза діапазоном).
        text = input(f"Хід гравця {player}. Введи номер клітинки (1-9): ")
        try:
            number = int(text)
        except ValueError:
            print("Некоректне введення. Введи число від 1 до 9.")
            continue

        if not 1 <= number <= 9:
            print("Некоректне введення. Введи число від 1 до 9.")
        elif board[number - 1] in ["X", "O"]:
            print("Ця клітинка вже зайнята. Спробуй ще раз.")
        else:
            return number - 1

# 4. Перевірка перемоги: 3 в ряд по горизонталі, вертикалі або діагоналі.
def check_winner(board):
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    for combo in winning_combinations:
        a, b, c = combo
        if board[a] == board[b] == board[c] and board[a] in ["X", "O"]:
            return board[a]
    return None

# 5. Нічия, якщо поле заповнене, а переможця немає.
def is_draw(board):
    return all(cell in ["X", "O"] for cell in board)


# Необов'язково: гра проти комп'ютера з випадковими ходами.
def computer_move(board):
    free_cells = [i for i, cell in enumerate(board) if cell not in ["X", "O"]]
    return random.choice(free_cells)


def play_game(vs_computer=False):
    board = [str(i) for i in range(1, 10)]
    current_player = "X"

    while True:
        print_board(board)
        if vs_computer and current_player == "O":
            move = computer_move(board)
            print(f"Комп'ютер ходить у клітинку {move + 1}.")
        else:
            move = ask_move(board, current_player)
        board[move] = current_player

        winner = check_winner(board)
        if winner:
            print_board(board)
            print(f"Гравець {winner} переміг!")
            break
        elif is_draw(board):
            print_board(board)
            print("Нічия!")
            break

        current_player = "O" if current_player == "X" else "X"

# 6. Кінець гри з повідомленням і пропозицією зіграти ще раз.
def main():
    while True:
        mode = input("Грати проти комп'ютера? (y/n): ").strip().lower()
        play_game(vs_computer=(mode == 'y'))
        again = input("Хочеш зіграти ще раз? (y/n): ").strip().lower()
        if again != 'y':
            print("Дякую за гру!")
            break

if __name__ == "__main__":
    main()