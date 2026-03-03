import random

board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]


def display_board():
    print("\n")
    print(board[0] + " | " + board[1] + " | " + board[2] + "   1 | 2 | 3")
    print(board[3] + " | " + board[4] + " | " + board[5] + "   4 | 5 | 6")
    print(board[6] + " | " + board[7] + " | " + board[8] + "   7 | 8 | 9")
    print("\n")


def choose_mode():
    print("Wybierz tryb gry:")
    print("1 - Gracz vs Gracz")
    print("2 - Gracz vs AI")

    mode = input("Twój wybór: ")

    while mode not in ("1", "2"):
        mode = input("Wpisz 1 lub 2: ")

    return mode


def handle_turn(player):
    print(player, "Twoja kolej")
    position = input("Wybierz pozycję od 1 do 9: ")

    while position not in ("1", "2", "3", "4", "5", "6", "7", "8", "9"):
        position = input("Błędna wartość. Wybierz pozycję 1-9: ")

    position = int(position) - 1

    if board[position] != "-":
        print("To miejsce jest już zajęte")
        return handle_turn(player)

    board[position] = player
    display_board()


def ai_move():
    free_positions = [i for i, v in enumerate(board) if v == "-"]
    return random.choice(free_positions)


def check_if_game_is_on(current_player):
    if check_rows() or check_columns() or check_diagonals():
        winner = flip_player(current_player)
        print("Gratulacje", winner, "wygrałeś!")
        return False

    elif "-" not in board:
        print("Mamy remis!")
        return False

    return True


def check_rows():
    return (board[0] == board[1] == board[2] != "-" or
            board[3] == board[4] == board[5] != "-" or
            board[6] == board[7] == board[8] != "-")


def check_columns():
    return (board[0] == board[3] == board[6] != "-" or
            board[1] == board[4] == board[7] != "-" or
            board[2] == board[5] == board[8] != "-")


def check_diagonals():
    return (board[0] == board[4] == board[8] != "-" or
            board[2] == board[4] == board[6] != "-")


def flip_player(current_player):
    if current_player == "X":
        return "O"
    else:
        return "X"


def play_game():
    display_board()
    mode = choose_mode()

    current_player = "X"

    while check_if_game_is_on(current_player):

        if mode == "1":  # Gracz vs Gracz
            handle_turn(current_player)

        elif mode == "2":  # Gracz vs AI
            if current_player == "X":
                handle_turn("X")
            else:
                print("Ruch AI...")
                position = ai_move()
                board[position] = "O"
                display_board()

        current_player = flip_player(current_player)


play_game()
