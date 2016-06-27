import tkinter
import random

#CONSTANTS
WIDTH=640
HEIGHT=480
BG_COLOR='white'
ZERO = 0
MAIN_BALL_RADIUS = 30
MAIN_BALL_COLOR = 'red'
INIT_DX = 1
INIT_DY = 1
DELAY = 5
COLORS = ['green', 'aqua', 'yellow']

# balls Class
class Balls():
    def __init__(self, x, y, r, color, dx=0, dy=0):
        self.x = x
        self.y = y
        self.r = r
        self.color = color
        self.dx = dx
        self.dy = dy

    def draw(self):
        canvas.create_oval(self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r, fill=self.color)

    def hide(self):
        canvas.create_oval(self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r, fill=BG_COLOR, outline=BG_COLOR)
    
    def move(self):
        #colliding with walls
        if (self.x + self.r + self.dx >= WIDTH) or (self.x - self.r + self.dx <= ZERO):
            self.dx = -self.dx
        if (self.y + self.r + self.dy >= HEIGHT) or (self.y - self.r + self.dy <= ZERO):
            self.dy = -self.dy
        self.hide()
        self.x += self.dx
        self.y += self.dy
        self.draw()
        

# mouse events
def mouse_click(event):
    global main_ball
    print(event.num, event.x, event.y)
    if event.num == 1:
        if 'main_ball' not in globals():
            main_ball = Balls(event.x, event.y, MAIN_BALL_RADIUS, MAIN_BALL_COLOR , INIT_DX, INIT_DY)
            main_ball.draw()
        else: #Turn Left
            if main_ball.dx * main_ball.dy > 0:
                main_ball.dy = -main_ball.dy
            else:
                main_ball.dx = -main_ball.dx
    elif event.num == 3: #turn right
        if main_ball.dx * main_ball.dy > 0:
                main_ball.dx = -main_ball.dx
        else:
                main_ball.dy = -main_ball.dy       

# main cicle game
def main():
    if 'main_ball' in globals():
        main_ball.move()
    root.after(DELAY, main)

# Create list of balls
def create_list_of_balls(number):
    lst=[]
    while len(lst) < number:
        next_ball = Balls(random.choice(range(0, WIDTH)), 
                          random.choice(range(0, HEIGHT)), 
                          random.choice(range(15, 35)),
                          random.choice(COLORS))
        lst.append(next_ball)
        next_ball.draw
    return lst


root = tkinter.Tk()
root.title('colliding Balls')
canvas = tkinter.Canvas(root, width=WIDTH, height=HEIGHT, bg=BG_COLOR)
canvas.pack()
canvas.bind('<Button-1>', mouse_click)
canvas.bind('<Button-2>', mouse_click, '+')
canvas.bind('<Button-3>', mouse_click, '+')
if 'main_ball' in globals():
    del main_ball
balls = create_list_of_balls(5)
main()
root.mainloop()