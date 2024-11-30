from board import Connect4Board

GAME_SIZE = 10

def take_turn(board, color, column):
    row = 0
    for row in range(board.rows):
        if board.get_cell(row, column) != 0: 
            row = row-1
            break
    if row > 0:
        board.set_cell(row, column, 1)
    return row
    


def my_turn(board):
    column = int(input("Please enter a number: "))
    print(f"You entered: {column}")
    take_turn(board, board.RED, column)

def check_for_winner(board, row, col):
    if check_vertical(board, row, col) == True: return True
    if check_horizontal(board, row, col) == True: return True
    if check_diag_right(board, row, col) == True: return True
    if check_diag_left(board, row, col) == True: return True
    return False

def check_horizontal(board, row, col): return True
def check_diag_right(board, row, col): return True
def check_diag_left(board, row, col): return True

def check_vertical(board, row, col):
    count = 0
    color = board.get_cell(row, col)
    row_dir = 1
    i = row + row_dir
    while i < board.rows: 
        if board.get_cell(i, col) == color: 
            count += 1
            i += row_dir
        else:
            break
    row_dir = -1
    i = row + row_dir
    while i >= 0:
        if board.get_cell(i, col) == color:
            count += 1
            i += row_dir
        else:
            break
    if count >= 4: return True
    return False


def play_game(board):
    while True: 
        my_turn(board)
        my_turn(board)
        my_turn(board)
        my_turn(board)
        if check_for_winner(board, 0, 0) == True:
            print(f"You win!")
            break

def print_board(board):
    for row in range(board.rows):
        print(f"")
        for column in range(board.columns):
            value = board.get_cell(row, column)
            print(f" {value}", end=' ')


if __name__ == "__main__":
    board = Connect4Board(rows=6, columns=7)
    #matrix = create_empty_matrix(GAME_SIZE)
    play_game(board)
    print_board(board)

    #for row in matrix:
    #    print(row)

