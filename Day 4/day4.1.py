import os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

from bingo_board.py import BingoBoard

bingo_boards = open(os.path.join(__location__, 'day4-bingo-boards.txt')).read().splitlines()
bingo_numbers = open(os.path.join(__location__, 'day4-bingo-numbers.txt')).read().splitlines()[0].split(',')

def create_bingo_boards(self, bingo_boards=None) -> list:
    pass

def play():
    boards = create_bingo_tables(bingo_boards=bingo_boards)
    for number in bingo_numbers:
        for board in boards:
            board.check_line()
