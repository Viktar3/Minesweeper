import random

class Board():

    _mine = "m"

    def __init__(self, width, height, mines):
        self.width = width
        self.height = height
        self.mines = mines

        self.board = []

        for x in range(0, width):
            row = []
            for y in range(0, height):
                row.append(0)
            self.board.append(row)

        self.set_mines(width, height, mines, self.board)
        self.print_board()

    def set_mines(self, width, height, mines, board):
        while mines > 0:
            rand = random.randint(0, self.width*self.height)
            x = int(rand / self.width)
            y = rand % self.height

            cell = self.board[x][y]

            if cell is not self._mine:
                self.board[x][y] = self._mine
                mines -= 1

                minX = x - 1 if x > 0 else x
                while minX <= x + 1 and minX < self.width:
                    minY = y - 1 if y > 0 else y

                    while minY <= y + 1 and minY < self.height:
                        if self.board[minX][minY] is not self._mine:
                            self.board[minX][minY] += 1

                        minY += 1
                    minX += 1

    def print_board(self):
        board_str = ""

        for x in range(0, len(self.board)):
            for y in range(0, len(self.board[x])):
                board_str += str(self.board[x][y]) + " "
            board_str += "\n"

        print(board_str)


board = Board(10, 10, 10)

