# A data structure that represents a connect4 board
# this only has the data structure and no game logic
# the value in the cells in the board are 0 or 1
class Connect4Board:
    RED = 1
    YELLOW = 2
    
    def __init__(self, rows=6, columns=7):
        self.board = [[0 for _ in range(columns)] for _ in range(rows)]
        self.rows = rows
        self.columns = columns
        
    # string versions of the board.  They should be of the form:
    # 0000000 or 1111111 per row (number of items is based on the number of columns)
    def __str__(self):
        return "\n".join("".join(str(cell) for cell in row) for row in self.board)
    
    def rows(self):
        return self.rows
    
    def columns(self):
        return self.columns

    def get_cell(self, row, column):
        return self.board[row][column]

    def set_cell(self, row, column, value):
        self.board[row][column] = value

    # def is_full(self):
    #     for row in self.board:
    #         for cell in row:
    #             if cell == 0:
    #                 return False
    #     return True

    # def is_valid_move(self, column):
    #     return self.board[0][column] == 0

    # def get_valid_moves(self):
    #     return [column for column in range(self.columns) if self.is_valid_move(column)]

    # def get_winner(self):
    #     for row in range(self.rows):
    #         for column in range(self.columns):
    #             if self.board[row][column] != 0:
    #                 if self.check_winner(row, column):
    #                     return self.board[row][column]
    #     return 0

    # def check_winner(self, row, column):
    #     return self.check_horizontal(row, column) or self.check_vertical(row, column) or self.check_diagonal(row, column)

    # def check_horizontal(self, row, column):
    #     count = 0
    #     for i in range(max(0, column - 3), min(self.columns, column + 4)):
    #         if self.board[row][i] == self.board[row][column]:
    #             count += 1
    #             if count == 4:
    #                 return True
    #         else:
    #             count = 0
    #     return False

    # def check_vertical(self, row, column):
    #     count = 0
    #     for i in range(max(0, row - 3), min(self.rows, row + 4)):
    #         if self.board[i][column] == self.board[row][column]:
    #             count += 1
    #             if count == 4:
    #                 return True
    #         else:
    #             count = 0
    #     return False

    # def check_diagonal(self, row, column):
    #     pass