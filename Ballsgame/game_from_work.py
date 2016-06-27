import tkinter
import random


##Constants
WIDTH=640
HEIGHT=480
BG_COLOR='white'
BAD_COLOR='red'
color_list = ['green', 'yellow', 'aqua', 'purple', 'blue', 'red']

##Class
class Ball():
    def __init__(self, x, y, r, color, dx=0, dy=0):
        self.x = x
        self.y = y
        self.r = r
        self.color = color
        self.dx = dx
        self.dy = dy

    def draw(self):
        canvas.create_oval(self.x + self.r, self.y + self.r, self.x - self.r, self.y - self.r, fill=self.color, outline=self.color)

    def hide(self):
        canvas.create_oval(self.x + self.r, self.y + self.r, self.x - self.r, self.y - self.r, fill=BG_COLOR, outline=BG_COLOR)

    def is_collision(self, ball):
        a = abs(self.x + self.dx - ball.x)
        b = abs(self.y + self.dy - ball.y)
        return (a*a + b*b) **0.5 <= self.r + ball.r

    def move(self):
        # Stolknovenie so stenami
        if (self.x + self.r + self.dx >= WIDTH) or (self.x - self.r + self.dx <= 0):
            self.dx = -self.dx
        if (self.y + self.r + self.dy >= HEIGHT) or (self.y - self.r + self.dy <= 0):
            self.dy = -self.dy
        # Stolknovenie s sharami
        for ball in balls:
            if self.is_collision(ball):
                if ball.color != BAD_COLOR:
                    ball.hide()
                    balls.remove(ball)
                    self.dx = -self.dx
                    self.dy = -self.dy
                else:
                    self.dx = self.dy = 0
        self.hide()
        self.x += self.dx
        self.y += self.dy 
        self.draw()

##Functions
def mouse_click(event):
    global main_ball
    print(event.num, event.x, event.y)
    if event.num == 1:
        if 'main_ball' not in globals():
            main_ball = Ball(event.x, event.y, 30, 'blue', 1, 1)
            main_ball.draw()
        else:
            if main_ball.dx * main_ball.dy > 0:
                main_ball.dy = -main_ball.dy
            else:
                main_ball.dx = -main_ball.dx
    elif event.num == 3:
           if main_ball.dx * main_ball.dy > 0:
              main_ball.dx = -main_ball.dx
           else:
              main_ball.dy = -main_ball.dy

def create_list_of_balls(number):
    global lst
    lst = []
    while len(lst) < number:
        for i in range(number):
            rnd_ball = Ball(random.choice(range(0, WIDTH)), random.choice(range(0,HEIGHT)), random.randint(20,25), random.choice(color_list))
            lst.append(rnd_ball)
            rnd_ball.draw()
    return lst

        
## main_cicle_game
def main():
    if 'main_ball' in globals():
        main_ball.move()
        if len(lst) == 0:
            canvas.create_text(WIDTH/2, HEIGHT/2, text='YOU WON', font='Arial 20', fill='red')
            main_ball.hide()
            main_ball.dx = main_ball.y = 0
            
            
    root.after(1, main)



root = tkinter.Tk()
root.title('Colliding balls')
canvas = tkinter.Canvas(root, width=WIDTH, height=HEIGHT, bg=BG_COLOR)
canvas.pack()
canvas.bind('<Button-1>', mouse_click)
canvas.bind('<Button-2>', mouse_click, '+')
canvas.bind('<Button-3>', mouse_click, '+')
if 'main_ball' in globals():
    del main_ball
balls = create_list_of_balls(10)
main()
root.mainloop()



