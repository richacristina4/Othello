
from ast import literal_eval as eval

board_size = 8
BLACK = '\u26AB'
WHITE = '\u26AA'
EMPTY = "\U0001F7E9"
check_move_legality = ((0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1 , 1))

def inverse(piece):
    return BLACK if piece is WHITE else WHITE

def main():
    board = create_board()
    piece = BLACK
    while has_valid_move(board, piece):
        game_loop(board, piece)
        if has_valid_move(board, inverse(piece)):
            piece = inverse(piece)
    print_board(board)
    black, white = 0,0
    for row in board:
        for token in row:
            if token is WHITE: white += 1
            if token is BLACK: black += 1
    if black == white:
        print("BOTH PLAYER'S SCORES MATCH - GAME IS A TIE")
    else:
        print()
        print('{token} CONGRATULATIONS, YOU WON!' % (BLACK if black>white else WHITE))
    return


def create_board():
    board = [[EMPTY for x in range(board_size)] for x in range(board_size)]
    half = board_size //  2
    board[half -1][half - 1] = WHITE
    board[half][half] = WHITE
    board[half - 1][half] = BLACK
    board[half][half - 1] = BLACK
    return board


def print_board(board):
    for row in range(len(board)):
        print(*board[row], sep='')
    return


def game_loop(board, piece):
    print()
    print_board(board)
    while(True):
        try:
            move = eval(input('WHERE SHOULD I PLACE %s? ' % piece))
            move = tuple(reversed(move))
            if is_valid_move(board, piece, move):
                place_piece(board, piece, move)
                return
            else:
                raise AssertionError
        except (TypeError, ValueError, IndexError, SyntaxError, AssertionError):
            print('WRONG MOVE, ENTER THE MOVE AGAIN')


def is_valid_move(board, piece, move):
    if board[move[0]][move[1]] is not EMPTY: return False
    for validation_pair in check_move_legality:
        validate_move = [move[0]+validation_pair[0], move[1]+validation_pair[1]]
        while 0<=validate_move[0]<board_size-1 and 0<=validate_move[1]<board_size-1 and \
              board[validate_move[0]][validate_move[1]] is inverse(piece):
            validate_move[0] += validation_pair[0]
            validate_move[1] += validation_pair[1]
            if board[validate_move[0]][validate_move[1]] is piece:
                return True
    return False

def place_piece(board, piece, move):
    board[move[0]][move[1]] = piece
    for validation_pair in check_move_legality:
        validate_move = [move[0]+validation_pair[0], move[1]+validation_pair[1]]
        while 0<=validate_move[0]<board_size and 0<=validate_move[1]<board_size:
            if board[validate_move[0]][validate_move[1]] is EMPTY: break
            if board[validate_move[0]][validate_move[1]] is piece:
                flip(board, piece, move, validation_pair)
                break
            validate_move[0] += validation_pair[0]
            validate_move[1] += validation_pair[1]	
    return

def flip(board, piece, move, validation_pair):
    validate_move = [move[0]+validation_pair[0], move[1]+validation_pair[1]]
    while(board[validate_move[0]][validate_move[1]] is inverse(piece)):
        board[validate_move[0]][validate_move[1]] = piece
        validate_move[0] += validation_pair[0]
        validate_move[1] += validation_pair[1]
    return

def has_valid_move(board, piece):
    for y in range(board_size):
        for x in range(board_size):
            if is_valid_move(board, piece, (y,x)): return True
    return False

if __name__ == '__main__':
    main()
  