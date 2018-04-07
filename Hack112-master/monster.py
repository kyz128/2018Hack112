import random 
def inBoard(x, y, data):
    r = data.cellSize//2
    nR = len(data.maze)
    nC = len(data.maze[0])
    return (r < x < ((data.cellSize * nC) - r)) and (r < y < ((data.cellSize * nR) - r))

class Monster(object):
    all_monsters = []
    
    def __init__(self, data, color):
        self.color = color
        self.x = random.randint(1, data.width - 1)
        self.y = random.randint(1, data.height - 1)
        self.r, self.c = self.x//data.cellSize, self.y//data.cellSize
        Monster.all_monsters.append(self)
    
    @staticmethod
    def draw(data, canvas):
        for monster in Monster.all_monsters:
            canvas.create_oval(monster.x, monster.y, monster.x + data.cellSize,
                            monster.y + data.cellSize, fill = monster.color)
    
    @staticmethod
    def move(data, direction):
    #moves monster
        if data.gameOver: return

        for monster in Monster.all_monsters:
            temp = [monster.x, monster.y]
            if direction == 'up':
                temp[1] -= data.speedY
            elif direction == 'down':
                temp[1] += data.speedY
            elif direction == 'left':
                temp[0] -= data.speedX
            elif direction == 'right':
                temp[0] += data.speedX
            
            if not monster.collideWithWalls(monster.r, monster.c, data):
            # #move the monster only if the next position is valid
                monster.x, monster.y = temp[0], temp[1]
    
    @staticmethod
    def collideWithWalls(row, col, data):
        for i in range(len(data.maze)):
            for j in range(len(data.maze[0])):
                if ((data.maze[i][j] == 1) and (row == i) and (col == j) and
                inBoard(row * data.cellSize, col * data.cellSize, data)):
                    return True
        return False
