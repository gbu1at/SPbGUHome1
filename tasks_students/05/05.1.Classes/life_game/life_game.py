class LifeGame(object):
    """
    Class for Game life
    """

    def __init__(self, board: list[list:int]):
        self.board: list[list:int] = board
        self.rows = self.board.__len__()
        self.cols = self.board[0].__len__()

    def get_next_generation(self):
        new_board: list[list:int] = [[-1 for _ in range(self.cols)] for _ in range(self.rows)]
        for row in range(self.rows):
            for col in range(self.cols):
                new_board[row][col] = self.get_next_cell_generator(row, col)

    def __get_next_cell_generator(self, row, col):
        if self.board[row][col] == 1:
            return

        elif self.board[row][col] == 0:
            ...

        elif self.board[row][col] == 2:
            ...


