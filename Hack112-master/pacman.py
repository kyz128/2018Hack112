def collideWithWalls(row, col, data):
    for i in range(len(data.maze)):
        for j in range(len(data.maze[0])):
            if ((data.maze[i][j] == 1) and (row == j) and (col == i)):
                return True
    return False
    
class Pacman(object):

    def __init__(self, row, col, data):
        self.x = data.cellSize/2 + data.cellSize*row
        self.y = data.cellSize/2 + data.cellSize*col
        self.size = (data.cellSize*2/3)/2
    
    def move(self, dx, dy, data):
        if collideWithWalls((self.x + dx)//data.cellSize,
                            (self.y + dy)//data.cellSize, data):
            pass
        
        else:
            if ((0 < self.x + dx < (data.cols - 1) * data.cellSize) and
            (0 < self.y + dy < (data.rows - 1) * data.cellSize)):
                self.x += dx
                self.y += dy
            else:
                self.x = temp[0]
                self.y = temp[1]

    def drawPacman(self, canvas, color="yellow"):
        r = self.size
        canvas.create_oval(self.x-r, self.y-r, 
                           self.x+r, self.y+r, fill=color)
