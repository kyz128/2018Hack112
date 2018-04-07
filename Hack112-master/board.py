#game board
def init(data):
    data.cellSize = 30
    data.nR = data.height//data.cellSize
    data.nC = data.width//data.cellSize


class Board(object):
    def __init__(self, board):
        self.board = board
        self.R, self.C = len(board), len(board[0])
        self.cellSize = 30
    
    @staticmethod
    def drawFood(data, canvas):
        for i in range(data.rows - 1):
            for j in range(data.cols -1 ):
                if data.food[i][j] == 0:
                #open cells that pacman can travel through
                    canvas.create_rectangle(j * data.cellSize + data.cellSize/3, i * data.cellSize + data.cellSize/3,
                                (j + 1) * data.cellSize - data.cellSize/3, (i + 1) * data.cellSize - data.cellSize/3,
                                fill = "tan")
        

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
