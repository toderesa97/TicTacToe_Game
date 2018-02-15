import numpy as np

board = [["-","-", "-"],["-","-", "-"],["-","-", "-"]]

def print_board():
    for i in board:
        print(str(i)+"\n")

def start_game():
    player = str(np.floor(np.random.rand()*2+1))[0:1]
    name_p1 = input("Your name (X): ")
    name_p2 = input("Oponent's name (O): ")
    map = {"X": name_p1, "O": name_p2}
    if player == "1":
        print(str(name_p1) + " starts playing (X)")
        player = name_p1
    else:
        print(str(name_p2) + " starts playing (O)")
        player = name_p2
    winner = False

    while not winner:
        valid = False
        while not valid:
            piece = input("Player "+str(player)+", enter in format: row,column >>")
            try:
                row = int(piece[0:1])
                column = int(piece[2:])
            except:
                print("-Err: invalid input")
                continue
            if  not (1 <= row <= 3 and 1 <= column <= 3):
                print("-Err: Index out of range (positions must be between 1-3)")
                continue
            if board[row-1][column-1] != "-":
                print("-Err: Position ("+str(row)+","+str(column)+") already occupied")
                continue
            break

        board[row-1][column-1] = "X" if player == name_p1 else "O"
        for i in range(0,3):
            if board[i][0] == board[i][1] == board[i][2] and board[i][1] != "-":
                return "Player "+map[board[i][0]]+" wins!"
            if board[0][i] == board[1][i] == board[2][i] and board[2][i] != "-":
                return "Player "+map[board[0][i]]+" wins!"
        if board[0][0] == board[1][1] == board[2][2] and board[2][2] != "-":
            return "Player "+map[board[0][0]]+" wins!"
        if board[0][2] == board[1][1] == board[2][0] and board[2][0] != "-":
            return "Player "+map[board[1][1]]+" wins!"
        if player == name_p1:
            player = name_p2
        else:
            player = name_p1
        print_board()

print(start_game())