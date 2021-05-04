import random

def display_board(board):

    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')

def player_input():
    # Takes Player input and assigns X or O Marker, returns tuple (player1choice, player2choice)

    marker = ''

    while not (marker == 'X' or marker == 'O'):
        marker = random.randint(0,1)

        if marker == 0:
            return ('X', 'O')
        else:
            return ('O','X')


def place_marker(board, marker, position):
    board[position] = marker

def win_check(board, mark):

    return ((board[1] == mark and board[2] == mark and board[3] == mark) or # Hori
            (board[4] == mark and board[5] == mark and board[6] == mark) or # zon
            (board[7] == mark and board[8] == mark and board[9] == mark) or # tal
            (board[1] == mark and board[4] == mark and board[7] == mark) or  # Ver
            (board[2] == mark and board[5] == mark and board[8] == mark) or  # ti
            (board[3] == mark and board[6] == mark and board[9] == mark) or  # tal
            (board[1] == mark and board[5] == mark and board[9] == mark) or  # Dia
            (board[3] == mark and board[5] == mark and board[7] == mark))   # gonal

def choose_first():

    firstplayer = random.randint(1, 2)

    if firstplayer == 1:
        return 'Player 1'
    else:
        return 'Player 2'

def space_check(board, position):

    return board[position] == ' '

def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True

def player_choice(board):
    position = 0

    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input('Choose your next position: (1-9) '))

    return position

def random_choice(board):
    position = 0

    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = random.randint(1,9)

    return position


def replay():

    return input('Play again? Enter Yes or No: ').lower().startswith('y')

def getduplicateboard(board):
    # creates a duplicate board for AI to check win conditions
    duplicate_board = []

    for i in board:
        duplicate_board.append(i)

    return duplicate_board

def choose_random_move_from_list(board, moveslist):
    # returns valid move from passed list on passed board
    # returns None if no valid move
    possible_moves = []

    for i in moveslist:
        if space_check(board, i):
            possible_moves.append(i)

    if len(possible_moves) != 0:
        return random.choice(possible_moves)
    else:
        return None

def cpu_get_move(board, marker):

    if marker == 'X':
        playermarker = 'O'
    else:
        playermarker = 'X'



    # check if CPU has a winning move

    for i in range(1, 10):
        copy = getduplicateboard(board)
        if space_check(copy, i):
            place_marker(copy, marker, i)
            if win_check(copy, marker):
                return i

    # check if next move of player could be winning move, block

    for i in range(1, 10):
        copy = getduplicateboard(board)
        if space_check(copy,i):
            place_marker(copy,playermarker, i)
            if win_check(copy,playermarker):
                return i

    # Try to take corners
    move = choose_random_move_from_list(board, [1, 3, 7, 9])
    if move != None:
        return move

    # Try to take center
    if space_check(board,5):
        return 5

    # take a side
    return choose_random_move_from_list(board,[2, 4, 6, 8])