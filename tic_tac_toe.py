from pprint import pprint
from random import randint, choice

board = {}
list_board = []
sym = {}
win = False
def main():
    global sym
    sym['comp'] = controller()
    set_board()
    play()

# main code of the game
def play():
    global win
    start = initial_set() #  if comp == 1, then comp goes first
    display_board()
    print(start)
    if start == 1: 
        print('Computer starts first!!')
    else:
        print('You go first!!!')

    while not win:
        if start == 0: 
            player_turn()
            start = 1
        else:
            comp_turn()
            start = 0

        display_board()
        win = win_checker()


# check if anyone has won ? 
def win_checker():
    global list_board, win
    s = []

    #check for if anyone makes a line

    #check for tie
    if list_board == s:
        print("tie")
        return True
    else:
        return False



# computer's move
def comp_turn():
    global sym, board, list_board
    move = choice(list_board)
    board[move] = sym['comp']
    list_board.remove(move)
    

# ask user for their move 
def player_turn():
    global sym, board, list_board
    print("Where would you like to mark ? (for Row type [top-, mid-, bottom-] and for column type [L, M, R] ) example: top-L")
    while True:
        temp = input()
        if board.get(temp, 'Fail') == 'Fail':
            print('error: invalid answer, try again')
        elif board[temp] != " ":
            print('try again')
        else: 
            board[temp] = sym['player']
            list_board.remove(temp)
            break




# display the current state of the game baord
def display_board():
    print()
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R']) 
    print('-----')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-----') 
    print(board['bottom-L'] + '|' + board['bottom-M'] + '|' + board['bottom-R']) 

# decide who goes first
def initial_set():
    return randint(0,1)

# decide what symbol does the player want to use 
def controller():
    global sym

    sym = { 'player': ' ', 'comp': ' '}
    print('Would you like to play with "X" or "O" ?')

    while True: 
        sym['player'] = input().upper()
        if sym['player'] == 'X':
            return 'O'
            
        elif sym['player'] == 'O':
            return 'X'
             
        else:
            print('pls either enter alphabetical X or O to proced further into the game')

        

# set the baord to inital state
def set_board():
    global board, list_board
    board = {'top-L'    : ' ',
             'top-M'    : ' ',
             'top-R'    : ' ',
             'mid-L'    : ' ',
             'mid-M'    : ' ',
             'mid-R'    : ' ',
             'bottom-L' : ' ',
             'bottom-M' : ' ',
             'bottom-R' : ' ' }

    list_board = list(board.keys())

if __name__ == '__main__':
    main()