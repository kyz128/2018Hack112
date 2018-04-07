class Pacman(object):

    def __init__(self, x, y, data):
        self.x = x
        self.y = y
        self.size = (data.cellSize*2/3)/2
            
    def move(self, dx, dy, data):
        if ((data.cellSize//2 < self.x + dx < data.cols-1*data.cellSize)
            and (data.cellSize//2 < self.y + dy < data.rows*data.cellSize):
            self.x += dx
            self.y += dy

    def drawPacman(self, canvas, color="yellow"):
        r = self.size
        canvas.create_oval(self.x-r, self.y-r, 
                           self.x+r, self.y+r, fill=color)
