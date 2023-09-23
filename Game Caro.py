import random

def DrawBoard (board):
    print( board[7] + '|' + board[8] + '|' + board[9] )
    print('-----')
    print(board[4] + '|' + board[5] + '|' + board[6] )
    print('-----')
    print(board[1] + '|' + board[2] + '|' + board[3] )
    print('-----')


def Input_player ():
    letter = ''
    while not ( letter == 'X' or letter == 'O'):
        print("Do you want X of O?")
        letter = input().upper()            # In hoa kí tự
    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']


def Who_goes_first():
    if random.randint(0,1) == 0:
        return 'Computer'
    else:
        return 'Player'


def Make_move (board, value, move):
    board[move] = value


def Move_correct(board, move):
    return board[move] == ' '


def Get_player_move (board):
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not Move_correct(board, int(move)):
        print("What is your next move ?")
        move = input()
    return int(move)


def Copy_board(board):
    board_copy = []
    for i in board:
        board_copy.append(i)
    return board_copy


def Choose_random_move (board, moveslist):
    possible_moves = []
    for i in moveslist:
        if Move_correct (board, i):
            possible_moves.append(i)
    if len( possible_moves ) != 0:
        return random.choice(possible_moves)
    else:
        return None

def Who_winner(board, value):
    return ( 
             (board[7] == board[8] == board[9] == value) or
             (board[4] == board[5] == board[6] == value) or
             (board[1] == board[2] == board[3] == value) or
             (board[7] == board[4] == board[1] == value) or
             (board[8] == board[5] == board[2] == value) or
             (board[9] == board[6] == board[3] == value) or
             (board[7] == board[5] == board[3] == value) or
             (board[9] == board[5] == board[1] == value)
           )


# Tạo mã AI:
def Computer_moves (board, computer_value):
    if computer_value == 'X':
        player_value = 'O'
    else:
        player_value ='X'
    for i in range(1,10):
        BoardCopy = Copy_board (board)
        if Move_correct (BoardCopy, i):
            Make_move (BoardCopy, computer_value, i)
            if Who_winner (BoardCopy, computer_value):
                return i
    for i in range(1,10):
        BoardCopy = Copy_board (board)
        if Move_correct (BoardCopy, i):
            Make_move (BoardCopy, player_value, i)
            if Who_winner (BoardCopy, player_value):
                return i
    move_for_computer = Choose_random_move( board, [1,3,7,9])
    if move_for_computer != None:
        return move_for_computer
    if Move_correct(board, 5):
        return 5
    else:
        return Choose_random_move( board, [2,4,6,8])

def full_board (board):
    for i in range(1,10):
        if Move_correct(board, i):
            return False
    return True

# Thực hiện trò chơi:
print("Welcome to my game: X O")
while True:
    player_value, computer_value = Input_player()
    turn = Who_goes_first()
    print(f"The person {turn} go first !")
    Myboard = [' '] * 10
    Game_is_playing = True
    while Game_is_playing:
        if turn == 'Player':
            DrawBoard(Myboard)
            move = Get_player_move(Myboard)
            Make_move(Myboard, player_value, move)
            if Who_winner(Myboard, player_value):
                DrawBoard(Myboard)
                print("You won this game !")
                Game_is_playing = False
            else:
                if full_board(Myboard):
                    DrawBoard(Myboard)
                    print("The game is a tie !")
                    break
                else:
                    turn = 'Computer'
        else:
            move = Computer_moves(Myboard, computer_value)
            Make_move(Myboard, computer_value, move)
            if Who_winner(Myboard, computer_value):
                DrawBoard(Myboard)
                print("You are lose !")
                Game_is_playing = False
            else:
                if full_board(Myboard):
                    DrawBoard(Myboard)
                    print("The game is a tie !")
                    break
                else:
                    turn = 'Player'
    print("Do you want play again ? Yes or No")
    if input().upper().startswith('N'):
        break