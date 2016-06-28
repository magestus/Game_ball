import tkinter
import random

## Constants
WIDTH = 640
HEIGHT = 480
BG_COLOR = 'white'
color_list = ['green', 'yellow', 'aqua', 'purple', 'blue', 'red']


## Class

class Colobok():
    def  __init__(self, x, y, r, color):
        self.x = x
        self.y = y
        self.r = r
        self.color = color

    def draw(self):
        canvas.create_oval(self.x + self.r, self.y + self.r, self.x - self.r, self.y - self.r, fill=self.color, outline=self.color)

    def hide(self):
        canvas.create_oval(self.x + self.r, self.y + self.r, self.x - self.r, self.y - self.r, fill=BG_COLOR, outline=BG_COLOR)


##Functions
   ##def mouse_click(event):
def create_colob(number):
    global lst
    lst = []
    while len(lst) < number:
        colob = Colobok(500, 200, 50, 'red')
        colob.draw()
        lst.append(colob)

       






root = tkinter.Tk()
root.title('Boom-Boom')
canvas = tkinter.Canvas(root, width=WIDTH, height=HEIGHT, bg=BG_COLOR)
canvas.grid(row=3, column=3)
label.grid(sticky='nsew')
canvas.create_rectangle((WIDTH/3), 0, ((WIDTH/3)*2), HEIGHT)
canvas.create_rectangle(0, (HEIGHT/3), WIDTH, ((HEIGHT/3)*2))
create_colob(5)
root.mainloop()