from tkinter import *
import random
from board import *

###########################################################################
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
        #if move wasn't valid, choose a new direction
        if monster.collideWithWalls(monster.r, monster.c, data):
            newDirections = data.directions.remove(data.direction)
            data.direction = random.choice(newDirections)
            monster.move(data, data.direction)

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