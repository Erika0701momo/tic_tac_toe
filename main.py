board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

game_on = True
game_count = 1

current_player_number = 0

players = ["player1", "player2"]
player_sign = ["", ""]

def display_borad():
    print(board[0] + " | " + board[1] + " | " + board[2] + " " + "1 | 2 | 3")
    print("----------")
    print(board[3] + " | " + board[4] + " | " + board[5] + " " + "4 | 5 | 6")
    print("----------")
    print(board[6] + " | " + board[7] + " | " + board[8] + " " + "7 | 8 | 9")

player_sign[0] = input("player1さん、XかOか選んでください >>").upper()
if player_sign[0] == "O":
    player_sign[1] = "X"
else:
    player_sign[1] = "O"

print("player1さんは" + player_sign[0], "player2さんは" + player_sign[1] + "です")


def check_winner(current_player_number):
    global game_on
    board_index = 0
    for i in range(3):
        if board[board_index] == player_sign[current_player_number] and board[board_index + 1] == player_sign[current_player_number] and board[board_index + 2] == player_sign[current_player_number]:
            print(players[current_player_number] + "さんの勝ち！")
            game_on = False
            break
        board_index += 3

    board_index = 0
    for i in range(3):
        if board[board_index] == player_sign[current_player_number] and board[board_index + 3] == player_sign[current_player_number] and board[board_index + 6] == player_sign[current_player_number]:
            print(players[current_player_number] + "さんの勝ち！")
            game_on = False
            break
        board_index += 1

    board_index = 0
    plus_num = 4
    for i in range(2):
        if board[board_index] == player_sign[current_player_number] and board[board_index + plus_num] == player_sign[current_player_number] and board[board_index + plus_num * 2] == player_sign[current_player_number]:
            print(players[current_player_number] + "さんの勝ち！")
            game_on = False
            break
        board_index = 2
        plus_num = 2

def flip_player():
    global current_player_number
    if current_player_number == 0:
        current_player_number = 1
    else:
        current_player_number = 0

def choose_place():
    global board
    picked_place = int(input(players[current_player_number] + "さん、1から9までの数字で場所を選択してください>>"))
    board_index = picked_place - 1
    board[board_index] = player_sign[current_player_number]

check_winner(current_player_number)

while game_on:
    if game_count > 9:
        print("引き分けです！")
        break
    display_borad()
    print(players[current_player_number] + "さんの番です")
    choose_place()
    check_winner(current_player_number)
    flip_player()
    game_count += 1
