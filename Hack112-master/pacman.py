from PIL import ImageTk, Image  
      
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
        temp = self.x, self.y
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


    def drawPacman(self, canvas, data):
        im = Image.open('pacman.png')
        if data.direction=="Right":
            canvas.image = ImageTk.PhotoImage(im)
        elif data.direction=="Left":
            canvas.image = ImageTk.PhotoImage(im.transpose(Image.FLIP_LEFT_RIGHT))
        elif data.direction=="Up":
            canvas.image = ImageTk.PhotoImage(im.rotate(90))
        elif data.direction=="Down":
            canvas.image = ImageTk.PhotoImage(im.rotate(-90))
        canvas.create_image(self.x, self.y, image=canvas.image)




