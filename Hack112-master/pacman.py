def collideWithWalls(row, col, data):
    for i in range(len(data.maze)):
        for j in range(len(data.maze[0])):
            if ((data.maze[i][j] == 1) and (row == i) and (col == j)):
                return True
    return False
    
class Pacman(object):

    def __init__(self, row, col, data):
        self.x = data.cellSize/2 + data.cellSize*row
        self.y = data.cellSize/2 + data.cellSize*col
        self.size = (data.cellSize*2/3)/2
    
    def move(self, dx, dy, data):
        if ((data.cellSize//2 < self.x + dx < data.cols*data.cellSize)
            and (data.cellSize//2 < self.y + dy < data.rows*data.cellSize)
            and not collideWithWalls(self.x//data.cellSize, self.y//data.cellSize, data)):
            self.x += dx
            self.y += dy

    def drawPacman(self, canvas, color="yellow"):
        r = self.size
        canvas.create_oval(self.x-r, self.y-r, 
                           self.x+r, self.y+r, fill=color)




