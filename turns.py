from board import Connect4Board

GAME_SIZE = 10

def create_empty_matrix(size):
    return [[0 for _ in range(size)] for _ in range(size)]


def my_turn(board):
    column = int(input("Please enter a number: "))
    print(f"You entered: {column}")
    row = 0
    for row in range(board.rows):
        if board.get_cell(row, column) != 0: 
            row = row-1
            break
    if row > 0:
        board.set_cell(row, column, 1)

def check_for_winner(board, row, column, number):
    for row in range(board.rows):
        pass
    
    return True

def take_turns(board):
    while True: 
        my_turn(board)
        my_turn(board)
        my_turn(board)
        my_turn(board)
        if check_for_winner(board, 0, 0, 0) == True:
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
    take_turns(board)
    print_board(board)

    #for row in matrix:
    #    print(row)

