from pprint import pprint
from random import randint
board = {}
sym = {}

def main():
    global sym
    sym['comp'] = controller()
    set_board()
    play()

# main code of the game
def play():
    start = initial_set() #  if comp == 1, then comp goes first
    display_board()
    update_board()

# ask user for their move 
def update_board():
    global sym, board

    print("Where would you like to mark ? (for Row type [top-, mid-, bottom-] and for column type [L, M, R] ) example: top-L")
    while True:
        temp = input()
        if board.get(temp, 'Fail') == 'Fail':
            print('error: invalid answer, try again')
        else: 
            board[temp] = sym['player']




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
    global board
    board = {'top-L'    : ' ',
             'top-M'    : ' ',
             'top-R'    : ' ',
             'mid-L'    : ' ',
             'mid-M'    : ' ',
             'mid-R'    : ' ',
             'bottom-L' : ' ',
             'bottom-M' : ' ',
             'bottom-R': ' ' }

if __name__ == '__main__':
    main()