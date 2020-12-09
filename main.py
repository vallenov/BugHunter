import random
import time
import math
from tkinter import *

HEIGHT = 500
WIDTH = 1000

class Bug:
    numofbugs = 0
    def __init__(self, name):
        Bug.numofbugs += 1
        self.RAD = random.randint(10, 20)
        self.speed = random.randint(5, 10)
        self.coordx = random.randint(20, WIDTH - 20)
        self.coordy = random.randint(20, HEIGHT - 20)
        self.coordx_change = random.randint(-1, 1)
        self.coordy_change = random.randint(-1, 1)
        Bug.numofbugs += 1
        self.name = name
        self.METEOR = c.create_oval(self.coordx - self.RAD / 2, self.coordy - self.RAD / 2, self.coordx + self.RAD / 2, self.coordy + self.RAD / 2, fill="black")
    def __del__(self):
        Bug.numofbugs -= 1

    def move(self):  #
        left, up, right, down = c.coords(self.METEOR)
        # print('LEFT: {}, UP: {}, RIGHT: {}, DOWN: {}, bounce: {}'.format(left,up,right,down,self.bounce))
        if ((((up) <= 0) or ((down) >= HEIGHT)) and (self.bounce == False)):
            self.coordy_change = -self.coordy_change
            self.bounce = True
        elif ((((left) <= 0) or ((right) >= WIDTH)) and (self.bounce == False)):
            self.coordx_change = -self.coordx_change
            self.bounce = True
        else:
            if (up > 0) and (down < HEIGHT) and (left > 0) and (right < WIDTH):
                self.bounce = False

        c.move(self.METEOR, self.coordx_change, self.coordy_change)

root = Tk()
root.title("Bug Hunter")  # Название окна
c = Canvas(root, width=WIDTH, height=HEIGHT, background="#999999")  # Создание окна
c.pack()

def main_move_loop(): #
    for i in range(len(dictBug)):
        dictBug[i].move()
    root.after(5,main_move_loop)

dictBug = {}

for i in range(9):
    dictBug[i] = Bug(i)

main_move_loop()
c.focus_set()
root.mainloop()
