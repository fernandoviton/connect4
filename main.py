# main.py
from board import Connect4Board
from solver import next_move

def get_valid_column_from_user(board):
    while True:
        column = int(input(f"Place piece in which column 0-{board.columns-1}?"))
        if not board.is_valid_column(column):
            print(f"Please choose a column between 0 and {board.columns-1}")
        elif board.is_column_full(column):
            print(f"Please choose a column that is not full")
        else:
            return column

def game_loop(board):
    player_value=1
    computer_value=2
    turn=0
    while True:
        print(board)
        turn += 1

        if turn > 4:
            print("Game over!")
            break

        # Player turn
        player_column = get_valid_column_from_user(board)
        board.add_to_column(player_column, player_value)

        # Computer turn
        # computer_column = next_move(board, computer_value)
        computer_column = 0 # just pick 0 always for now
        board.add_to_column(computer_column, computer_value)

if __name__ == "__main__":
    board = Connect4Board(rows=6, columns=7)
    game_loop(board)
