# main.py
from board import Connect4Board
from solver import next_move

# Nichol wrote this function
def print_board(board, headers=True):
    # if headers is True, print the column numbers and a - on the line below
    if headers:
        for column in range(board.columns):
            print(f" {column}", end=' ')
        print(f"")
        for column in range(board.columns):
            print(f" -", end=' ')
        print(f"")
    for row in range(board.rows):
        for column in range(board.columns):
            value = board.get_cell(row, column)
            print(f" {value}", end=' ')
        print(f"")


def get_valid_column_from_user(board):
    while True:
        column = int(input(f"Place piece in which column 0-{board.columns-1}?"))
        if not board.is_valid_column(column):
            print(f"Please choose a column between 0 and {board.columns-1}")
        elif board.is_column_full(column):
            print(f"Please choose a column that is not full")
        else:
            return column
        
# Check if we have a winner
# column_hint is the column that was last played (which has to be part of the winning condition)
def have_winner(board, player_value, column_hint):
    # Check if we have a winner, starting from the last played column
    
    # So first get the last played cell by finding the first row that is not empty in column_hint
    row = board.top_non_empty_row_in_column(column_hint)
    column = column_hint
    print(f"need to check winner for {player_value} at {row}, {column}")

    # for now we end only when a column is full
    for column in range(board.columns):
        if board.is_column_full(column):
            return True
                
    return False
        
def do_player_turn(board, player_value):
    column = get_valid_column_from_user(board)
    board.add_to_column(column, player_value)
    if have_winner(board, player_value, column):
        return True
    
def do_computer_turn(board, player_value):
    # column = next_move(board, player_value)
    column = 0 # just pick 0 always for now
    board.add_to_column(column, player_value)
    if have_winner(board, player_value, column):
        return True

def game_loop(board):
    human_value=1
    computer_value=2
    while True:
        print_board(board)

        if do_player_turn(board, human_value):
            print("End of game, player played last move")
            break

        if do_computer_turn(board, computer_value):
            print("End of game, computer played last move")
            break

if __name__ == "__main__":
    board = Connect4Board(rows=6, columns=7)
    game_loop(board)
