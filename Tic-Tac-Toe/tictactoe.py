import random

board = ["_", "_", "_",
         "_", "_", "_",
         "_", "_", "_"]

game_in_play = True
winner = None

player1 = "X"

current_player = player1
avail_spots = [0,1,2,3,4,5,6,7,8]
def display():
    print()
    print(board[0],board[1],board[2], "    1 2 3")
    print()
    print(board[3],board[4],board[5], "    4 5 6")
    print()
    print(board[6],board[7],board[8], "    7 8 9")
    print()

def player_move():
    print("Welcome, " + current_player+"!")
    move = int(input("Enter a number from 1-9 corresponding to the empty spots on the board to make your move: " ))
    while move<1 or move>9:
        move = int(input("Invaild number! Enter a number from 1-9 corresponding to the empty spots on the board to make your move: " ))

    spot = move-1
    
    if board[spot] != "_":
        print("that spot is already taken, input an availble spot below")
        move = int(input("Enter a number from 1-9 corresponding to the empty spots on the board to make your move: " ))
        spot = move-1
    else:
        board[spot] = current_player

    avail_spots.remove(spot)

    print()
    print("here is the updated board:")
    display()

def check_for_wins(a = board):
    global winner
    global game_in_play
    #checking all columns
    if a[0] == a[3] == a[6] and a[0]!= "_" and a[3] != "_" and a[6] != "_":
        if a[0] == "X":
            winner = player1
        else:
            winner = "BOT"
        return True

    if a[1] == a[4] == a[7] and a[1]!= "_" and a[4]!= "_" and a[7] != "_" :
        if a[1] == "X":
            winner = player1
        else:
            winner = "BOT"
        return True

    if a[2] == a[5] == a[8] and a[2] != "_" and a[5] != "_" and a[8] != "_":
        if a[2] == "X":
            winner = player1
        else:
            winner = "BOT"
        return True
    #checking rows
    if a[0] == a[1] == a[2] and a[0] != "_" and a[1] != "_" and a[2] != "_":
        if a[0] == "X":
            winner = player1
        else:
            winner = "BOT"
        return True

    if a[3] == a[4] == a[5] and a[3] != "_" and a[4] != "_" and a[5] != "_":
        if a[3] == "X":
            winner = player1
        else:
            winner = "BOT"
        return True

    if a[6] == a[7] == a[8] and a[6] != "_" and a[7] != "_" and a[8] != "_":
        if a[6] == "X":
            winner = player1
        else:
            winner = "BOT"
        return True
    #checking diagnols
    if a[0] == a[4] == a[8] and a[0] != "_" and a[4] != "_" and a[8] != "_":
        if a[0] == "X":
            winner = player1
        else:
            winner = "BOT"
        return True

    if a[2] == a[4] == a[6] and a[2] != "_" and a[4]!= "_" and a[6] != "_":
        if a[2] == "X":
            winner = player1
        else:
            winner = "BOT"
        return True
    print()

def bot_move():
    global board
    testboard = board.copy()
    m = None
    for x in avail_spots:
        testboard[x] = "O"
        if check_for_wins(testboard) != None:
            m = x
            break 

    if m is not None:
        board[m] = "O"          
    elif m == None:
        m = random.choice(avail_spots)
    board[m] = "O"

    avail_spots.remove(m)

    display()

def check_for_tie():
    if len(avail_spots)==0:
        return True



def play():
    global game_in_play
    display()
    print()
    while game_in_play:
        player_move()

        if check_for_wins():
            print("congrats, ", winner, "you won!!")
            game_in_play = False
            break
        if check_for_tie():
            print("There is a tie! No one wins.")
            game_in_play = False
            break

        bot_move()

        if check_for_wins():
            print("congrats, ", winner, "you won!!")
            game_in_play = False
            break
        if check_for_tie():
            print("There is a tie! No one wins.")
            game_in_play = False
            break

play()