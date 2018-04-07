from tkinter import *

def init(data):
    data.cellSize = 30
    data.nR = data.height//data.cellSize
    data.nC = data.width//data.cellSize
    data.xMargin = (data.width - ((data.nC)*data.cellSize))/2
    data.yMargin = (data.height - ((data.nR)*data.cellSize))/2


class Board(object):
    def __init__(self, board):
        self.board = board
        self.R, self.C = len(board), len(board[0])
        self.cellSize = 30

    def drawBoard(self, canvas):
        board = self.board
        for i in range(self.R - 1):
            for j in range(self.C -1 ):
                if board[i][j] == 0:
                #open cells that pacman can travel through
                    canvas.create_rectangle(j * self.cellSize, i * self.cellSize,
                                (j + 1) * self.cellSize, (i + 1) * self.cellSize,
                                fill = "black")
                else:
                #walls
                    canvas.create_rectangle(j * self.cellSize, i * self.cellSize,
                                (j + 1) * self.cellSize, (i + 1) * self.cellSize,
                                outline = "blue", fill = "blue")