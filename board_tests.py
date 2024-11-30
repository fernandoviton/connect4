import unittest
from board import Connect4Board

class TestConnect4Board(unittest.TestCase):
    def test_init(self):
        board = Connect4Board(rows=6, columns=7)
        self.assertEqual(str(board), "0000000\n0000000\n0000000\n0000000\n0000000\n0000000")

    def test_get_and_set_cell(self):
        board = Connect4Board(rows=6, columns=7)
        self.assertEqual(board.get_cell(0, 0), 0)
        board.set_cell(0, 0, 1)
        self.assertEqual(board.get_cell(0, 0), 1)
        self.assertEqual(board.get_cell(5,6 ), 0)
        board.set_cell(5, 6, 1)
        self.assertEqual(board.get_cell(5, 6), 1)

    def test_rows_and_columns(self):
        board = Connect4Board(rows=2, columns=5)
        self.assertEqual(board.rows, 2)
        self.assertEqual(board.columns, 5)

    def test_add_to_column(self):
        board = Connect4Board(rows=2, columns=4)
        self.assertTrue(board.add_to_column(0, 1))
        self.assertEqual(str(board), "0000\n1000")
        self.assertTrue(board.add_to_column(0, 1))
        self.assertEqual(str(board), "1000\n1000")
        self.assertFalse(board.add_to_column(0, 1))
        self.assertEqual(str(board), "1000\n1000")

    def test_is_valid_column(self):
        board = Connect4Board(rows=2, columns=4)
        self.assertTrue(board.is_valid_column(0))
        self.assertTrue(board.is_valid_column(3))
        self.assertFalse(board.is_valid_column(4))
        self.assertFalse(board.is_valid_column(-1))

    def test_is_column_full(self):
        board = Connect4Board(rows=2, columns=1)
        self.assertFalse(board.is_column_full(0))
        board.add_to_column(0, 1)
        self.assertFalse(board.is_column_full(0))
        board.add_to_column(0, 1)
        self.assertTrue(board.is_column_full(0))

if __name__ == "__main__":
    unittest.main()