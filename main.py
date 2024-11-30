# main.py
from board import Connect4Board
from solver import next_move

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
        player_column = int(input(f"Place piece in which column 0-{board.columns-1}?"))
        board.add_to_column(player_column, player_value)

        # Computer turn
        # computer_column = next_move(board, computer_value)
        computer_column = 0 # just pick 0 always for now
        board.add_to_column(computer_column, computer_value)

if __name__ == "__main__":
    board = Connect4Board(rows=6, columns=7)
    game_loop(board)
