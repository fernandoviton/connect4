import unittest
from board import Connect4Board
from turns import take_turn, check_for_winner, print_board

class TestTurns(unittest.TestCase):
    
    def test_nowinner(self):
        board = Connect4Board(rows=6, columns=7)
        
        row = take_turn(board, board.RED, 3)
        row = take_turn(board, board.RED, 3)
        row = take_turn(board, board.RED, 3)

        result = check_for_winner(board, row, 3)
        self.assertEqual(result, False)
        print_board(board)

    def test_winner(self):
        board = Connect4Board(rows=6, columns=7)
        
        row = take_turn(board, board.RED, 3)
        row = take_turn(board, board.RED, 3)
        row = take_turn(board, board.RED, 3)
        row = take_turn(board, board.RED, 3)
        
        result = check_for_winner(board, row, 3)
        self.assertEqual(result, True)
        print_board(board)
    

if __name__ == "__main__":
    unittest.main()