import random 
import copy
from PIL import ImageTk, Image

class Monster(object):
    all_monsters = []
    
    def __init__(self, data):
        self.size = data.cellSize
        self.r, self.c = data.monsterCenter[0], data.monsterCenter[1]
        Monster.all_monsters.append(self)
    
    
    def draw(self, canvas):
    #image from http://chapmanworld.com/wp-content/uploads/2015/02/pacman.png
        r = self.size
        monster = Image.open('redMonster.png')
        canvas.image = ImageTk.PhotoImage(monster)
        canvas.create_image(self.r, self.c, image= canvas.image)
        


    def move(self, data, dr, dc):
    #moves monster
        if data.gameOver: return
        if ((0 < self.r + dr < data.cols) and (1 < self.c + dc < data.rows)):
                self.r += dr
                self.c += dc
    
    def collideWithPacMan(self, data):
        if (self.r == data.center[0]) and (self.c == data.center[1]):
            data.lives -= 1
            data.monsterCenter = 0, 1
            data.center = data.cols//2 - 1, data.rows//2 - 1

            
            
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
