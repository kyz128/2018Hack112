import socket

class Pacman(object):

    def __init__(self, PID, x, y, points=0):
        self.PID = PID
        self.x = x
        self.y = y
        self.size = 30
        self.points= points
    
    @staticmethod
    def food(data):
        data.food=[]
        for row in range(len(data.board)):
            for col in range(len(data.board[0])):
                if data.board[row][col]==0:
                    data.food.append((row,col))
            
    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def changePID(self, PID):
        self.PID = PID
    
    def eat(self):
        self.points+=10

    def drawPacman(self, canvas, color):
        r = self.size
        canvas.create_oval(self.x-r, self.y-r, 
                           self.x+r, self.y+r, fill=color)
        canvas.create_text(self.x, self.y, text=self.PID, fill="white")

