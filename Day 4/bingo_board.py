class BingoBoard:

    def __init__(self):
        self.board = [][]
        self.board_size_x = 0
        self.board_size_y = 0

    def set_board(board=None, size_x=None, size_y=None):
        self.board_size_x = size_x
        self.board_size_y = size_y

        for number in board:
            pass

    def check_number(selected_number=None) -> bool:
        for i in range(0, self.board_size_x):
            for j in range(0, self.board_size_y):
                board_number = self.board[i][j]
                if int(number[-1:]) == selected_number:
                    self.board[i][j] = "{}t".format(selected_number)
                    return True

        return False

    def check_line() -> bool:
        for i in range(0, self.board_size_x):
            for j in range(0, self.board_size_y):
                if not i == j:
                    #if self.board[i][j] == self.board[x][j]
                    pass

    def get_points(last_called_number=None):
