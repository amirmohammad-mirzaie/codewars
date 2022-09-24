# https://www.codewars.com/kata/534e01fbbb17187c7e0000c6

# Your task, is to create a NxN spiral with a given size.
#
# For example, spiral with size 5 should look like this:
#
# 00000
# ....0
# 000.0
# 0...0
# 00000
# and with the size 10:
#
# 0000000000
# .........0
# 00000000.0
# 0......0.0
# 0.0000.0.0
# 0.0..0.0.0
# 0.0....0.0
# 0.000000.0
# 0........0
# 0000000000
# Return value should contain array of arrays, of 0 and 1, with the first row being composed of 1s. For example for given size 5 result should be:
#
# [[1,1,1,1,1],[0,0,0,0,1],[1,1,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
# Because of the edge-cases for tiny spirals, the size will be at least 5.
#
# General rule-of-a-thumb is, that the snake made with '1' cannot touch to itself.


import sys

sys.setrecursionlimit(10000)

# I wanted to use recursion
def spiralize(size):
    moving = MovingObj(size=size)
    moving.right(row_no=0, col_no=0)

    spiral = moving.board

    return spiral


class MovingObj:

    def __init__(self, size):
        self.size = size

        self.row_no = 0
        self.col_no = 0

        self.board = [[0 for x in range(self.size)] for y in range(self.size)]

    def right(self, row_no, col_no):

        if (self.size - 1) >= col_no >= 0 and (self.size - 1) >= row_no >= 0:

            if self.board[row_no][col_no] == 1:
                if self.size % 2 == 0:
                    self.board[row_no][col_no - 1] = 0

                return

            if row_no == 0:
                self.board[row_no][col_no] = 1

                if col_no == (self.size - 1):
                    self.down(row_no + 1, col_no)
                else:
                    self.right(row_no, col_no + 1)

            elif self.board[row_no][col_no + 1] == 0:

                self.board[row_no][col_no] = 1
                self.right(row_no, col_no + 1)

            else:

                self.down(row_no + 1, col_no - 1)

    def left(self, row_no, col_no):
        if (self.size - 1) >= col_no >= 0 and (self.size - 1) >= row_no >= 0:

            if self.board[row_no][col_no] == 1:
                if self.size % 2 == 0:
                    self.board[row_no][col_no + 1] = 0

                return

            if row_no == (self.size - 1):
                self.board[row_no][col_no] = 1

                if col_no == 0:
                    self.up(row_no - 1, col_no)
                else:
                    self.left(row_no, col_no - 1)

            elif self.board[row_no][col_no - 1] == 0:

                self.board[row_no][col_no] = 1
                self.left(row_no, col_no - 1)

            else:

                self.up(row_no - 1, col_no + 1)

    def up(self, row_no, col_no):

        if (self.size - 1) >= col_no >= 0 and (self.size - 1) >= row_no >= 0:

            if self.board[row_no][col_no] == 1:
                if self.size % 2 == 0:
                    self.board[row_no + 1][col_no] = 0

                return

            if self.board[row_no - 1][col_no] == 0:

                self.board[row_no][col_no] = 1
                self.up(row_no - 1, col_no)

            else:

                self.right(row_no + 1, col_no + 1)

    def down(self, row_no, col_no):

        if (self.size - 1) >= col_no >= 0 and (self.size - 1) >= row_no >= 0:

            if self.board[row_no][col_no] == 1:
                if self.size % 2 == 0:
                    self.board[row_no - 1][col_no] = 0

                return

            if col_no == (self.size - 1):
                self.board[row_no][col_no] = 1

                if row_no == (self.size - 1):
                    self.left(row_no, col_no - 1)
                else:
                    self.down(row_no + 1, col_no)

            elif self.board[row_no + 1][col_no] == 0:

                self.board[row_no][col_no] = 1
                self.down(row_no + 1, col_no)

            else:

                self.left(row_no - 1, col_no - 1)
