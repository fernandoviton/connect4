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
    directions = [(1, 0), (0, 1), (1, 1), (1, -1)]
    for d_row, d_col in directions:
        if check_direction(board, row, col, d_row, d_col):
            return True
    return False


def check_direction(board, row, col, d_row, d_col):
    count = 0
    color = board.get_cell(row, col)
    r, c = row, col
    while r < board.rows and c < board.cols and board[r][c] == color:
        count += 1
        r += d_row
        c += d_col

    # Check in the negative direction
    r, c = row - d_row, col - d_col
    while r >= 0 and c >= 0 and board.get_cell(r, c) == color:
        count += 1
        r -= d_row
        c -= d_col

    return count >= 4


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

