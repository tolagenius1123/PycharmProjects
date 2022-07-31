import os

db_row1 = [" ", " ", " "]
db_row2 = [" ", " ", " "]
db_row3 = [" ", " ", " "]

status = False


def display_board():
    for each in db_row1:
        print(each, " | ", end="")
    print()
    for each in db_row2:
        print(each, " | ", end="")
    print()
    for each in db_row3:
        print(each, " | ", end="")
    print()


player1 = "X"
player2 = "O"


def validate_row(db_row, player, player_name):
    if db_row[0] == player and db_row[1] == player and db_row[2] == player:
        print(f"{player_name} wins!")
        display_board()
        os.abort()


def validate_diagonal_1(player, player_name):
    if db_row1[0] == player and db_row2[1] == player and db_row3[2] == player:
        print(f"{player_name} wins!")
        display_board()
        os.abort()


def validate_diagonal_2(player, player_name):
    if db_row1[2] == player and db_row2[1] == player and db_row3[0] == player:
        print(f"{player_name} wins!")
        display_board()
        os.abort()


def win(player, player_name):
    for i in range(0, 3):
        if db_row1[i] == player and db_row2[i] == player and db_row3[i] == player:
            print(f"{player_name} wins!")
            display_board()
            os.abort()
    validate_row(db_row1, player, player_name)
    validate_row(db_row2, player, player_name)
    validate_row(db_row3, player, player_name)
    validate_diagonal_1(player, player_name)
    validate_diagonal_2(player, player_name)


def play_game(number, player, player_name, opponent):
    for i in range(1, 4):
        if number == i and db_row1[i - 1] != player and db_row1[i - 1] != opponent:
            db_row1[i - 1] = player
    for i in range(4, 7):
        if number == i and db_row2[i - 4] != player and db_row2[i - 4] != opponent:
            db_row2[i - 4] = player
    for i in range(7, 10):
        if number == i and db_row3[i - 7] != player and db_row3[i - 7] != opponent:
            db_row3[i - 7] = player
    win(player, player_name)
    if number <= 0 or number > 9:
        print("Invalid number! Game Over")
        os.abort()


while status is False:
    x = int(input("Player 1 turn-> Enter number between 1 and 9: "))
    play_game(x, player1, "Player1", player2)
    display_board()
    y = int(input("Player 2 turn-> Enter number between 1 and 9: "))
    play_game(y, player2, "Player2", player1)
    display_board()