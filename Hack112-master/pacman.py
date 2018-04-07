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
                  
    def eatFood(self,data):
        for i in range(len(data.food)):
            for j in range(len(data.food[0])):
                if ((data.food[i][j] == 0) and ((self.x)//data.cellSize, (self.y)//data.cellSize)==(j, i)):
                    data.food[i][j]= 1


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




import random 
import copy

class Monster(object):
    all_monsters = []
    
    def __init__(self, data, color):
        self.color = color
        self.size = data.cellSize
        self.r, self.c = data.monsterCenter[0], data.monsterCenter[1]
        Monster.all_monsters.append(self)
    
    
    def draw(self, data, canvas):
        r = self.size
        canvas.create_oval(self.r * self.size, self.c * self.size,
                        (self.r + 1) * self.size, (self.c + 1) * self.size,
                        fill = self.color)

    def move(self, data, dr, dc):
    #moves monster
        if data.gameOver: return
        if ((0 < self.r + dr < data.cols) and (1 < self.c + dc < data.rows)):
                self.r += dr
                self.c += dc
