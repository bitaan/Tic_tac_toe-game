import numpy as np
from board_draw import draw
def row_check(row):
    (c_1,c_2) = (0, 0)
    for i in range(0, 3):
        if row[i] == 'X':
            c_1 += 1
        elif row[i] == 'o':
            c_2 += 1
    if c_1 == 3:
        return 1
    elif c_2 == 3:
        return 2
    else:
        return None

def col_check(col):

    (c_1,c_2) = (0, 0)
    for i in range(0, 3):
        if col[i] == 'X':
            c_1 += 1
        elif col[i] == 'o':
            c_2 += 1
    if c_1 == 3:
        return 1
    elif c_2 == 3:
        return 2
    else:
        return None

def diag_check(diag):
    (c_1,c_2) = (0, 0)
    for i in range(0, 3):
        if diag[i] == 'X':
            c_1 += 1
        elif diag[i] == 'o':
            c_2 += 1
    if c_1 == 3:
        return 1
    elif c_2 == 3:
        return 2
    else:
        return None    

def start():
    #print("A tic tac toe board has 3 rows and 3 columns. So when the prompt appears, please enetr 3 and 3")
    #print(draw(3,3))
    draw(3, 3)
    print("""This is what a tic tac toe baord looks like.
            Only values possible are:
            X --> Player one
            o --> Player two
            0 --> No one has entered""")
    a = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    return a

def enter(a, player):
    while True:
        b = 1
        try:    
            d = 0
            while d == 0:
                x = int(input("Enter the row where you want to enter your entry:"))
                y = int(input("Enter the column where you want to enter your entry:"))
                if a[x][y] == 0:
                    if player == 1:
                        a[x][y] = 'X'
                    else:
                        a[x][y] = 'o'
                    d = 1
                else:
                    print("This place is already filled choose again wisely")
        except ValueError:
            print("Enter integer values only")
            b = 0
        if b == 1:
            break

def present(a):
    print('_'*3*3)
    for i in range(0, 3):
        print('| {}| {}| {}|'.format(a[i][0], a[i][1], a[i][2]))
        print('_'*3*3)

def win_lose(a, a_t):
    c = 0
    for i in range(0, 3):
        send_row = list(a[i])
        winner = row_check(send_row)
        if winner is not None:
            c = 1
            break
    if c == 1:
        print('We have found a winner:{}'.format(winner))
        return 1
    for i in range(0, 3):
        send_col = list(a_t[i])
        winner = col_check(send_col)
        if winner is not None:
            c = 1
            break
    if c == 1:
        print('We have found a winner:{}'.format(winner))
        return 1
    for i in range(0, 2):
        if i == 0:
            send_diag = [a[0][0], a[1][1], a[2][2]]
        else:
            send_diag = [a[0][2], a[1][1], a[2][0]]
        winner = diag_check(send_diag)
        if winner is not None:
            c = 1
            break
    if c == 1:
        print('We have found a winner:{}'.format(winner))
        return 1
    else:
        print("No winner for this game")
        return 0

def alternate_player(p):
    if p == 1:
        return 2
    else:
        return 1

if __name__ == '__main__':
    try:
        while True:
            a = start()
            moves = 9
            player = 1
            while moves > 0:
                present(a)
                enter(a, player)
                a_t = [list(i) for i in zip(*a)]
                win_or_not = win_lose(a, a_t)
                moves -= 1
                if win_or_not == 0:
                    if moves == 0:
                        print("Tie")
                        break
                elif win_or_not == 1:
                    break
                player = alternate_player(player)
    except ValueError:
        print("Only values you can enter for row and column values, are integers.")