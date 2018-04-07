from tkinter import *
import random
from board import *
from pacman import Pacman
from monster import Monster

from collections import deque
import numpy as np
import cv2

redLower= (170,70,50)
redUpper= (180,255,255)

#animation framework with openCV modeled from ___insert link
import time
import sys

# Tkinter selector
if sys.version_info[0] < 3:
    from Tkinter import *
    import Tkinter as tk
else:
    from tkinter import *
    import tkinter as tk

import numpy as np
import cv2
from PIL import Image, ImageTk

def opencvToTk(frame):
    """Convert an opencv image to a tkinter image, to display in canvas."""
    rgb_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    rgb_image = cv2.GaussianBlur(rgb_image, (31, 31), 0)
    rgb_image = np.fliplr(rgb_image)
    pil_img = Image.fromarray(rgb_image)
    tk_image = ImageTk.PhotoImage(image=pil_img)
    return tk_image
############################################################################
# Basic animation frame work from 112 website
# https://www.cs.cmu.edu/~112/notes/notes-animations-part1.html
############################################################################
def init(data):
# load data.xyz as appropriate
    data.maze = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0],
                    [0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0],
                    [0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0],
                    [0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0],
                    [0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0],
                    [0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0],
                    [0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0],
                    [0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0],
                    [0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    data.gameOver = False
    data.timer = 0
    data.cellSize = 30
    data.board = Board(data.maze)
    data.rows, data.cols = len(data.maze), len(data.maze[0])
    #moves by width and height of each cell
    data.speedX, data.speedY = data.cellSize, data.cellSize
    data.counter = 0
    data.directions = ['up', 'down', 'left', 'right']
    data.direction = random.choice(data.directions)
    data.pacman = Pacman(data.cols//2 - 1, data.rows//2 - 1, data)
    data.points = deque(maxlen= 64)
    data.center = None
    data.direction= "Right"

def mousePressed(event, data):
# use event.x and event.y
    pass

def keyPressed(event, data):
    if event.keysym == "q":
        data.root.destroy()
    pass
# use event.char and event.keysym
    if (event.keysym == "Up"):
        data.pacman.move(0, -data.cellSize, data)
    elif (event.keysym == "Down"):
        data.pacman.move(0, data.cellSize, data)
    elif (event.keysym == "Left"):
        data.pacman.move(-data.cellSize, 0, data)
    elif (event.keysym == "Right"):
        data.pacman.move(data.cellSize, 0, data)
    
        
def cameraFired(data):
    """Called whenever new camera frames are available.
    Camera frame is available in data.frame. You could, for example, blur the
    image, and then store that back in data. Then, in drawCamera, draw the
    blurred frame (or choose not to).
    """

    (grabbed, data.frame)= data.camera.read()
    hsv= cv2.cvtColor(data.frame, cv2.COLOR_BGR2HSV)
    mask= cv2.inRange(hsv, redLower, redUpper)
    data.frame= cv2.bitwise_and(data.frame, data.frame, mask= mask)
    cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE)[-2]
 
    
    if len(cnts) > 0:
        c = max(cnts, key=cv2.contourArea)
        M = cv2.moments(c)
        if M["m00"] != 0:
            data.center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
        else: 
            data.center= (0,0)


        cv2.circle(data.frame, data.center, 2, (0, 0, 255), 5)
       # cv2.line(data.frame, data.points[i - 1], data.center, (0, 255, 0), 5)
   

def drawCamera(canvas, data):
    data.tk_image = opencvToTk(data.frame)
    canvas.create_image(data.width/4 + data.width/2, data.height / 2, image=data.tk_image)
    
def timerFired(data):
    if data.timer == 0:
        Monster.all_monsters.append(Monster(data, "red"))

    data.timer += 100 #tracks number of milliseconds (1000 milliseconds = 1 sec)
    """x: 0, 600
    y: 0, 500"""
    if data.center!=None:
        x, y= data.center[0], data.center[1]
        if x > 550:
            data.pacman.move(-data.cellSize, 0, data)
            data.direction= "Left"
        elif x < 150:
            data.pacman.move(data.cellSize, 0, data)
            data.direction="Right"
        elif y < 100:
            data.pacman.move(0, -data.cellSize, data)
            data.direction= "Up"
        elif y > 410:
            data.pacman.move(0, data.cellSize, data)
            data.direction= "Down"
        for monster in Monster.all_monsters:
            monster.move(data, data.direction)
            # #if move wasn't valid, choose a new direction
            # newDirections = data.directions.remove(data.direction)
            # data.direction = random.choice(newDirections)
            # move(data, data.direction)

def redrawAll(canvas, data):
# draw in canvas
    data.board.drawBoard(canvas)
    Monster.draw(data, canvas)
    data.pacman.drawPacman(canvas, data)
    drawCamera(canvas, data)

####################################
# use the run function as-is
####################################

def run(width=300, height=300):

    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    data.camera_index = 0

    data.timer_delay = 100 # ms
    data.redraw_delay = 50 # ms
    init(data)
    # Initialize the webcams
    camera = cv2.VideoCapture(data.camera_index)
    data.camera = camera

    # Make tkinter window and canvas
    data.root = Tk()
    canvas = Canvas(data.root, width=data.width, height=data.height)
    canvas.pack()

    # Basic bindings. Note that only timer events will redraw.
    data.root.bind("<Button-1>", lambda event: mousePressed(event, data))
    data.root.bind("<Key>", lambda event: keyPressed(event, data))

    # Timer fired needs a wrapper. This is for periodic events.
    def timerFiredWrapper(data):
        # Ensuring that the code runs at roughly the right periodicity
        start = time.time()
        timerFired(data)
        end = time.time()
        diff_ms = (end - start) * 1000
        delay = int(max(data.timer_delay - diff_ms, 0))
        data.root.after(delay, lambda: timerFiredWrapper(data))

    # Wait a timer delay before beginning, to allow everything else to
    # initialize first.
    data.root.after(data.timer_delay, 
        lambda: timerFiredWrapper(data))

    def redrawAllWrapper(canvas, data):
        start = time.time()

        # Get the camera frame and get it processed.
        _, data.frame = data.camera.read()
        cameraFired(data)

        # Redrawing code
        canvas.delete(ALL)
        redrawAll(canvas, data)

        # Calculate delay accordingly
        end = time.time()
        diff_ms = (end - start) * 1000

        # Have at least a 5ms delay between redraw. Ideally higher is better.
        delay = int(max(data.redraw_delay - diff_ms, 5))

        data.root.after(delay, lambda: redrawAllWrapper(canvas, data))

    # Start drawing immediately
    data.root.after(0, lambda: redrawAllWrapper(canvas, data))

    # Loop tkinter
    data.root.mainloop()

    # Once the loop is done, release the camera.
    print("Releasing camera!")
    data.camera.release()

run(1150, 400)
