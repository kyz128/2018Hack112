from tkinter import *
import random
from board import *

def inBoard(x, y, data):
    r = data.cellSize//2
    nR = len(data.maze)
    nC = len(data.maze[0])
    return (r < x < ((data.cellSize * nC) - r)) and (r < y < ((data.cellSize * nR) - r))

class Monster(object):
    all_monsters = []
    
    def __init__(self, data, color):
        self.color = color
        self.x, self.y = data.x, data.y
        self.r, self.c = self.x//data.cellSize, self.y//data.cellSize
        self.d = data.cellSize #diameter of monster
    
    @staticmethod
    def draw(canvas):
        for monster in Monster.all_monsters:
            canvas.create_oval(monster.x, monster.y, monster.x + monster.d,
                                monster.y + monster.d, fill = monster.color)
    
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
            #move the monster only if the next position is valid
                monster.x, monster.y = temp[0], temp[1]
    
    @staticmethod
    def collideWithWalls(row, col, data):
        for i in range(len(data.maze)):
            for j in range(len(data.maze[0])):
                if ((data.maze[i][j] == 1) and (row == i) and (col == j) and
                inBoard(row * data.cellSize, col * data.cellSize, data)):
                    return True
        return False

############################################################################
# Basic animation frame work from 112 website
# https://www.cs.cmu.edu/~112/notes/notes-animations-part1.html
############################################################################
def init(data):
# load data.xyz as appropriate
    data.maze = [[0, 0, 0, 0, 0, 0, 0, 0]*2 + [0, 0],
                [0, 1, 0, 1, 0, 1, 1, 1]*2 + [0, 0],
                [0, 1, 0, 1, 0, 0, 0, 1]*2 + [0, 0],
                [0, 1, 0, 1, 0, 1, 1, 1]*2 + [0, 0],
                [0, 1, 0, 1, 0, 1, 0, 0]*2 + [0, 0],
                [0, 1, 0, 1, 0, 1, 1, 1]*2 + [0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0]*2 + [0, 0],
                [0, 1, 0, 1, 0, 1, 1, 1]*2 + [0, 0],
                [0, 1, 0, 1, 0, 0, 0, 1]*2 + [0, 0],
                [0, 1, 0, 1, 0, 1, 1, 1]*2 + [0, 0],
                [0, 1, 0, 1, 0, 1, 0, 0]*2 + [0, 0],
                [0, 1, 0, 1, 0, 1, 1, 1]*2 + [0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0]*2 + [0, 0]]
    data.gameOver = False
    data.timer = 0
    data.cellSize = 30
    data.board = Board(data.maze)
    data.rows, data.cols = len(data.maze), len(data.maze[0])
    data.x = random.randint(1, data.width - 1)
    data.y = random.randint(1, data.height - 1)
    #moves by width and height of each cell
    data.speedX, data.speedY = data.cellSize//2, data.cellSize//2 
    data.counter = 0
    data.directions = ['up', 'down', 'left', 'right']
    data.direction = random.choice(data.directions)

def mousePressed(event, data):
# use event.x and event.y
    pass

def keyPressed(event, data):
# use event.char and event.keysym
    pass

def timerFired(data):
    if data.timer == 0:
        Monster.all_monsters.append(Monster(data, "red"))

    data.timer += 100 #tracks number of milliseconds (1000 milliseconds = 1 sec)
    
    for monster in Monster.all_monsters:
        monster.move(data, data.direction)
        # #if move wasn't valid, choose a new direction
        # newDirections = data.directions.remove(data.direction)
        # data.direction = random.choice(newDirections)
        # move(data, data.direction)

def redrawAll(canvas, data):
# draw in canvas
    data.board.drawBoard(canvas)
    Monster.draw(canvas)

####################################
# use the run function as-is
####################################

def run(width=300, height=300):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        canvas.create_rectangle(0, 0, data.width, data.height,
                                fill='white', width=0)
        redrawAll(canvas, data)
        canvas.update()    

    def mousePressedWrapper(event, canvas, data):
        mousePressed(event, data)
        redrawAllWrapper(canvas, data)

    def keyPressedWrapper(event, canvas, data):
        keyPressed(event, data)
        redrawAllWrapper(canvas, data)

    def timerFiredWrapper(canvas, data):
        timerFired(data)
        redrawAllWrapper(canvas, data)
        # pause, then call timerFired again
        canvas.after(data.timerDelay, timerFiredWrapper, canvas, data)
    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    data.timerDelay = 100 # milliseconds
    init(data)
    # create the root and the canvas
    root = Tk()
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.pack()
    # set up events
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    timerFiredWrapper(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed
    print("bye!")

run(520, 400)