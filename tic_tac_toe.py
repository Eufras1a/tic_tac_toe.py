from random import randint, choice

board = {}
list_board = []
sym = {}  # symbol player/controller: tick or cross


def main():
    global sym
    sym['comp'] = controller()  # assigning computer AI symbol
    set_board()
    play()


# main code of the game
def play():
    start = initial_set()  # if comp == 1, then comp goes first
    display_board()

    if start == 1: 
        print('Computer starts first!!')
        comp_turn()

    while True:
        player_turn()
        display_board()
        if win_checker(sym['player']):
            break
        
        comp_turn()
        if win_checker(sym['comp']):
            break


# check if anyone has won ? 
def win_checker(temp):
    global list_board, board

    # check for if anyone makes a line
    if board['top-L'] == board['top-R'] == board['top-M'] == temp :
        return end_msg(temp)
    elif board['mid-L'] == board['mid-R'] == board['mid-M'] == temp :
        return end_msg(temp)
    elif board['bottom-L'] == board['bottom-R'] == board['bottom-M'] == temp :
        return end_msg(temp)
    elif board['top-L'] == board['bottom-L'] == board['mid-L'] == temp :
        return end_msg(temp)
    elif board['top-R'] == board['bottom-R'] == board['mid-R'] == temp :
        return end_msg(temp)
    elif board['top-M'] == board['bottom-M'] == board['mid-M'] == temp :
        return end_msg(temp)
    elif board['top-L'] == board['mid-M'] == board['bottom-R'] == temp :
        return end_msg(temp)
    elif board['top-R'] == board['mid-M'] == board['bottom-L'] == temp :
        return end_msg(temp)

    # if the board is filled then tie
    if not list_board:
        return end_msg('tie')

    return False



def end_msg(temp):
    if temp == sym['player']:
        print('Congratulations you won!!!')
    elif temp == sym['player']:
        print('Game Over')
    else:
        print()
        print("It's a tie!!!")
    
    return True


# computer's move
def comp_turn():
    global sym, board, list_board
    print("It's computer's turn.")
    move = choice(list_board)
    board[move] = sym['comp']
    list_board.remove(move)
    #sleep(2)
    display_board()

# ask user for their move 
def player_turn():
    global sym, board, list_board
    print("Where would you like to mark ? (for Row type [top-, mid-, bottom-] and for column type [L, M, R] ) example: top-L")
    while True:
        temp = input()
        if board.get(temp, 'Fail') == 'Fail':
            print('error: invalid keyword, try again')
        elif board[temp] != " ":
            print('that place is already filled duh!!!')
        else:
            board[temp] = sym['player']
            list_board.remove(temp)
            break
    display_board()

# display the current state of the game baord
def display_board():
    print()
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R']) 
    print('-----')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-----') 
    print(board['bottom-L'] + '|' + board['bottom-M'] + '|' + board['bottom-R']) 
    print()
    print()

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
            print('pls either enter alphabetical X or O to proced further into the game', end = ': ')

        
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
    while True:
        main()
        print('Would you like to play again ?', 'Press "y" to play again or to quit press any key', sep = '\n')
        if input().lower() != 'y':
            break