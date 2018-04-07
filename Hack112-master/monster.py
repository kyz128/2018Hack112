import random 
import copy

def collideWithWalls(row, col, data):
    for i in range(len(data.maze)):
        for j in range(len(data.maze[0])):
            if ((data.maze[i][j] == 1) and (row == i) and (col == j)):
                return True
    return False

class Monster(object):
    all_monsters = []
    
    def __init__(self, data, color):
        self.color = color
        self.size = data.cellSize
        self.r, self.c = data.monster[0], data.monster[1]
        Monster.all_monsters.append(self)
    
    @staticmethod
    def draw(data, canvas):
        for monster in Monster.all_monsters:
            r = monster.size
            canvas.create_oval(monster.r * monster.size, monster.c * monster.size,
                    (monster.r + 1) * monster.size, (monster.c + 1) * monster.size,
                    fill = monster.color)
    
    @staticmethod
    def move(data, dr, dc):
    #moves monster
        if data.gameOver: return

        for monster in Monster.all_monsters:
            if ((0 < monster.x + dx < (data.cols - 1) * data.cellSize) and 
                (0 < monster.y + dy < (data.rows - 1) * data.cellSize)):
                monster.x += dx
                monster.y += dy
