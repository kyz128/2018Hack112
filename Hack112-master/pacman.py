def collideWithWalls(row, col, data):
        for i in range(len(data.maze)):
            for j in range(len(data.maze[0])):
                if ((data.maze[i][j] == 1) and (row == i) and (col == j)):
                    return True
        return False

from PIL import ImageTk, Image        
class Pacman(object):

    def __init__(self, row, col, data):
        self.x = data.cellSize/2 + data.cellSize*row
        self.y = data.cellSize/2 + data.cellSize*col
        self.size = (data.cellSize*2/3)/2
         

    def move(self, dx, dy, data):
        if ((0 < self.x + dx < (data.cols-1)*data.cellSize)
            and (0< self.y + dy < (data.rows-1)*data.cellSize)):
            self.x += dx
            self.y += dy

    def drawPacman(self, canvas, color="yellow"):
        im = Image.open('pacman.png')
        canvas.image = ImageTk.PhotoImage(im)
        canvas.create_image(self.x, self.y, image=canvas.image)




