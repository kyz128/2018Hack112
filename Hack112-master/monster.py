import random 
import copy

class Monster(object):
    all_monsters = []
    
    def __init__(self, data, color):
        self.color = color
        self.size = data.cellSize
        self.r, self.c = data.monsterCenter[0], data.monsterCenter[1]
        Monster.all_monsters.append(self)
    
    @staticmethod
    def draw(data, canvas):
        for monster in Monster.all_monsters:
            r = monster.size
            canvas.create_oval(monster.r * monster.size, monster.c * monster.size,
                    (monster.r + 1) * monster.size, (monster.c + 1) * monster.size,
                    fill = monster.color)
    
    def move(self, data, dr, dc):
    #moves monster
        if data.gameOver: return
        if ((0 < self.r + dr < data.cols) and (0 < self.c + dc < data.rows)):
                self.x += dx
                self.y += dy
